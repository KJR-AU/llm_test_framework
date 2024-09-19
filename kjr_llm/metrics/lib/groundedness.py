from trulens.core.feedback.feedback import Feedback
from trulens.core.utils.serial import Lens

from ..metric import Metric


class Groundedness(Metric):
    def __init__(self, context_path: Lens) -> None:
        self.context_path: Lens = context_path

        super().__init__(name="Groundedness")

    @property
    def feedback_name(self) -> str:
        return "groundedness_measure_with_cot_reasons"

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return feedback.on(self.context_path.collect()).on_output()
