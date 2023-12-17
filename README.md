# Sequentium

Sequentium is a user-friendly package designed to effortlessly implement various well-known sequences, 
providing a seamless and intuitive experience for users.

For an exhaustive list of all sequences implemented in Sequentium, 
please click [here](https://github.com/VascoSch92/sequentium/blob/main/sequence/SEQUENCES_LIST.md).

## Quick start

To install Sequentium, use the following command:
```shell
pip install sequentium
```
Suppose you want to work with the Fibonacci sequence. First, import it into your script:
```python
from sequence import FibonacciSequence
```
Now, FibonacciSequence is a class representing the Fibonacci sequence. It behaves similarly to a list. 
You can iterate through it:

```python
for x in FibonacciSequence:
    print(x)
>> 0, 1, 1, 2, 3, 5, 8, 13, 21,...
```
Or you can access a specific term directly:
```python
FibonacciSequence[8]
>> 21
```
Slicing is also supported:
```python
FibonacciSequence[2:8]
>> [1, 2, 3, 5, 13]
```
Additionally, you can check if a number appears in the `Fibonacci sequence`:
```python
7 in FibonacciSequence
>> False
21 in FibonacciSequence
>> True
```
## Command Line Interface (CLI)
Sequentium provides a Command Line Interface (CLI) for convenient usage from your terminal.
```text
usage: Sequentium [-h] [-v] [--list {all,integer,generalised} [{all,integer,generalised} ...]] [-a AT] [-l] [--start START] [--stop STOP] [--step STEP] [-c C] [sequence]

Sequentium is a tool for working with mathematical sequences.

positional arguments:
  sequence              Specify the name or identifier of the sequence to operate on.

options:
  -h, --help            show this help message and exit
  -v, --version         Display the version information.
  --list {all,integer,generalised} [{all,integer,generalised} ...]
                        List of implemented sequences.

sequence options:
  -a AT, --at AT        Retrieve the term at the specified index in the sequence.
  -l, --length          Display the length of the sequence.
  --start START         Define the starting point of the sequence.
  --stop STOP           End point of the sequence (excluded).
  --step STEP           Step size for iterating through the sequence.
  -c C                  Check if the sequence contains a specific value.

For help with a specific command, see: `sequence help <command>`.
```
Here are some examples illustrating the usage of the Sequentium CLI:
- specify the index to get a specific element of `FibonacciSequence`
```text
sequence FibonacciSequence --at 8
>> Fibonacci numbers at index 8 is 21
```
- define a range of `FibonacciSequence` using start and stop parameters

```text
sequence FibonacciSequence --start 2 --stop 8
>> Fibonacci numbers: [1, 2, 3, 5, 8, 13]
```
- check if a particular number belongs to the `FibonacciSequence`
```text
sequence FibonacciSequence -c 7
>> False
sequence FibonacciNumbers -c 21
>> True
```