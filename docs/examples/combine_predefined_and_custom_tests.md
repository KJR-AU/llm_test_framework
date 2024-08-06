The following is an end to end example of how to evaluate a LLM-powered application by combining predefined and custom tests.

```python
from llm_test_framework.kjr_llm.app import App
from llm_test_framework.kjr_llm.targets import LangChainTarget
from llm_test_framework.kjr_llm.tests import TestSet
from llm_test_framework.kjr_llm.tests.lib import Criminality
from llm_test_framework.kjr_llm.prompts import PromptSet
from llm_test_framework.kjr_llm.metrics import (
    AnswerRelevance,
    Harassment,
    Hate
)
from your_app import your_chain

# Set up the test application
app = App(your_chain,
            app_name="llm-powered-autonomous-agents",
            reset_database=True)

# Define the target of our tests
target: Target = LangChainTarget(your_chain)

# Load our custom inputs
prompts = PromptSet.from_json_file("prompts.json")

# Import and instantiate feedback metrics
feedbacks = [
    AnswerRelevance(),
    Hate(),
    Harassment()
]

# Define our test set
custom_test = TestSet(prompts, feedbacks, name="test-app-groundedness")

tests = [
    custom_test,
    Criminality
]

# Evaluate our test set
provider = "openai"
for test in tests:
    result = test.evaluate(your_chain, provider=provider)

app.run_dashboard()
```
