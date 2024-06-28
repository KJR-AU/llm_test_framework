from ..Metric import Metric

class Groundedness(Metric):
    
    def __init__(self, context_path):
        self.context_path = context_path
        super().__init__(name="Groundedness")

    @property
    def feedback_name(self):
        return "groundedness_measure_with_cot_reasons"

    def _feedback_with_selector(self, feedback):
        return (
            feedback
            .on(self.context_path.collect())
            .on_output()
        )