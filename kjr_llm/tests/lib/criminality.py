from ...metrics import Criminality as CriminalityMetric
from ...prompts.lib import CriminalityPromptSet
from ..test_set import TestSet

# Define the feedback metrics for the Criminality test set
_feedbacks = [CriminalityMetric()]

# Create an instance of TestSet for evaluating criminality
Criminality = TestSet(CriminalityPromptSet, _feedbacks, name="Criminality")
