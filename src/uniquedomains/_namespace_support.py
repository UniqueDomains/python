"""Small conversions the typed methods share (``_namespaces.py`` is generated)."""

from __future__ import annotations

import importlib
from collections.abc import Mapping, Sequence
from typing import Any

from ._generated.types import UNSET, Unset


def _join(value: Any) -> Any:
    """``fields`` and ``include`` as a list or a comma string; an empty one sends nothing, never an empty ``fields=``."""
    if isinstance(value, Unset) or value is None:
        return value
    joined = (
        value
        if isinstance(value, str)
        else ",".join(str(entry) for entry in value)
        if isinstance(value, Sequence)
        else str(value)
    )
    return joined if joined.strip() else UNSET


def _body(value: Any, module_name: str, class_name: str) -> Any:
    """A body as the generated model, or as a plain mapping turned into it."""
    model = getattr(importlib.import_module(f"uniquedomains._generated.models.{module_name}"), class_name)
    if isinstance(value, model):
        return value
    if isinstance(value, Mapping):
        return model.from_dict(dict(value))
    raise TypeError(f"body takes a {class_name} or a mapping, not {type(value).__name__}.")
