import uuid
from trulens_eval import TruChain, TruLlama, Tru, Feedback
from ..targets import Target, LangChainTarget, LlamaIndexTarget
from ..prompts.PromptSet import PromptSet
from typing import List
from .UnknownTargetException import UnknownTargetException


def evaluate(target: Target, prompts: PromptSet, feedbacks: List[Feedback], 
                    app_id: str | None = None, reset_database: bool = True):

    if app_id is None:
        app_id = uuid.uuid4().hex
    
    if not isinstance(target, (LangChainTarget, LlamaIndexTarget)):
        raise UnknownTargetException()
    
    tru = Tru()
    tru.reset_database()

    recorders = {
        LangChainTarget: TruChain,
        LlamaIndexTarget: TruLlama
    }
    recorder_class = recorders.get(type(target))
    recorder = recorder_class(target.chain, app_id=app_id, feedbacks=feedbacks)

    with recorder as recording:
        for prompt in prompts:
            response = target.invoke(prompt.input)

    tru.run_dashboard()