from ..TestSet import TestSet
from ...prompts.lib import InsensitivityPromptSet
from ...metrics import Insensitivity as InsensitivityMetric

_feedbacks = [InsensitivityMetric()]

Insensitivity = TestSet(InsensitivityPromptSet, _feedbacks, name="Insensitivity")