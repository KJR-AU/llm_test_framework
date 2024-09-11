from trulens.core.feedback.feedback import Feedback

from ..metric import Metric


class Maliciousness(Metric):
    def __init__(self) -> None:
        super().__init__(name="Maliciousness", higher_is_better=False)

    @property
    def feedback_name(self) -> str:
        return "maliciousness_with_cot_reasons"

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return feedback.on_output()
