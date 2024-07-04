### Comparing LLM Applications
This example demonstrates how to evaluate multiple applications (or versions of an application) side by side.

```python
from llm_test_framework.kjr_llm.app import App
from llm_test_framework.kjr_llm.targets import LangChainTarget
from llm_test_framework.kjr_llm.tests.lib import Criminality

from your_app_v1 import your_chain_v1
from your_app_v2 import your_chain_v2

app = App(your_chain, 
            app_name="side-by-side-example",
            reset_database=True)

Criminality.provider = "openai"

targets = [
    LangChainTarget(your_app_v1, name="v1"),
    LangChainTarget(your_app_v2, name="v2")
]

results = []
for target in targets:
    result = Criminality.evaluate(target, app_name=f"criminality-{target.name}")
    results.append(result)

app.run_dashboard()
```