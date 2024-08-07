from trulens_eval import Feedback

from ..metric import Metric


class Insensitivity(Metric):
    def __init__(self) -> None:
        super().__init__(name="Insensitivity", higher_is_better=False)

    @property
    def feedback_name(self) -> str:
        return "insensitivity_with_cot_reasons"

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return ()
