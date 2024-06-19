# llm_test_framework
LLM testing framework


```python
# Import necessary classes and modules from the llm_test_framework
from llm_test_framework.src.tests.lib import Maliciousness, Criminality
from llm_test_framework.src.targets import LangChainTarget
from llm_test_framework.src.app import App
from llm_test_framework.src.tests import TestSet
from llm_test_framework.src.targets import Target

# Import the rag_chain from the LLMTesting.lang_chain.lang_chain module
from LLMTesting.lang_chain.lang_chain import rag_chain

# Import the List type from the typing module
from typing import List

# Set up the test application with a specific name and context
app = App(app_name="llm-powered-autonomous-agents")
context = app.set_context(rag_chain)
app.reset_database()

# Define the target of our tests
target: Target = LangChainTarget(rag_chain)

# Define the tests to be executed, which are instances of TestSet
tests: List[TestSet] = [
    Maliciousness, 
    Criminality
]

# Execute each test on the target and store the results
test_results = [test.evaluate(target, app_id=f"{app.app_name}-{test.name}") for test in tests]

# Run the test dashboard to evaluate results
app.run_dashboard() 
```
