from .FeedbackProvider import FeedbackProvider
from trulens_eval.feedback.provider import LiteLLM

class LiteLLMProvider(FeedbackProvider):
    def __init__(self, name: str = "litellm", model_name: str = "gpt-3.5-turbo", **kwargs) -> None:
        super().__init__(name, model_name)
        self._completion_args = kwargs

    @property
    def provider(self):
        return LiteLLM(
            model_engine=self.model_name, 
            completion_args=self._kwargs
        )

    @property
    def completion_args(self):
        return self._completion_args

    @completion_args.setter
    def completion_args(self, **kwargs):
        self._completion_args = kwargs