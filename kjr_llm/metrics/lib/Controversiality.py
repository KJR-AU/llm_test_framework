# Import the base Metric class from the parent package.
from ..Metric import Metric

# Import the custom exception MetricNotAvailableError from the parent package.
from ...exceptions import MetricNotAvailableError

# Define a class named Controversiality that inherits from the Metric class.
class Controversiality(Metric):
    
    # Constructor method to initialize the Controversiality object.
    def __init__(self):
        super().__init__(name="Controversiality", higher_is_better=False)

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "controversiality_with_cot_reasons"

    # Method to apply a selector to the feedback.
    def _feedback_with_selector(self, feedback):
        # Apply the feedback selector to the output and return the result.
        return (
            feedback
            .on_output()  # Select feedback based on the output.
        )