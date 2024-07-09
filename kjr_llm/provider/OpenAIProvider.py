from trulens_eval.feedback.provider import OpenAI
from .FeedbackProvider import FeedbackProvider

class OpenAIProvider(FeedbackProvider):
    def __init__(self, model_name: str = "gpt-3.5-turbo") -> None:
        name = "openai"
        super().__init__(name, model_name)

    @property
    def provider(self):
        return OpenAI(model_engine=self.model_name)
