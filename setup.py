"""
This setup.py file is used to define and configure a Python package for distribution using setuptools.
"""

import re
from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent.resolve()

def load_long_description() -> str:
    """
    Reads and returns the content of the README.md file for the package's long description.
    """
    file_path = this_directory / "README.md"
    with file_path.open() as f:
        return f.read()

def load_version() -> str:
    """
    Extracts and returns the version number from the __version__.py file.
    Raises a ValueError if the version number is not found.
    """
    version_path = this_directory / "__version__.py"
    version_pattern = r"version\s*=\s*[\"'](.+)[\"']"
    with version_path.open() as f:
        match = re.search(version_pattern, f.read().strip())
        if match is None:
            raise ValueError(f"invalid version at {version_path}")
        return match.group(1)

def load_requirements() -> list[str]:
    """
    Reads and returns the list of dependencies from the requirements.txt file.
    """
    file_path: Path = this_directory / "requirements.txt"
    with file_path.open() as f:
        return [line.strip() for line in f]

"""
Configuration:
- name: The name of the package.
- version: The version of the package, extracted from __version__.py.
- description: A short description of the package.
- long_description: A detailed description of the package, read from README.md.
- long_description_content_type: Specifies the format of the long description (Markdown).
- url: The URL of the package's repository.
- author: The author of the package.
- author_email: The email address of the author.
- packages: A list of packages to include in the distribution.
- install_requires: A list of dependencies required by the package, read from requirements.txt.
"""
setup(
    name="kjr_llm",
    version=load_version(),
    description="KJR's LLM testing framework.",
    long_description=load_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/KJR-AU/llm_test_framework",
    author="Joe Burton",
    author_email="joe.burton@kjr.com.au",
    packages=[
        "kjr_llm",
        "kjr_llm.app",
        "kjr_llm.exceptions",
        "kjr_llm.metrics",
        "kjr_llm.metrics.lib",
        "kjr_llm.prompts",
        "kjr_llm.prompts.lib",
        "kjr_llm.prompts.lib.data",
        "kjr_llm.provider",
        "kjr_llm.targets",
        "kjr_llm.tests",
        "kjr_llm.tests.lib"
    ],
    install_requires=load_requirements(),
    package_data={
        "kjr_llm": ["prompts/lib/data/*"]
    },
    include_package_data=True
)
