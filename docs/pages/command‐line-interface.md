# Command-line interface

Sequentium provides a Command Line Interface (CLI) for convenient usage from your terminal.

```text
usage: Sequentium [-h] [-v] [--list {integer,generalised} [{integer,generalised} ...]] 
    [-a AT] [-l] [--start START] [--stop STOP] [--step STEP] [-c CONTAINS] [sequence]

Sequentium is a user-friendly package that implements various well-known sequences, 
providing a seamless and intuitive experience for the user

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

## Working with sequences

Using the command line interface you can retrieve information of a sequence in a fast way. 
### Retrieving sequence length

To obtain the length of a sequence, you can execute the following commands:
```text
sequence HeegnerNumebrs --length
>>> 9
```

or 
```text
sequence HeegnerNumbers -l
>>> 9
```

Consider what occurs when attempting to determine the length of an infinite sequence
```text
sequence FibonacciNumbers --length
>>> inf
```
### Single element retrieval in a sequence

To retrieve the element of a sequence at a given index, you can execute the following commands:

```text
sequence FibonacciNumbers --at 8
>>> 21
```
or 
```
sequence FibonacciNumbers -a 8
>>> 21
```

### Checking membership in a sequence

To checks if an element appears in a given sequence you can run the following commands:
```text
sequence FibonacciSequence --contains 7
>> False
sequence FibonacciNumbers --contains 21
>> True
```

or
```text
sequence FibonacciSequence -c 7
>> False
sequence FibonacciNumbers -c 21
>> True
```

### Printing a chunk of a sequence

You can print a chunk of a sequence using the command --list, as follows:
```text
sequence FibonacciSequence --start 2 --stop 8
>> [1, 2, 3, 5, 8, 13]
```
