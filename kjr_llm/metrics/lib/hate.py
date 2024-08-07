from trulens_eval import Feedback

from ...exceptions import MetricNotAvailableError
from ..metric import Metric


class Hate(Metric):
    def __init__(self) -> None:
        super().__init__(name="Hate", higher_is_better=False)

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return ()

    @property
    def feedback_name(self) -> str:
        return "moderation_hate"

    @property
    def llama3(self) -> Feedback:
        raise MetricNotAvailableError()
