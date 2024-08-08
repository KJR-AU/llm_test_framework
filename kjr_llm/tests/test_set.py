import uuid
from typing import Self, TypeVar

from trulens_eval import Feedback, TruBasicApp, TruChain, TruCustomApp, TruLlama
from trulens_eval.schema.record import Record

from ..exceptions import UnknownTargetError
from ..metrics.metric import Metric
from ..prompts.prompt_set import PromptSet
from ..provider import FeedbackProvider
from ..targets import CustomTarget, LangChainTarget, LlamaIndexTarget, Target

TrulensApp = TypeVar("TrulensApp", TruChain, TruLlama, TruCustomApp, TruBasicApp)


class TestSet:
    """
    A class representing a set of tests to evaluate a target using a collection of prompts and feedback metrics.
    """

    def __init__(
        self,
        prompts: PromptSet,
        feedbacks: list[Feedback],
        name: str = "",
        default_provider: FeedbackProvider | None = None,
    ):
        """
        Initializes a new instance of the TestSet class.

        :param prompts: The set of prompts to be evaluated.
        :param feedbacks: The list of feedback metrics to be used for evaluation.
        :param name: The name of the test set.
        :param provider: The feedback provider to be used.
        """
        self.prompts: PromptSet = prompts
        self.feedbacks: list[Feedback] = feedbacks
        self.name: str = name
        self.default_provider: FeedbackProvider = default_provider

    @classmethod
    def from_prompts_file_json(
        cls, file_path: str, feedbacks: list[Feedback], name: str = "", default_provider: FeedbackProvider | None = None
    ) -> Self:
        prompts = PromptSet.from_json_file(file_path)
        return cls(prompts, feedbacks, name=name, default_provider=default_provider)

    def evaluate(self, target: Target, app_id: str | None = None) -> Record:
        """
        Evaluates the target using the prompts and feedbacks defined in the test set.

        :param target: The target to be evaluated.
        :param app_id: The application ID for the evaluation.
        :param reset_database: If True, resets the database before evaluation.
        :return: The recording of the evaluation.
        """

        feedbacks = self._get_coerced_feedbacks()

        recorder = self.get_recorder(target, feedbacks, app_id=app_id)

        with recorder as recording:
            for prompt in self.prompts:
                target.invoke(prompt.input)

        return recording

    def get_recorder(
        self, target: Target, feedbacks: list[Feedback], app_id: str | None = None
    ) -> TruChain | TruLlama | TruCustomApp | TruBasicApp:
        """
        Creates a recorder for the evaluation.

        :param target: The target to be evaluated.
        :param feedbacks: The list of feedback metrics to be used.
        :param app_id: The application ID for the evaluation.
        :return: A recorder instance.
        """
        if app_id is None:
            app_id = uuid.uuid4().hex

        if not isinstance(target, LangChainTarget | LlamaIndexTarget | CustomTarget):
            raise UnknownTargetError()

        # Define a dictionary to map target types to their corresponding recorder classes
        recorders = {LangChainTarget: TruChain, LlamaIndexTarget: TruLlama, CustomTarget: TruCustomApp}
        recorder_class = recorders.get(type(target))
        if recorder_class is None:
            raise UnknownTargetError()
        return recorder_class(target.app, app_id=app_id, feedbacks=feedbacks, selector_nocheck=True)

    @property
    def default_provider(self) -> FeedbackProvider | None:
        """
        The feedback provider used in the test set.
        """
        return self._provider

    @default_provider.setter
    def default_provider(self, provider: FeedbackProvider | None) -> None:
        """
        Sets the feedback provider.

        :param provider: The feedback provider to be used.
        """
        if provider is not None and not isinstance(provider, FeedbackProvider):
            raise ValueError(f"unsupported provider: '{provider}'. Provider must be one of (None, FeedbackProvider)")
        self._provider = provider

    def _get_coerced_feedbacks(self) -> list[Metric]:
        """Returns a list of trulens-compatible feedback functions. Attempts
        to use a user-set provider attribute to extract the feedback function
        from a Metric object.
        """
        coerced_feedbacks = []
        for feedback in self.feedbacks:
            # Try to set the provider if no provider has been set
            if isinstance(feedback, Metric):
                if self.default_provider is None:
                    error_msg = "provider cannot be determined"
                    raise ValueError(error_msg)
                coerced_feedback = getattr(feedback, self.default_provider.name)
            elif isinstance(feedback, Feedback):
                coerced_feedback = feedback
            else:
                type_error_msg: str = "unrecognised feedback type"
                raise TypeError(type_error_msg)

            coerced_feedbacks.append(coerced_feedback)
        return coerced_feedbacks
