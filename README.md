# llm_test_framework
LLM testing framework


```python
from llm_test_framework.src.prompts.PromptSet import PromptSet
from llm_test_framework.src.metrics.metrics import ContextRelevance, Relevance, Controversiality
from llm_test_framework.src.eval.evaluate import evaluate
from llm_test_framework.src.targets import LangChainTarget
from trulens_eval.app import App

# Import the RAG application we're testing
from LLMTesting.lang_chain.lang_chain import rag_chain

# Set the context for Trulens
context = App.select_context(rag_chain)

# Load a set of prompts
prompts = PromptSet.from_json_file("inputs.json")

# Define metrics/feedbacks to evaluate
feedbacks = [
    ContextRelevance(context),
    Relevance,
    Controversiality
]

# Create a target so the framework can invoke the application
target = LangChainTarget(rag_chain)

evaluate(target, prompts, feedbacks)
```
