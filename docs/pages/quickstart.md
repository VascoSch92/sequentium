# Quick Start

To install Sequentium, use the following command:
```shell
pip install sequentium
```

You can control that sequentium was indeed installed by running the following command
```shell
sequence --version
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
