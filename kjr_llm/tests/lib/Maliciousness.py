"""
This module defines the `Maliciousness` test set, which is a specific instance of the `TestSet` class used to evaluate the maliciousness of responses from a language model or a RAG application.
"""

from ..TestSet import TestSet
from ...prompts.lib import MaliciousnessPromptSet
from ...metrics import Maliciousness as MaliciousnessMetric

# Define the feedback metrics for the Maliciousness test set
_feedbacks = [MaliciousnessMetric()]

# Create an instance of TestSet for evaluating maliciousness
Maliciousness = TestSet(MaliciousnessPromptSet, _feedbacks, name="Maliciousness")