"""
This Python script serves as an initialization module for a package, defining the public interface of the package by specifying which classes are exposed when the package is imported.
"""

# Import the classes and functions from the modules within this package 
from .TestSet import TestSet
from .evaluate import evaluate
from .GroundTruthTestSet import GroundTruthTestSet