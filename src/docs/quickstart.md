# Quickstart
This guide helps you to get started evaluating your RAG application.

## Table of Contents
- [App](#app)
- [Target](#target)
- [Feedback](#feedback)
- [TestSet](#testset)
- [Dataset](#dataset)
- [Result Review](#result-review)
- [Other](#other)

# App
This framework evaluates a RAG application using an evaluation framework, TruLens.
To install TruLens dependency:
```bash
pip install trulens-eval
```
## How to set RAG application
To define the RAG application,
```python
from llm_test_framework.src.app import App
from LLMTesting.lang_chain.lang_chain import rag_chain # import your rag application here this is example.

# Set up the test application
app = App(app_name="llm-powered-autonomous-agents") 
context = app.set_context(rag_chain)
```
please set the app_name to your preference and import your rag_application.

To reset the database - clean previous evaluation records:
```python
# Reset the application's database to ensure a clean state for testing
app.reset_database()
```

# Target
[Target](.\..\targets\Target.py) class is used to instantiate the RAG application that is targeted to evaluate. Various llm framework is supported and they can be evaluated by setting the correct target which the RAG application to evaluate uses.

## Supported LLM Framework:

| LLM Framework | Url |
|---------------|-----|
| **LangChain** | https://python.langchain.com/v0.2/docs/introduction/ |
| **LlamaIndex** | https://docs.llamaindex.ai/en/stable/ |

## How to set Target

Set target:
```python
# LangChainTarget
from llm_test_framework.src.targets import LangChainTarget
target: Target = LangChainTarget(rag_chain)
```
or 
```python
# LlamaIndexTarget
from llm_test_framework.src.targets import LlamaIndexTarget
target: Target = LlamaIndexTarget(rag_chain)
```

# Feedback

## Feedback Metric

List of overall feedback metrics available.
**Some feedback metric may only be supported by a particular feedback provider.** For more details please read [TruLens LLMProvider](https://www.trulens.org/trulens_eval/api/provider/llmprovider/)

| Feedback Metric | Description |
|-----------------|-------------|
| **ContextRelevance** | Relevancy of the context to the question |
| **Relevance** | Relevancy of the RAG application response to the question |
| **Maliciousness** | Check the maliciousness of the RAG Application response |
| **Insensitivity** | Check the insensitivity of the RAG Application response |
| **Criminality** | Check the criminality of the RAG Application response |
| **Controversiality** | Check the controversiality of the RAG Application response |
| **Coherence** | Check the coherence of the RAG Application response |
| **CoherenceWithCotReasons** | Check the coherence of the RAG Application response with reasoning provided |
| **Violence** | Check the violence of the RAG Application response |
| **Harassment** | Check the harassment of the RAG Application response |
| **HarassmentThreatening** | Check the harassment and threatening of the RAG Application response |
| **Hate** | Check the hate of the RAG Application response |
| **SelfHarm** | Check the self harm of the RAG Application response |
| **ViolenceGraphic** | Check the violence graphic of the RAG Application response |

## Feedback Provider
Feedback provider is an LLM model that is used to evaluate the target RAG application. For instance, llama3 feedback provider can be used to evaluate an openai RAG application.

### Supported LLM Framework:
Multiple feedback providers is supported in this framework. 

| Feedback Providers | Url | python file |
|--------------------|-----|-------------|
| **openai** | https://www.trulens.org/trulens_eval/api/provider/openai/, https://platform.openai.com/docs/overview | [openai.py](./../metrics/openai/metrics.py) |
| **llama3** | https://www.trulens.org/trulens_eval/api/provider/litellm/, https://ollama.com/blog/llama3 | [llama3.py](./../metrics/llama3/metrics.py) |

## How to set Feedback Metric
By default, feedback provider is set to **llama3** for existing TestSet in tests directory,
To set a TestSet with a specific feedback provider:

Import metric from the preferred feedback provider
```python
from ...metrics.openai import Criminality
```
And include the imported module when [defining a TestSet](#how-to-define-testset).
```python
Criminality = TestSet(CriminalityPromptSet, [Criminality], name="Criminality")
```

# TestSet
[TestSet](../tests/TestSet.py) is a [list of prompts](#promptset) (PromptSet) combined with relevant feedback metric. It manage and evaluate a list of prompts against specific targets, and records the interactiona and feedback. It ensures that only recognized target types are used and provides flexibility in managing the evaluation process, including the option to reset the database and generate unique identifiers for different evaluations.

### PromptSet
[PromptSet](../prompts/PromptSet.py) is a list of [Prompt](#Prompt). PromptSet class has a static method `from_json_file` to read a local JSON file.

### Prompt
[Prompt](../prompts/Prompt.py) is a class for storing the input and expected output.


### Available TestSet:

| TestSet | Description | python file |
|---------|-------------|-------------|
| **Criminality** | TestSet that evaluates the criminality of the RAG application's responses using llama3 and has list of Criminality related Prompt.  | [Criminiality.py](./../tests/lib/Criminality.py) |
| **Maliciousness** | TestSet that evaluates the maliciousness of the RAG application's responses using llama3 and has list of Maliciousness related Prompt. | [Maliciousness.py](./../tests/lib/Maliciousness.py) |


### How to define Testset:
```python
from ..TestSet import TestSet # import TestSet class
from ...metrics.openai import Criminality # import your preferred feedback provider's feedback metric for evaluation
from ...prompts.lib import CriminalityPromptSet # import promptset

# Define test set
Criminality = TestSet(CriminalityPromptSet, [Criminality], name="Criminality")
```

### How to run evaluate:
```python
Criminality.evaluate(target, app_id=f"{app.app_name}-{Criminality.name}")
```
You can also reset database by setting reset_database to True, by default it is False.
```python
test_result = Criminality.evaluate(target, app_id=f"{app.app_name}-{Criminality.name}", reset_database=True)
```

## Dataset
Prompt Data needs to be prepared as a JSON file and it needs to be in the local machine, for example "llm_test_framework\src\prompts\lib\data\ambiguousness.json". 
Each object must have field name, "input" and "expected output". 
- "input": An user message to the RAG application and it needs to be a string value.
- "output": An expected response from the RAG application, which can be null. This value will be used to compare with the actual output/response of the RAG application.

### Json file data format:
```JSON
[
    {
        "input": "Input or a question to the RAG application",
        "expected_output": "Expected output/response of the RAG application to the input"
    },
    {
         "input": "Input or a question to the RAG application2",
        "expected_output": null
    }
]
```

More Prompt examples can be found from [Test Dataset](https://kjra-my.sharepoint.com/:x:/g/personal/aletta_cawood_kjr_com_au/ET5C9M6YYPpNr6iAL7MuvfgBDma8omCJaq1Hhcczt-Kzlg?e=S2JXoX) created by Aletta Cawood and Marielle Selmo.

## Custom test

To run a test prompts that is not existing in this repository, prepare a JSON file that follows the [data format](#json-file-data-format) and save it in a local directory for example, the data folder located in prompts/lib folder where other test prompt files are located.

Say we have a test prompts related to Violence.
Prepare a JSON file and save it in llm_test_framework/src/prompts/lib/data/violence.json.

Set the RAG application to evaluate
```python
from LLMTesting.lang_chain.lang_chain import rag_chain
from llm_test_framework.src.app import App

# Set up the test application
app = App(app_name="llm-powered-autonomous-agents")
context = app.set_context(rag_chain)
app.reset_database()
```
Set Target:
```python
# Define the target of our tests
from llm_test_framework.src.targets import LangChainTarget
from llm_test_framework.src.targets import Target

target: Target = LangChainTarget(rag_chain)
```
Define PromptSet
```python
from llm_test_framework.src.metrics.openai import Violence
from llm_test_framework.src.prompts.PromptSet import PromptSet 
import os  # Import the os module for file path operations.

# Get the directory of the current file.
current_file_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the JSON file containing the prompts related to hate.
relative_path = 'llm_test_framework/src/prompts/lib/data/violence.json'

# Construct the full path to the JSON file by joining the current file directory and the relative path.
full_path = os.path.join(current_file_dir, relative_path)

# Create an instance of PromptSet by loading prompts from the specified JSON file.
ViolencePromptSet = PromptSet.from_json_file(str(full_path))
```

Define TestSet
```python
from llm_test_framework.src.tests import TestSet
ViolenceTestSet = TestSet(ViolencePromptSet, [Violence], name="Violence")
```

Evaluate the RAG application on Violency and start TruLens dashboard.
```python
# Evaluate the RAG application and record the evaluation
test_results = ViolenceTestSet.evaluate(target, app_id=f"{app.app_name}-{test.name}")

# Run the test dashboard to evaluate results
app.run_dashboard()
```

# Result Review
TruLens framework is used to evaluate the RAG application. TruLens provides a TruLens dashboard to display the result of the evaluation.


To start TruLens dashboard in the new python file that 
```python
app.run_dashboard()
```
Then click on the url to open the TruLens dashboard in a web browser.
[TruLens documentation](https://www.trulens.org/trulens_eval/getting_started/)


To record evaluation result
```python
# The evaluate method of each test is called with the target and a unique app ID
test_result = testset.evaluate(target, app_id=f"{app.app_name}-{testset.name}")
```
*You may change app_id to our preference.

Each TestSet will record the evaluation result with the provided app_id of the TestSet will be displayed in the TruLens dashboard.

![alt text](./img/trulens_dashboard.png)


# Other
For more advanced usage please read [advanced.md](./advanced.md) file.

For example:
- Test Prompt generation

