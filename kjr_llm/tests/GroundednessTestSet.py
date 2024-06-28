from .TestSet import TestSet
from ..metrics import Groundedness
from ..prompts import PromptSet

class GroundednessTestSet(TestSet):
    def __init__(self, prompts: PromptSet, context_path, name: str  | None = None, provider: str | None = None):
        feedback = Groundedness(context_path)
        super().__init__(prompts, [feedback], name=name, provider=provider)

    @classmethod
    def from_file(cls, file_path, *args, **kwargs):
        prompt_set = PromptSet.from_json_file(file_path)
        return cls(prompt_set, *args, **kwargs)