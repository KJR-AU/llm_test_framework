# Import the base Metric class from the parent package.
from ..Metric import Metric

# Import the numpy library for numerical operations.
import numpy as np

# Define a class named ContextRelevance that inherits from the Metric class.
class ContextRelevance(Metric):
    
    # Constructor method to initialize the ContextRelevance object.
    def __init__(self, query_path, context_path):
        # Store the paths to the query and context data.
        self.query_path = query_path
        self.context_path = context_path
        # Call the constructor of the parent Metric class with the name "Context Relevance".
        super().__init__(name="Context Relevance")

    # Property method to return the name of the feedback metric.
    @property
    def feedback_name(self):
        return "context_relevance_with_cot_reasons"

    # Method to apply a selector to the feedback.
    def _feedback_with_selector(self, feedback):
        # Apply the feedback selector to the query and context paths and aggregate the results using the mean function.
        return (
            feedback
            .on(self.query_path)  # Select feedback based on the query path.
            .on(self.context_path)  # Select feedback based on the context path.
            .aggregate(np.mean)  # Aggregate the selected feedback using the mean function.
        )