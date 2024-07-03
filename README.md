# kjr_llm
KJR's internal LLM-testing framework.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Quickstart](#quickstart)

## About

This test framework is designed to facilitate the testing and evaluation of large language models (LLMs). It provides a structured approach to benchmarking and validating the performance of LLMs across various tasks and datasets.

## Features

- **Comprehensive Benchmarking**: Evaluate LLMs on a wide range of tasks.
- **Customizable Test Suites**: Easily create and run custom test suites.
- **Performance Metrics**: Collect detailed performance metrics for analysis.
- **Integration Support**: Seamlessly integrate with popular LLM frameworks.

## Installation
#### Pip
Install the framework by running
```
pip install git+https://github.com/KJR-AU/llm_test_framework
```
then import it with
```python 
import kjr_llm
```

## Quickstart

```python
from kjr_llm.app import App
from kjr_llm.targets import LangChainTarget
from kjr_llm.tests.lib import Criminality

from your_app import your_chain

# Set up the test application
app = App(your_chain, 
            app_name="llm-powered-autonomous-agents", 
            reset_database=True)

# Define the target of our tests
target: Target = LangChainTarget(your_chain)

# Define and execute the tests
Criminality.evaluate(target, app_id=f"{app.app_name}-{test.name}", provider="openai")

# Run the test dashboard to evaluate results
app.run_dashboard() 
```
