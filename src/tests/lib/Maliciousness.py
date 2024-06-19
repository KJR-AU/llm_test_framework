"""
This module defines a `TestSet` for evaluating maliciousness using a combination of prompts and metrics.

The module imports the following components:
1. `TestSet`: A class or function from the `TestSet` module located in the parent package. This is likely used to create a test set for evaluating some aspect of maliciousness.
2. `MaliciousnessPromptSet`: A class or module from the `prompts.lib` package located two levels up from the current package. This provides the prompts necessary for evaluating maliciousness.
3. `Maliciousness`: A class or module from the `metrics.llama3` package located two levels up from the current package. This provides the metrics necessary for evaluating maliciousness.

The module then creates an instance of `TestSet` named `Maliciousness`. This instance is configured with:
- `MaliciousnessPromptSet`: The prompts used for evaluation.
- `[Maliciousness]`: A list containing the `Maliciousness` metric, which is used to measure the performance of the test set.
- `name="Maliciousness"`: A name for the test set, which is set to "Maliciousness".

This `Maliciousness` test set can be used to evaluate models or systems based on their ability to handle maliciousness-related tasks using the specified prompts and metrics.
"""

from ..TestSet import TestSet
from ...prompts.lib import MaliciousnessPromptSet
from ...metrics.llama3 import Maliciousness

Maliciousness = TestSet(MaliciousnessPromptSet, [Maliciousness], name="Maliciousness")