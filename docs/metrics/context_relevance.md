[<- back to metrics](./metrics.md)
# Context Relevance
The context relevance metric is used to assess the relevance of the context to
the input. As such, it is generally used to evaluate performance and
optimisation of the vector store.

### Providers
* openai
* llama3

### Signature
```python
class ContextRelevance(query_path, context_path, cot_reasons: bool = True)
```
* query_path: *Lens* - Trulens Selector path to the query fed into the context-retrieval
tool.
* context_path: *Lens* - Trulens Selector path to the context documents returned by the
context-retrieval tool.
* cot_reasons: *bool* - If True include chain of thought reasoning in addition to
a float score.

### Example
```python
from kjr_llm.metrics import ContextRelevance
from trulens_eval import Select

query_path = Select.RecordCalls.retrieve.args.query
context_path = Select.RecordCalls.retrieve.rets
context_relevance = ContextRelevance(query_path, context_path, cot_reasons = False) \
                    .openai
```
