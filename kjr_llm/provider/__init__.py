from .deepseek_provider import DeepSeekProvider
from .feedback_provider import FeedbackProvider
from .litellm_provider import LiteLLMProvider
from .llama3_provider import Llama3Provider
from .openai_provider import OpenAIProvider


class Provider:
    llama3 = Llama3Provider()
    openai = OpenAIProvider()
    litellm = LiteLLMProvider()
    deepseek = DeepSeekProvider()


__all__ = ["FeedbackProvider", "Provider", "LiteLLMProvider", "Llama3Provider", "OpenAIProvider", "DeepSeekProvider"]
