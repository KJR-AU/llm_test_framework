from trulens_eval import Feedback

from ...exceptions import MetricNotAvailableError
from ..metric import Metric


class ViolenceGraphic(Metric):
    def __init__(self) -> None:
        super().__init__(name="Violence Graphic", higher_is_better=False)

    @property
    def feedback_name(self) -> str:
        return "moderation_violencegraphic"

    @property
    def llama3(self) -> None:
        raise MetricNotAvailableError()

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return feedback.on_output()
