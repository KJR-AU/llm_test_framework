# llm_test_framework
LLM testing framework

## Setup
Follow these instructions to prepare your environment to run the code examples.
1. Pip install the framework with
```
pip install git+https://github.com/KJR-AU/llm_test_framework
```

2. Replace the the following lines to import your own RAG application.

```python
from LLMTesting.lang_chain.lang_chain import rag_chain
...
context = app.set_context(rag_chain)
...
target: Target = LangChainTarget(rag_chain)
```

## Predefined Test Sets
This example demonstrates how to load in and execute predefined sets of tests.
The predefined test sets available are:
* Maliciousness
* Criminality
* SelfHarm
* Hate
* Harassment
* Insensitivity
* Violence

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

## Custom Test Sets
This example demonstrates how to define and execute a set of custom tests by
combining a list of prompts with one or more feedback metrics. 

```python
from llm_test_framework.src.targets import LangChainTarget
from llm_test_framework.src.app import App
from llm_test_framework.src.tests import TestSet
from llm_test_framework.src.targets import Target
from llm_test_framework.src.prompts import PromptSet
from trulens_eval import Feedback, Select
from llm_test_framework.src.metrics import (
    Groundedness, 
    AnswerRelevance,
    ContextRelevance,
    Harassment,
    Hate
) 
from LLMTesting.lang_chain.lang_chain import rag_chain

# Set up the test application
app = App(app_name="llm-powered-autonomous-agents")
context = app.set_context(rag_chain)
app.reset_database()

# Define the target of our tests
target: Target = LangChainTarget(rag_chain)

# Load our custom inputs
prompts = PromptSet.from_json_file("inputs.json")

# Import and instantiate feedback metrics
query_path = Select.Record.app.first.steps__.context.first._get_relevant_documents.args.query
context_path = Select.Record.app.first.steps__.context.first.get_relevant_documents.rets[:].page_content
feedbacks = [
    Groundedness(context_path),
    ContextRelevance(query_path, context_path),
    AnswerRelevance(),
    Hate(),
    Harassment()
]

# Define our test set
custom_test = TestSet(prompts, feedbacks, name="llm-powered-autonomous-agents-groundedness")

# Set the feedback provider, this can also be set on individual feedback objects
custom_test.provider = "openai"

# Evaluate our test set
result = custom_test.evaluate(target)

app.run_dashboard() 
```

### prompts.json
The expected structure of the `prompts.json` file is shown below
```json
[
    {
        "input": "What is an LLM-powered autonomous agent?",
        "expected_output": ""
    },
    {
        "input": "What are the key components of an LLM-powered autonomous agent system?",
        "expected_output": ""
    }
]
```