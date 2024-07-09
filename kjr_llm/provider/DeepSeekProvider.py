from .LiteLLMProvider import LiteLLMProvider

class DeepSeekProvider(LiteLLMProvider):
    def __init__(self, **kwargs):
        name = "deepseek"
        model_name: str = "deepseek/deepseek-chat"
        super().__init__(name, model_name, **kwargs)