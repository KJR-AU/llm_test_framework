from trulens.core.feedback.feedback import Feedback

from ..metric import Metric


class AnswerRelevance(Metric):
    def __init__(self) -> None:
        super().__init__(name="Answer Relevance")

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return feedback.on_input_output()

    @property
    def feedback_name(self) -> str:
        return "relevance_with_cot_reasons"
