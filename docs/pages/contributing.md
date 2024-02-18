# Contributing

Firstly, it's important to note that the `main` branch is the deployed branch, whereas the `staging` branch is where 
development takes place. Consequently, only pull requests addressing critical bugs will be accepted against `main`.

## Add a sequence

We suggest to follow the following steps:
1. (Optional) Open an issue to discuss and outline the sequence you intend to implement, and/or review the project roadmap.

2. Think about the best way to represent your sequence.

3. In the `sequentium.sequence.sequences` module, implement the sequence in the script corresponding to the category to which your sequence belongs.

4. Implement tests for your sequence in the `sequentium.tests.tests_sequence` module. The test structure should resemble the following:
    ```python
    class TestSEQUENCENAME(SequenceTestSuite):
        sequence = SEQUENCENAME()
        sequence_name = 'sequence name'
        ground_truth = [
            ...
        ]
    ```
    where `SEQUENCENAME` is the name of your sequence.

5. Once that the tests and the listing with Ruff are passing, open a pull request against the `staging` branch.

6. Congratulations!

## Testing
Before opening a pull request, ensure that the unit tests pass locally. You can run the tests on your machine simply 
by typing the following two commands in a terminal from the working directory.
```shell
pip install pytest
python -m pytest tests
```
## Linting
Linting and code style are provided by Ruff. You can run the linting and automatically format your code using the 
following two commands in a terminal from the working directory.
```shell
pip install ruff
python -m ruff check . --fix
```