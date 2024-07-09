from .provider import Provider
from .FeedbackProvider import FeedbackProvider
from .LiteLLMProvider import LiteLLMProvider
from .OpenAIProvider import OpenAIProvider
from .Llama3Provider import Llama3Provider
from .DeepSeekProvider import DeepSeekProvider

class Provider:
    llama3 = Llama3Provider()
    openai = OpenAIProvider()
    litellm = LiteLLMProvider()
    deepseek = DeepSeekProvider()
