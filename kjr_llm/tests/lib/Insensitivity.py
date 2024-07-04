"""
This module defines the `Insensitivity` test set, which is a specific instance of the `TestSet` class used to evaluate the insensitivity of responses from a language model or a RAG application.
"""

from ..TestSet import TestSet
from ...prompts.lib import InsensitivityPromptSet
from ...metrics import Insensitivity as InsensitivityMetric

# Define the feedback metrics for the Insensitivity test set
_feedbacks = [InsensitivityMetric()]

# Create an instance of TestSet for evaluating insensitivity
Insensitivity = TestSet(InsensitivityPromptSet, _feedbacks, name="Insensitivity")