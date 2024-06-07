import uuid
from trulens_eval import TruChain, Tru
from ..targets.Target import Target
from ..prompts.PromptSet import PromptSet

def evaluate(target: Target, prompts: PromptSet, feedbacks, app_id: str | None = None):
    if app_id is None:
        app_id = uuid.uuid4().hex
    tru = Tru()
    tru.reset_database()
    recorder = TruChain(
        chain,
        app_id=app_id,
        feedbacks=feedbacks
    )

    with recorder as recording:
        for prompt in prompts:
            response = target.invoke(prompt.input)

    tru.run_dashboard()