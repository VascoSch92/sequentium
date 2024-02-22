from pathlib import Path

import pytest

from tests.tests_meta.utils import (
    get_class_names_from_script,
    get_sequences_defined_in_script,
    get_sequence_class_names_from_md,
)
from tests.tests_meta.test_cases import (
    TEST_CASES_ORDER_SCRIPT,
    TEST_CASES_TESTED_SEQUENCES,
)


@pytest.mark.parametrize(
    argnames=("script_path", "pattern"),
    argvalues=TEST_CASES_ORDER_SCRIPT,
    ids=[script for script, _ in TEST_CASES_ORDER_SCRIPT],
)
def test_order_script(script_path, pattern):
    """ The test checks if the script give at script_path is sorted alphabetically after filtered by pattern. """
    sequence_names = get_class_names_from_script(script_path=script_path, pattern=pattern)
    assert sequence_names == sorted(sequence_names), f"Classes in '{script_path}' are not in alphabetical order."


@pytest.mark.parametrize(
    argnames=("script_path", "pattern", "test_script_path"),
    argvalues=TEST_CASES_TESTED_SEQUENCES,
    ids=[script for script, _, _ in TEST_CASES_TESTED_SEQUENCES]
)
def test_every_sequence_is_tested(script_path, pattern, test_script_path):
    """ The test checks if for every sequence defined there is a test. """
    sequence_names = get_class_names_from_script(script_path=script_path, pattern=pattern)
    test_names = get_class_names_from_script(script_path=test_script_path)
    sequences_tested = [test.replace("Test", "") for test in test_names]

    sequences_not_tested = set(sequence_names).difference(set(sequences_tested))
    if sequences_not_tested:
        raise Exception(f"There are no tests for the following sequence/s: {sequences_not_tested}")


def test_markdown():
    """ The test checks if every defined sequence is also reported in the SEQUENCE_LIST.md, and vice-versa."""
    sequence_markdown = get_sequence_class_names_from_md()

    sequences_scripts_path = Path("sequence/sequences")
    sequence_script_paths = [file for file in sequences_scripts_path.rglob("*.py") if file.name != "__init__.py"]

    sequence_scripts = set().union(
        *[get_sequences_defined_in_script(script_path) for script_path in sequence_script_paths]
    )

    sequences_in_markdown_but_not_in_scripts = sequence_markdown.difference(sequence_scripts)
    error_msg = ""
    if sequences_in_markdown_but_not_in_scripts != set():
        error_msg += f"The following sequences are in the SEQUENCE_LIST.md, " \
                     f"but are not implemented: {', '.join(list(sequences_in_markdown_but_not_in_scripts))}\n"

    sequences_in_scripts_but_not_in_markdown = sequence_scripts.difference(sequence_markdown)
    if sequences_in_scripts_but_not_in_markdown != set():
        error_msg += f"The following sequences are implemented, " \
                     f"but are not in SEQUENCE_LIST.md: {', '.join(list(sequences_in_scripts_but_not_in_markdown))}"

    if error_msg:
        raise Exception(error_msg)
