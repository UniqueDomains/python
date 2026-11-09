"""The README's Python examples compile, and name only what the package exports."""

from __future__ import annotations

import ast
import re
from pathlib import Path

import uniquedomains

README = (Path(__file__).resolve().parent.parent / "README.md").read_text(encoding="utf-8")
BLOCKS = re.findall(r"```python\n(.*?)```", README, re.DOTALL)


def test_the_examples_compile() -> None:
    assert len(BLOCKS) >= 8
    for block in BLOCKS:
        compile(block, "README.md", "exec")


def test_the_examples_import_what_exists() -> None:
    for block in BLOCKS:
        for node in ast.walk(ast.parse(block)):
            if isinstance(node, ast.ImportFrom) and node.module == "uniquedomains":
                for alias in node.names:
                    assert hasattr(uniquedomains, alias.name), alias.name


def test_the_examples_call_methods_that_exist() -> None:
    client = uniquedomains.Client(api_key="")
    for namespace, method in re.findall(r"ud\.(\w+)\.(\w+)\(", README):
        assert callable(getattr(getattr(client, namespace), method)), f"{namespace}.{method}"
    for operation in re.findall(r'ud\.(?:request|iter_rows)\("(\w+)"', README):
        assert operation in uniquedomains.OPERATIONS
    client.close()
