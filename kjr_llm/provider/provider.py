from typing import List

class Provider:
    OPENAI: str = "openai"
    LLAMA3: str = "llama3"
    DEEPSEEKER: str = "deepseeker"

    all: List[str] = [
        OPENAI,
        LLAMA3,
        DEEPSEEKER
    ]

    @classmethod
    def is_supported(cls, provider: str) -> bool:
        return provider in cls.all
