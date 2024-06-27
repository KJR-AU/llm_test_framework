# Import the base Metric class from the parent package.
from ..Metric import Metric

# Define a class named Groundedness that inherits from the Metric class.
class Groundedness(Metric):
    
    # Constructor method to initialize the Groundedness object.
    def __init__(self, context_path):
        # Store the path to the context data.
        self.context_path = context_path
        # Call the constructor of the parent Metric class with the name "Groundedness".
        super().__init__(name="Groundedness")

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "groundedness_measure_with_cot_reasons"

    # Method to apply a selector to the feedback.
    def _feedback_with_selector(self, feedback):
        # Apply the feedback selector to the context path and output, and return the result.
        return (
            feedback
            .on(self.context_path.collect())  # Select feedback based on the collected context path.
            .on_output()  # Select feedback based on the output.
        )