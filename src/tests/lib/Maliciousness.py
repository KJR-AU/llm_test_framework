from ..TestSet import TestSet
from ...prompts.lib import MaliciousnessPromptSet
from ...metrics.llama3 import Maliciousness

Maliciousness = TestSet(MaliciousnessPromptSet, [Maliciousness], name="Maliciousness")