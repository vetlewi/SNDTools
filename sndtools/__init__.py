from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("sndtools")
except PackageNotFoundError:
    __version__ = "unknown.dev"

