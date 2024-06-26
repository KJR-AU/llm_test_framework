import uuid
from trulens_eval import TruChain, TruLlama, Feedback
from ..targets import Target, LangChainTarget, LlamaIndexTarget
from ..prompts.PromptSet import PromptSet
from typing import List
from .UnknownTargetException import UnknownTargetException

class TestSet:

    def __init__(self, prompts: PromptSet, feedbacks: List[Feedback], name: str = ""):
        self.prompts: PromptSet = prompts
        self.feedbacks: List[Feedback] = feedbacks
        self.name = name

    def evaluate(self, target: Target, app_id: str | None = None, reset_database: bool = False):
        
        if reset_database:
            self.reset_database()

        recorder = self.get_recorder(target, app_id=app_id)

        with recorder as recording:
            for prompt in self.prompts:
                response = target.invoke(prompt.input)
        
        return recording


    def get_recorder(self, target, app_id: str | None = None):
        if app_id is None:
            app_id = uuid.uuid4().hex
        
        if not isinstance(target, (LangChainTarget, LlamaIndexTarget)):
            raise UnknownTargetException()

        recorders = {
            LangChainTarget: TruChain,
            LlamaIndexTarget: TruLlama
        }
        recorder_class = recorders.get(type(target))
        recorder = recorder_class(target.chain, app_id=app_id, feedbacks=self.feedbacks, selector_nocheck=True)
        return recorder