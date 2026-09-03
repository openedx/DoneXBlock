"""
Runtime will load the XBlock class from here.
"""

from importlib.metadata import PackageNotFoundError, version

from .done import DoneXBlock

try:
    __version__ = version("done-xblock")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"
