# Sequentium

![GitHub Release](https://img.shields.io/github/v/release/vascoSch92/sequentium)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sequentium)
[![Downloads](https://static.pepy.tech/badge/sequentium)](https://pepy.tech/project/sequentium)
![PyPI - License](https://img.shields.io/pypi/l/sequentium)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat)](https://www.firsttimersonly.com/)
![Static Badge](https://img.shields.io/badge/Linting%20-%20passing%20-%20green?style=flat&logo=ruff&label=Linted%20with%20Ruff&color=blue)
[![tests-suite](https://github.com/VascoSch92/sequentium/actions/workflows/tests-suite.yml/badge.svg?branch=main)](https://github.com/VascoSch92/sequentium/actions/workflows/tests-suite.yml)
---

Sequentium is a user-friendly package that implements various well-known sequences, 
providing a seamless and intuitive experience for the user.

- 💻 - installabe via pip
- 🐍 - compatible with Python 3.9, 3.10, 3.11 and 3.12
- 📈 - +50 sequences already coded. Click [here](https://github.com/VascoSch92/sequentium/blob/main/sequence/SEQUENCES_LIST.md) for a complete list
- 👍 - intuitive API
- ✅ - accurately tested


If you would like to contribute to the project, take a look to the section [_How to contribute_](https://github.com/VascoSch92/sequentium/wiki/5.-How-to-contribuite) in the wiki.

For some practical examples on how to use Sequentium, take al look [_here_](https://github.com/VascoSch92/sequentium/examples).

## Quick start

To install Sequentium, use the following command:
```shell
pip install sequentium
```
Suppose you want to work with the Fibonacci sequence. First, import it into your script:
```python
from sequence import FibonacciSequence

fibonacci = FibonacciSequence()
```
Now, FibonacciSequence is a class representing the Fibonacci sequence. It behaves similarly to a list. 
You can iterate through it:

```python
for x in fibonacci:
    print(x)
>> 0, 1, 1, 2, 3, 5, 8, 13, 21,...
```
Or you can access a specific term directly:
```python
fibonacci[8]
>> 21
```
Slicing is also supported:
```python
fibonacci[2:8]
>> [1, 2, 3, 5, 13]
```
Additionally, you can check if a number appears in the `Fibonacci sequence`:
```python
7 in fibonacci
>> False
21 in fibonacci
>> True
```
## Command Line Interface (CLI)
Sequentium provides a Command Line Interface (CLI) for convenient usage from your terminal.
```text
usage: Sequentium [-h] [-v] [--list {integer,generalised} [{integer,generalised} ...]] [-a AT] [-l] [--start START] [--stop STOP] [--step STEP] [-c CONTAINS] [sequence]

Sequentium is a user-friendly package that implements various well-known sequences, providing a seamless and intuitive experience for the user

positional arguments:
  sequence              Specify the name or identifier of the sequence to operate on.

options:
  -h, --help            show this help message and exit
  -v, --version         Display the version information.
  --list {integer,generalised} [{integer,generalised} ...]
                        List of implemented sequences.

sequence options:
  -a AT, --at AT        Retrieve the term at the specified index in the sequence.
  -l, --length          Display the length of the sequence.
  --start START         Define the starting point of the sequence.
  --stop STOP           End point of the sequence (excluded).
  --step STEP           Step size for iterating through the sequence.
  -c CONTAINS, --contains CONTAINS
                        Check if the sequence contains a specific value.

For help with a specific command, see: `sequence help <command>`

```
Here are some examples illustrating the usage of the Sequentium CLI:
- specify the index to get a specific element of `FibonacciSequence`
```text
sequence FibonacciSequence --at 8
>> 21
```
- define a range of `FibonacciSequence` using start and stop parameters

```text
sequence FibonacciSequence --start 2 --stop 8
>> [1, 2, 3, 5, 8, 13]
```
- check if a particular number belongs to the `FibonacciSequence`
```text
sequence FibonacciSequence --contains 7
>> False
sequence FibonacciNumbers --contains 21
>> True
```