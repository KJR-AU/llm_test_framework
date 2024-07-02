import uuid
from trulens_eval import TruChain, TruLlama, Feedback, TruCustomApp
from ..targets import Target, LangChainTarget, LlamaIndexTarget, CustomTarget
from ..prompts.PromptSet import PromptSet
from typing import List
from .UnknownTargetException import UnknownTargetException
from ..metrics.Metric import Metric

class TestSet:

    SUPPORTED_PROVIDERS = [
        "openai",
        "llama3"
    ]

    def __init__(self, prompts: PromptSet, feedbacks: List[Feedback], name: str = "", provider: str = None):
        self.prompts: PromptSet = prompts
        self.feedbacks: List[Feedback] = feedbacks
        self.name: str = name
        self.provider = provider
            

    def evaluate(self, target: Target, app_id: str | None = None, reset_database: bool = False):
        """
        """
        
        feedbacks = self._get_coerced_feedbacks()

        if reset_database:
            self.reset_database()

        recorder = self.get_recorder(target, feedbacks, app_id=app_id)

        with recorder as recording:
            for prompt in self.prompts:
                response = target.invoke(prompt.input)
        
        return recording


    def get_recorder(self, target: Target, feedbacks: List[Feedback], app_id: str | None = None):
        if app_id is None:
            app_id = uuid.uuid4().hex
        
        if not isinstance(target, (LangChainTarget, LlamaIndexTarget, CustomTarget)):
            raise UnknownTargetException()

        recorders = {
            LangChainTarget: TruChain,
            LlamaIndexTarget: TruLlama,
            CustomTarget: TruCustomApp
        }        
        recorder_class = recorders.get(type(target))
        recorder = recorder_class(target.chain, app_id=app_id, feedbacks=feedbacks, selector_nocheck=True)
        return recorder

    
    @property
    def provider(self):
        return self._provider

    @provider.setter
    def provider(self, provider: str | None):
        if provider not in [None, *self.SUPPORTED_PROVIDERS]:
            supported_provider_string: str = ", ".join(self.SUPPORTED_PROVIDERS)
            raise ValueError(f"unsupported provider: '{self.provider}'. Provider must be None or one of {supported_provider_string}")
        self._provider = provider


    def _get_coerced_feedbacks(self):
        """Returns a list of trulens-compatible feedback functions. Attempts 
        to use a user-set provider attribute to extract the feedback function
        from a Metric object.
        """
        coerced_feedbacks = []
        for feedback in self.feedbacks:
            
            # Try to set the provider if no provider has been set
            if isinstance(feedback, Metric):
                if self.provider is None:
                    raise ValueError("provider cannot be determined")
                coerced_feedback = getattr(feedback, self.provider)
            elif isinstance(feedback, Feedback):
                coerced_feedback = feedback
            else:
                raise TypeError("unrecognised feedback type")
            
            coerced_feedbacks.append(coerced_feedback)
        return coerced_feedbacks