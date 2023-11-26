import ast
import re
from pathlib import Path
from typing import Union, List

import pytest


def get_classes_from_script(script_path: Union[str, Path], pattern: Union[str, None] = None) -> List[str]:
    """
    The method returns a list of all classes respecting the given pattern in the Python script provided at
    the location script_path.
    """
    with open(script_path, 'r') as f:
        tree = ast.parse(f.read())
        class_names = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
        if pattern:
            return filter_list_by_pattern(input_list=class_names, pattern=pattern)
        else:
            return class_names


def filter_list_by_pattern(input_list: List[str], pattern: str) -> List[str]:
    """ The method filter a list of string by a given pattern. """
    regex = re.compile(pattern)
    return [item for item in input_list if regex.match(item)]

# TODO: extend to test scripts
@pytest.mark.parametrize(
    'script_path, pattern',
    [('sequence/sequences/integer/explicit.py', r'^A\d{6}$'),
     ('sequence/sequences/integer/explicit_generalised_sequences.py', None),
     ('sequence/sequences/integer/finite.py', r'^A\d{6}$'),
     ('sequence/sequences/integer/periodic.py', r'^A\d{6}$'),
     ('sequence/sequences/integer/property_defined.py', r'^A\d{6}$'),
     ('sequence/sequences/integer/property_defined_generalised_sequences.py', None),
     ('sequence/sequences/integer/recursive.py', r'^A\d{6}$'),
     ('sequence/sequences/integer/recursive_generalised_sequences.py', None)]
)
def test_order_script(script_path, pattern):
    """ The test checks if the script give at script_path is sorted alphabetically after filtered by pattern. """
    sequence_names = get_classes_from_script(script_path=script_path, pattern=pattern)
    assert sequence_names == sorted(sequence_names), f"Classes in '{script_path}' are not in alphabetical order."


@pytest.mark.parametrize(
    'script_path, pattern, test_script_path',
    [('sequence/sequences/integer/explicit.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_explicit.py'),
     ('sequence/sequences/integer/finite.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_finite.py'),
     ('sequence/sequences/integer/periodic.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_periodic.py'),
     ('sequence/sequences/integer/recursive.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_recursive.py')]
)
def test_tests_every_sequence(script_path, pattern, test_script_path):
    sequence_names = get_classes_from_script(script_path=script_path, pattern=pattern)
    test_names = get_classes_from_script(script_path=test_script_path)
    sequences_tested = [test.replace('Test', '') for test in test_names]

    sequences_not_tested = set(sequence_names).difference(set(sequences_tested))
    if sequences_not_tested:
        raise Exception(f'There are no tests for the following sequence/s: {sequences_not_tested}')
