from trulens.core.feedback.feedback import Feedback

from ...exceptions import MetricNotAvailableError
from ..metric import Metric


class SelfHarm(Metric):
    def __init__(self) -> None:
        super().__init__(name="Self Harm", higher_is_better=False)

    @property
    def feedback_name(self) -> str:
        return "moderation_selfharm"

    @property
    def llama3(self) -> Feedback:
        raise MetricNotAvailableError()

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return feedback.on_output()
