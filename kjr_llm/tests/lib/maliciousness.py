from ...metrics import Maliciousness as MaliciousnessMetric
from ...prompts.lib import MaliciousnessPromptSet
from ..test_set import TestSet

# Define the feedback metrics for the Maliciousness test set
_feedbacks = [MaliciousnessMetric()]

# Create an instance of TestSet for evaluating maliciousness
Maliciousness = TestSet(MaliciousnessPromptSet, _feedbacks, name="Maliciousness")
