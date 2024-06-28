from ..Metric import Metric
import numpy as np

class ContextRelevance(Metric):
    
    def __init__(self, query_path, context_path):
        self.query_path = query_path
        self.context_path = context_path
        super().__init__(name="Context Relevance")

    @property
    def feedback_name(self):
        return "context_relevance_with_cot_reasons"

    def _feedback_with_selector(self, feedback):
        return (
            feedback
            .on(self.query_path)
            .on(self.context_path)
            .aggregate(np.mean)
        )