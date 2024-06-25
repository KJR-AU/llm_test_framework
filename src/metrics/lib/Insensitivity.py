from .Metric import Metric
from .MetricNotAvailableError import MetricNotAvailableError


class Insensitivity(Metric):
    
    def __init__(self):
        super().__init__(name="Insensitivity")

    @property
    def feedback_name(self):
        return "insensitivity_with_cot_reasons"

    def __feedback_with_selector(self, feedback):
        return (
            feedback
            .on_output()
        )