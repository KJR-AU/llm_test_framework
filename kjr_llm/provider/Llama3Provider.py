from .LiteLLMProvider import LiteLLMProvider

class Llama3Provider(LiteLLMProvider):
    def __init__(self, **kwargs):
        name = "llama3"
        model_name: str = "ollama/llama3"
        super().__init__(name, model_name, **kwargs)