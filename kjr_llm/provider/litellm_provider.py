from typing import Any

from trulens_eval.feedback.provider import LiteLLM

from .feedback_provider import FeedbackProvider


class LiteLLMProvider(FeedbackProvider):
    def __init__(self, name: str = "litellm", model_name: str = "gpt-3.5-turbo", **kwargs: str) -> None:
        super().__init__(name, model_name)
        self._completion_args = kwargs

    @property
    def provider(self) -> LiteLLM:
        return LiteLLM(model_engine=self.model_name, completion_args=self.completion_args)

    @property
    def completion_args(self) -> dict[str, Any]:
        return self._completion_args

    @completion_args.setter
    def completion_args(self, **kwargs: str) -> None:
        self._completion_args = kwargs
