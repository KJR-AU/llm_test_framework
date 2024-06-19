"""
This module defines the public interface for a package that deals with aspects of maliciousness and criminality.

The module imports two main components:
1. `Maliciousness`: A class or module that deals with the concept of maliciousness.
2. `Criminality`: A class or module that deals with the concept of criminality.

The `__all__` attribute is used to specify the public interface of this module. It lists the names of the objects that should be imported when `from module import *` is used.

Currently, the public interface includes:
- `MaliciousnessTestSet`: This is expected to be a class, function, or module that is related to testing or evaluating maliciousness.

Note: The actual definition of `MaliciousnessTestSet` is not provided in this snippet. Ensure that it is defined elsewhere in the package.
"""

from .Maliciousness import Maliciousness
from .Criminality import Criminality

__all__ = [
    "MaliciousnessTestSet"
]