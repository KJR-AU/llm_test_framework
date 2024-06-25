from .Metric import Metric
from .MetricNotAvailableError import MetricNotAvailableError


class Criminality(Metric):
    
    def __init__(self):
        super().__init__(name="Criminality")

    @property
    def feedback_name(self):
        return "criminality_with_cot_reasons"