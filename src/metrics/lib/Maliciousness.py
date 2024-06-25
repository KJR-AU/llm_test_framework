from .Metric import Metric
from .MetricNotAvailableError import MetricNotAvailableError


class Maliciousness(Metric):
    
    def __init__(self):
        super().__init__(name="Maliciousness")

    @property
    def feedback_name(self):
        return "maliciousness_with_cot_reasons"