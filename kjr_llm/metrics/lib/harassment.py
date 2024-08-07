from trulens_eval import Feedback

from ...exceptions import MetricNotAvailableError
from ..metric import Metric


class Harassment(Metric):
    def __init__(self) -> None:
        super().__init__(name="Harassment", higher_is_better=False)

    @property
    def feedback_name(self) -> str:
        return "moderation_harassment"

    @property
    def llama3(self) -> Feedback:
        raise MetricNotAvailableError()

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return ()
