import ast
import re
from pathlib import Path
from typing import Union, List, Set, Tuple


def get_class_names_from_script(script_path: Union[str, Path], pattern: Union[str, None] = None) -> List[str]:
    """
    The method returns a list of all classes respecting the given pattern in the Python script provided at
    the location script_path.
    """
    script_text = Path(script_path).read_text()
    tree = ast.parse(script_text)
    class_names = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    if pattern:
        return filter_list_by_pattern(input_list=class_names, pattern=pattern)
    return class_names


def filter_list_by_pattern(input_list: List[str], pattern: str) -> List[str]:
    """ The method filter a list of string by a given pattern. """
    regex = re.compile(pattern)
    return [item for item in input_list if regex.match(item)]


def get_sequence_class_names_from_md() -> Set:
    """ The method returns all the class names contained in the markd down file SEQUENCES_LIST.md """
    sequence_list = Path('sequence/SEQUENCES_LIST.md').read_text()

    integer_sequence_class_names = extract_integer_sequences_class_names_from_md(content=sequence_list)
    generalised_sequence_class_names = extract_generalised_sequences_class_names_from_md(content=sequence_list)
    return integer_sequence_class_names.union(generalised_sequence_class_names)


def extract_integer_sequences_class_names_from_md(content: str) -> Set[str]:
    # extract the table integer sequences from the md
    integer_sequences_pattern = re.compile(r'## Integer sequences\n(.+?)\n## Generalised integer sequences', re.DOTALL)
    match = re.search(integer_sequences_pattern, content)
    generalised_sequences_table = match.group(1).strip()

    # extract the row of the table
    row_pattern = r'\| (.*?) \| (.*?) \| (.*?) \| (.*?) \|'
    row_matches = re.findall(row_pattern, generalised_sequences_table)
    del row_matches[0]  # delete first element as it is the header

    return extract_class_names_from_row(row_matches=row_matches, column_number=2)


def extract_generalised_sequences_class_names_from_md(content: str) -> Set[str]:
    # extract the table generalised sequences from the md
    generalised_sequences_pattern = re.compile(r'## Generalised integer sequences\n(.+?)(?=\n##|$)', re.DOTALL)
    match = re.search(generalised_sequences_pattern, content)
    generalised_sequences_table = match.group(1).strip()

    # extract the row of the table
    row_pattern = r'\| (.*?) \| (.*?) \| (.*?) \|'
    row_matches = re.findall(row_pattern, generalised_sequences_table)
    del row_matches[0]  # delete first element as it is the header

    return extract_class_names_from_row(row_matches=row_matches, column_number=1)


def extract_class_names_from_row(row_matches: List[Tuple], column_number: int) -> Set[str]:
    """
    Extracts sequence class names from a specific column in a list of row matches.

    Args:
        row_matches(List[Tuple]): A list of tuples representing rows, where each tuple contains data columns.
        column_number(int): The index of the column from which to extract sequence class names.
    Returns:
        Set[str]: A set containing unique sequence class names extracted from the specified column.
    """
    sequence_class_names = set()
    for row in row_matches:
        sequence_class_names_in_row = row[column_number].split(',')
        sequence_class_names_in_row = {name.strip(' `') for name in sequence_class_names_in_row}
        sequence_class_names = sequence_class_names.union(sequence_class_names_in_row)
    return sequence_class_names


def get_sequences_defined_in_script(script_path: Path) -> Set:
    """ The method returns all sequence defined in a given script"""
    sequence_defined_in_script = set()
    script_text = Path(script_path).read_text()
    tree = ast.parse(script_text)
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            sequence_defined_in_script.add(node.name)
        elif isinstance(node, ast.Assign):
            sequence_defined_in_script.add(node.targets[0].id)
    return sequence_defined_in_script
