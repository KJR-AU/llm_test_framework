from setuptools import setup, find_packages
import os
import re

this_directory = os.path.abspath(os.path.dirname(__file__))

def load_long_description():
    with open(os.path.join(this_directory, 'README.md')) as f:
        return f.read()

def load_version():
    version_path = os.path.join(
        this_directory, "__version__.py"
    )
    version_pattern = r"version\s*=\s*[\"'](.+)[\"']"
    with open(version_path) as f:
        match = re.search(version_pattern, f.read().strip())
        if match is None:
            raise ValueError(f'invalid version at {version_path}')
        return match.group(1)

def load_requirements():
    with open(os.path.join(this_directory, 'requirements.txt')) as f:
        return [line.strip() for line in f]

setup(
    name='kjr_llm',
    version=load_version(),
    description="KJR's LLM testing framework.",
    long_description=load_long_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/KJR-AU/llm_test_framework',
    author='Joe Burton',
    author_email='joe.burton@kjr.com.au',
    packages=[
        'kjr_llm', 
        'kjr_llm.app',
        'kjr_llm.metrics',
        'kjr_llm.prompts',
        'kjr_llm.targets',
        'kjr_llm.tests'
        
    ],
    install_requires=load_requirements(),
    # package_data={
    #     'datarwecdk': ['sagemaker/resources/*']
    # },
    # include_package_data=True
)