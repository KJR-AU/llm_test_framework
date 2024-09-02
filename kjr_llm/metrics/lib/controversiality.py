from trulens.core.feedback.feedback import Feedback

from ..metric import Metric


class Controversiality(Metric):
    def __init__(self) -> None:
        super().__init__(name="Controversiality", higher_is_better=False)

    @property
    def feedback_name(self) -> str:
        return "controversiality_with_cot_reasons"

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return feedback.on_output()
