# Import the base Metric class from the parent package.
from ..Metric import Metric

# Import the custom exception MetricNotAvailableError from the parent package.
from ..MetricNotAvailableError import MetricNotAvailableError

# Define a class named Criminality that inherits from the Metric class.
class Criminality(Metric):
    
    # Constructor method to initialize the Criminality object.
    def __init__(self):
        # Call the constructor of the parent Metric class with the name "Criminality" and specify that higher values are not better.
        super().__init__(name="Criminality", higher_is_better=False)

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "criminality_with_cot_reasons"

    # Method to apply a selector to the feedback.
    def _feedback_with_selector(self, feedback):
        # Apply the feedback selector to the output and return the result.
        return (
            feedback
            .on_output()  # Select feedback based on the output.
        )