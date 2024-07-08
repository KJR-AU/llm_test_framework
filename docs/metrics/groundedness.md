[<- back to metrics](./metrics.md)
# Groundedness
The groundedness metric is used to assess the groundedness of the application
response in the context documents. This is similar to monitoring for model
hallucination. Chain of thought reasoning is always included.

### Providers
* openai
* llama3

### Signature
```python
class Groundedness(context_path)
```
* context_path: *Lens* - Trulens Selector path to an array of context documents 
returned by the context-retrieval tool.

### Example
```python
from kjr_llm.metrics import Groundedness
from trulens_eval import Select

context_path = Select.RecordCalls.retrieve.rets 
groundedness = Groundedness(query_path) \
                .openai
```