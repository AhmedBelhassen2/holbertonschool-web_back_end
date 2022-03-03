#!/usr/bin/env python3
"""an int OR float v as arguments and returns a tuple."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """should be annotated as a float"""
    return (k, v**2)
