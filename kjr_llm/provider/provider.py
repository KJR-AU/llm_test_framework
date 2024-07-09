from typing import List

class Provider:
    OPENAI: str = "openai"
    LLAMA3: str = "llama3"
    DEEPSEEK: str = "deepseek"

    all: List[str] = [
        OPENAI,
        LLAMA3,
        DEEPSEEK
    ]

    @classmethod
    def is_supported(cls, provider: str) -> bool:
        return provider in cls.all
