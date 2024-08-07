from trulens_eval import Feedback

from ...exceptions import MetricNotAvailableError
from ..metric import Metric


class HarassmentThreatening(Metric):
    def __init__(self) -> None:
        super().__init__(name="Harassment Threatening", higher_is_better=False)

    @property
    def feedback_name(self) -> str:
        return "moderation_harassment_threatening"

    @property
    def llama3(self) -> Feedback:
        raise MetricNotAvailableError()

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return ()
