# Import the base Metric class from the parent package.
from ..Metric import Metric

# Import the custom exception MetricNotAvailableError from the parent package.
from ..MetricNotAvailableError import MetricNotAvailableError

# Define a class named Insensitivity that inherits from the Metric class.
class Insensitivity(Metric):
    
    # Constructor method to initialize the Insensitivity object.
    def __init__(self):
        # Call the constructor of the parent Metric class with the name "Insensitivity".
        super().__init__(name="Insensitivity")

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "insensitivity_with_cot_reasons"

    # Method to apply a selector to the feedback.
    def _feedback_with_selector(self, feedback):
        # Apply the feedback selector to the output and return the result.
        return (
            feedback
            .on_output()  # Select feedback based on the output.
        )