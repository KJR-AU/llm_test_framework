import numpy as np
from trulens_eval import Feedback
from trulens_eval.utils.serial import Lens

from ..metric import Metric


class ContextRelevance(Metric):
    def __init__(self, query_path: Lens, context_path: Lens):
        self.query_path: Lens = query_path
        self.context_path: Lens = context_path
        super().__init__(name="Context Relevance")

    @property
    def feedback_name(self) -> str:
        return "context_relevance_with_cot_reasons"

    def _feedback_with_selector(self, feedback: Feedback) -> Feedback:
        return feedback.on(self.context_path).aggregate(np.mean)
