"""Small conversions the typed methods share (``_namespaces.py`` is generated)."""

from __future__ import annotations

import importlib
from collections.abc import Mapping, Sequence
from typing import Any

from ._generated.types import UNSET, Unset


def join_list(value: str | Sequence[str] | None) -> str | None:
    """``fields`` and ``include`` as a list or a comma string; an empty one is None, never an empty ``fields=``."""
    if value is None:
        return None
    joined = value if isinstance(value, str) else ",".join(str(entry) for entry in value)
    return joined if joined.strip() else None


def _join(value: Any) -> Any:
    """``join_list`` for a typed method, where a missing value is ``UNSET``."""
    if isinstance(value, Unset) or value is None:
        return UNSET
    joined = join_list(value)
    return UNSET if joined is None else joined


def _body(value: Any, module_name: str, class_name: str) -> Any:
    """A body as the generated model, or as a plain mapping turned into it."""
    model = getattr(importlib.import_module(f"uniquedomains._generated.models.{module_name}"), class_name)
    if isinstance(value, model):
        return value
    if isinstance(value, Mapping):
        return model.from_dict(dict(value))
    raise TypeError(f"body takes a {class_name} or a mapping, not {type(value).__name__}.")
