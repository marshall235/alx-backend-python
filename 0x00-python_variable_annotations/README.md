# Python Annotations

Python annotations provide a way to attach metadata to function arguments and return values. They help improve code readability and facilitate type checking, making it easier to understand how functions should be used.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Benefits](#benefits)
- [Limitations](#limitations)
- [Resources](#resources)

## Installation

Python annotations are part of the standard library, so no installation is required. Just ensure you are using Python 3.5 or higher.

## Usage

Annotations are specified by adding a colon (`:`) after the parameter name followed by the type hint. The return type is specified using the `->` syntax before the colon.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
Examples
Function with Annotations
python
def add(a: int, b: int) -> int:
    return a + b
Class with Annotations
python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
Benefits
Improved Readability: Makes it clear what types of arguments a function expects and what it returns.
Better Tooling Support: IDEs can provide better autocompletion and type checking.
Documentation: Annotations serve as a form of documentation for functions and classes.
Limitations
Annotations do not enforce type checking at runtime; they are purely for documentation and static analysis.
Annotations can become complex with generics and custom types, which may lead to confusion.
