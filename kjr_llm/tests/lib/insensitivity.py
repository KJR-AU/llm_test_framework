from ...metrics import Insensitivity as InsensitivityMetric
from ...prompts.lib import InsensitivityPromptSet
from ..test_set import TestSet

# Define the feedback metrics for the Insensitivity test set
_feedbacks = [InsensitivityMetric()]

# Create an instance of TestSet for evaluating insensitivity
Insensitivity = TestSet(InsensitivityPromptSet, _feedbacks, name="Insensitivity")
