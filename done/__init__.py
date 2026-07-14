"""
Runtime will load the XBlock class from here.
"""

from importlib.metadata import version

from .done import DoneXBlock

__version__ = version("done-xblock")
