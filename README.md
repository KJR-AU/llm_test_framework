# llm_test_framework
LLM testing framework

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Prompts](#prompts)
- [Usage](#usage)
- [Contributing](#Contributing)

## About

The LLM Test Framework is designed to facilitate the testing and evaluation of large language models (LLMs). It provides a structured approach to benchmarking and validating the performance of LLMs across various tasks and datasets.

## Features

- **Comprehensive Benchmarking**: Evaluate LLMs on a wide range of tasks.
- **Customizable Test Suites**: Easily create and run custom test suites.
- **Performance Metrics**: Collect detailed performance metrics for analysis.
- **Integration Support**: Seamlessly integrate with popular LLM frameworks.

## Installation

To get started with the LLM Test Framework, follow these steps:

1. Open Git Bash or terminal.

2. Change the current working directory to the parent directory of the evaluationg RAG.

3. Clone the repository
```bash
# Clone the repository
git clone https://github.com/KJR-AU/llm_test_framework.git
```
4. If your interpretor does not have TruLens library, install TruLens:
https://www.trulens.org/trulens_eval/getting_started/

```bash
pip install trulens-eval
```

## Prompts

For instruction on how to use prompts, please read [prompts.md](prompts.md).

## Usage

1. Create a new python file that imports the necessary classes and modules, and run the evaluation like below:

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
app.reset_database() # reset any existing evaluation record

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

2. Replace the below code to import the RAG you wish to evaluate.

```python
# Import the rag_chain from the LLMTesting.lang_chain.lang_chain module
from LLMTesting.lang_chain.lang_chain import rag_chain
```
this line with your LLM model or rag chain.

3. Change the app_name
```python
app = App(app_name="change to your own")
```

4. Change rag_chain to the RAG you have imported at step 2.
```python
context = app.set_context(rag_chain)
```
and here, also change to correct llm framework target which is set as LangChainTarget in the example.
```python
target: Target = LangChainTarget(rag_chain)
```
For details on how to set target please read [quickstart.md](./src/docs/quickstart.md).
5. Change the evaluation metric per your requirement by chaging values in the list below
```python
# Define the tests to be executed, which are instances of TestSet
tests: List[TestSet] = [
    Maliciousness, 
    Criminality
]
```

6. Execute the evaluation in terminal/bash
```bash
# Change main.py to the [filename].py created at step 1.
python .\main.py
```

7. Wait for the dashboard to run.

8. open the url and the dashboard will open in a web browser.

9. Now the evaluation result and traces can be viewed.

For more details of usage please read [quickstart.md](./src/docs/quickstart.md).

## Contributing
Contributions to the LLM Test Framework are welcome! If you would like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix.

Make your changes and commit them with descriptive messages.

Push your changes to your fork.

Submit a pull request detailing your changes and their purpose.