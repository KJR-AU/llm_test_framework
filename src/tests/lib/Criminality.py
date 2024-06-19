"""
This module defines a `TestSet` for evaluating criminality using a combination of prompts and metrics.

The module imports the following components:
1. `TestSet`: A class or function from the `TestSet` module located in the parent package. This is likely used to create a test set for evaluating some aspect of criminality.
2. `CriminalityPromptSet`: A class or module from the `prompts.lib` package located two levels up from the current package. This provides the prompts necessary for evaluating criminality.
3. `Criminality`: A class or module from the `metrics.llama3` package located two levels up from the current package. This provides the metrics necessary for evaluating criminality.

The module then creates an instance of `TestSet` named `Criminality`. This instance is configured with:
- `CriminalityPromptSet`: The prompts used for evaluation.
- `[Criminality]`: A list containing the `Criminality` metric, which is used to measure the performance of the test set.
- `name="Criminality"`: A name for the test set, which is set to "Criminality".

This `Criminality` test set can be used to evaluate models or systems based on their ability to handle criminality-related tasks using the specified prompts and metrics.
"""

from ..TestSet import TestSet
from ...prompts.lib import CriminalityPromptSet
from ...metrics.llama3 import Criminality

Criminality = TestSet(CriminalityPromptSet, [Criminality], name="Criminality")