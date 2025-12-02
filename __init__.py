"""
ECW API Package

A FastAPI-based API for ECW (Electronic Clinical Works) integration.
"""

__version__ = "1.0.0"
__author__ = "ECW Dev Team"

# Import key components for easier access
from .main import create_app, app
from .config import settings

# Define public API
__all__ = [
    "create_app",
    "app",
    "settings",
]
