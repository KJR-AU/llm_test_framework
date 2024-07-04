"""
This Python script serves as an initialization module for a package, defining the public interface of the package by specifying which prompt sets are exposed when the package is imported.

"""

# Importing specific prompt sets from their respective modules
from .Harassment import HarassmentPromptSet
from .Maliciousness import MaliciousnessPromptSet
from .Criminality import CriminalityPromptSet
from .Ambiguousness import AmbiguousnessPromptSet
from .Hate import HatePromptSet
from .SelfHarm import SelfHarmPromptSet
from .Violence import ViolencePromptSet
from .Insensitivity import InsensitivityPromptSet

# Defining a list of names to be exported when this module is imported
__all__ = [
    "HarassmentPromptSet",
    "MaliciousnessPromptSet",
    "CriminalityPromptSet",
    "AmbiguousnessPromptSet",
    "HatePromptSet",
    "SelfHarmPromptSet",
    "ViolencePromptSet",
    "InsensitivityPromptSet"
]