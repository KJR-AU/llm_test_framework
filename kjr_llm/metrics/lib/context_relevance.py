import numpy as np
from trulens.core.feedback.feedback import Feedback
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
        return (
            feedback.on(self.query_path)  # Select feedback based on the query path.
            .on(self.context_path)  # Select feedback based on the context path.
            .aggregate(np.mean)  # Aggregate the selected feedback using the mean function.
        )
