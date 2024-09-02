from trulens.core.feedback.feedback import Feedback

from ..provider import Provider


class Metric:
    """
    A base class for defining custom metrics to evaluate language models or RAG applications.
    """

    def __init__(self, *args: object, **kwargs: object) -> None:
        """
        Initializes a new instance of the Metric class.

        :param args: Variable length argument list.
        :param kwargs: Arbitrary keyword arguments.
        """
        self.args = args
        self.kwargs = kwargs

    def _feedback(self, provider: Provider) -> Feedback:
        """
        Generates a feedback object using the specified provider.

        :param provider: The feedback provider to use.
        :return: A Feedback object.
        """
        feedback_metric = getattr(provider, self.feedback_name)
        return Feedback(feedback_metric, *self.args, **self.kwargs)

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        """
        Applies a feedback selector to the feedback object. This method is intended to be overridden in subclasses.

        :param feedback: The feedback object to apply the selector to.
        :return: The feedback object with the selector applied.
        """
        raise NotImplementedError()

    @property
    def feedback_name(self) -> str:
        """
        The name of the feedback metric. This property should be overridden in subclasses.
        """
        raise NotImplementedError()

    @property
    def openai(self) -> Feedback:
        """
        Generates a feedback object using the OpenAI provider.

        :return: A Feedback object with the OpenAI provider.
        """
        feedback = self._feedback(Provider.openai.provider)
        return self._feedback_with_selector(feedback)

    @property
    def llama3(self) -> Feedback:
        """
        Generates a feedback object using the LiteLLM (llama3) provider.

        :return: A Feedback object with the LiteLLM (llama3) provider.
        """
        Provider.llama3.completion_args = {"api_base": "http://localhost:11434"}
        feedback = self._feedback(Provider.llama3.provider)
        return self._feedback_with_selector(feedback)

    @property
    def deepseek(self) -> Feedback:
        """
        Generates a feedback object using the LiteLLM (deepseek) provider.

        :return: A Feedback object with the LiteLLM (deepseek) provider.
        """
        feedback = self._feedback(Provider.deepseek.provider)
        return self._feedback_with_selector(feedback)
