# llm_test_framework
LLM testing framework


```python
from llm_test_framework.src.tests.lib import Maliciousness, Criminality
from llm_test_framework.src.targets import LangChainTarget
from llm_test_framework.src.app import App
from llm_test_framework.src.tests import TestSet
from llm_test_framework.src.targets import Target
from LLMTesting.lang_chain.lang_chain import rag_chain
from typing import List

# Set up the test application
app = App(app_name="llm-powered-autonomous-agents")
context = app.set_context(rag_chain)
app.reset_database()

# Define the target of our tests
target: Target = LangChainTarget(rag_chain)

# Define and execute the tests
tests: List[TestSet] = [
    Maliciousness, 
    Criminality
]
test_results = [test.evaluate(target, app_id=f"{app.app_name}-{test.name}") for test in tests]

# Run the test dashboard to evaluate results
app.run_dashboard() 
```
