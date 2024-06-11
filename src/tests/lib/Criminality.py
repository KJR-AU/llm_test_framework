from ..TestSet import TestSet
from ...prompts.lib import CriminalityPromptSet
from ...metrics.llama3 import Criminality

Criminality = TestSet(CriminalityPromptSet, [Criminality], name="Criminality")