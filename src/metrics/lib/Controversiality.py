from .Metric import Metric
from .MetricNotAvailableError import MetricNotAvailableError


class Controversiality(Metric):
    
    def __init__(self):
        super().__init__(name="Controversiality")

    @property
    def feedback_name(self):
        return "controversiality_with_cot_reasons"

    def __feedback_with_selector(self, feedback):
        return (
            feedback
            .on_output()
        )