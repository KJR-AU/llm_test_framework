"""
This module defines the `Criminality` test set, which is a specific instance of the `TestSet` class used to evaluate the criminality of responses from a language model or a RAG application.
"""

from ..TestSet import TestSet
from ...prompts.lib import CriminalityPromptSet
from ...metrics import Criminality as CriminalityMetric

# Define the feedback metrics for the Criminality test set
_feedbacks = [CriminalityMetric()]

# Create an instance of TestSet for evaluating criminality
Criminality = TestSet(CriminalityPromptSet, _feedbacks, name="Criminality")