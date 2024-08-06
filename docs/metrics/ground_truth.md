[<- back to metrics](./metrics.md)
# Ground Truth
The ground truth metric is used to assess the similarity of a response against
a pre-defined, verified response. Ground truth evaluations can be useful early
in the development process when assessing performance on a limited number of
integral queries.

### Providers
* openai
* llama3

### Signature
```python
class GroundTruthAgreement(golden_set: List[dict[str, str]] | PromptSet, agreement_measure = "agreement_measure")
```
* golden_set: *List[dict[str, str]] | PromptSet* - A list of JSON objects
containing prompts and expected responses. Alternatively a *PromptSet* loaded
from the same data can be provided.
* agreement_measure: *str* - The name of the agreement measure used to assess
similarity with the ground truth data.
### Agreement Measures
Several agreement measures can be used to assess similarity with the ground
truth data. For more details see the [Trulens documentation](https://www.trulens.org/trulens_eval/evaluation/feedback_implementations/stock/#ground-truth-agreement).

* [agreement_measure](https://www.trulens.org/trulens_eval/evaluation/feedback_implementations/stock/#trulens_eval.feedback.groundtruth.GroundTruthAgreement.agreement_measure) (note: this measure uses an OpenAI GPT model)
* [bert_score](https://www.trulens.org/trulens_eval/evaluation/feedback_implementations/stock/#trulens_eval.feedback.groundtruth.GroundTruthAgreement.bert_score)
* [bleu](https://www.trulens.org/trulens_eval/evaluation/feedback_implementations/stock/#trulens_eval.feedback.groundtruth.GroundTruthAgreement.bleu)
* [mae](https://www.trulens.org/trulens_eval/evaluation/feedback_implementations/stock/#trulens_eval.feedback.groundtruth.GroundTruthAgreement.mae)
* [rouge](https://www.trulens.org/trulens_eval/evaluation/feedback_implementations/stock/#trulens_eval.feedback.groundtruth.GroundTruthAgreement.rouge)

### Prompts
The expected format for prompts can be seen below.
```JSON
// golden_set.json
[
    {
        "input": "A question to be asked of your application",
        "expected_output": "The expected response from your application"
    }
]
```
Prompts can be provided directly to the metric as Python objects
```python
golden_set = [
    {
        "input": "A question to be asked of your application",
        "expected_output": "The expected response from your application"
    }
]
gta = GroundTruthAgreement(golden_set)
```
Or can be loaded directly from a file
```python
gta = GroundTruthAgreement.from_prompts_file_json("golden_set.json")
```

### Example
```python
from kjr_llm.metrics import GroundTruthAgreement
from kjr_llm.prompts import PromptSet

golden_set = PromptSet.from_json_file("golden_set.json")
gta = GroundTruthAgreement(golden_set, agreement_measure = "mae")
```
