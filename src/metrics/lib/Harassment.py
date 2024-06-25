from .Metric import Metric
from .MetricNotAvailableError import MetricNotAvailableError


class Harassment(Metric):
    
    def __init__(self):
        super().__init__(name="Harassment")

    @property
    def feedback_name(self):
        return "moderation_harassment"

    @property
    def llama3(self):
        raise MetricNotAvailableError()