from ..TestSet import TestSet
from ...prompts.lib import CriminalityPromptSet
from ...metrics import Criminality as CriminalityMetric

_feedbacks = [CriminalityMetric()]

Criminality = TestSet(CriminalityPromptSet, _feedbacks, name="Criminality")