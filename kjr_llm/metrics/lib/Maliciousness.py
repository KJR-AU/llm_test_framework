# Import the base Metric class from the parent package.
from ..Metric import Metric

# Import the custom exception MetricNotAvailableError from the parent package.
from ...exceptions import MetricNotAvailableError

# Define a class named Maliciousness that inherits from the Metric class.
class Maliciousness(Metric):
    
    # Constructor method to initialize the Maliciousness object.
    def __init__(self):
        # Call the constructor of the parent Metric class with the name "Maliciousness" and specify that higher values are not better.
        super().__init__(name="Maliciousness", higher_is_better=False)

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "maliciousness_with_cot_reasons"

    # Method to apply a selector to the feedback.
    def _feedback_with_selector(self, feedback):
        # Apply the feedback selector to the output and return the result.
        return (
            feedback
            .on_output()  # Select feedback based on the output.
        )