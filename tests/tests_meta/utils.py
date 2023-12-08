import ast
import re
from pathlib import Path
from typing import Union, List, Set


def get_class_names_from_script(script_path: Union[str, Path], pattern: Union[str, None] = None) -> List[str]:
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


def get_sequence_class_names_from_markdown() -> Set:
    """ The method returns all the class names contained in the markd down file SEQUENCES_LIST.md """
    with open('SEQUENCES_LIST.md', 'r') as file:
        content = file.read()

        # Define the pattern for matching rows in the table
        row_pattern = r'\| (.*?) \| (.*?) \| (.*?) \| (.*?) \|'
        row_matches = re.findall(row_pattern, content)

        sequence_class_names = set()
        for row in row_matches[1:]:
            sequence_class_names_in_row = row[2].split(',')
            sequence_class_names_in_row = {name.strip(' `') for name in sequence_class_names_in_row}
            sequence_class_names = sequence_class_names.union(sequence_class_names_in_row)
        return sequence_class_names


def get_sequences_defined_in_script(script_path: str) -> Set:
    """ The method returns all sequence defined in a given script"""
    sequence_defined_in_script = set()
    with open(script_path, 'r') as f:
        tree = ast.parse(f.read())
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                sequence_defined_in_script.add(node.name)
            elif isinstance(node, ast.Assign):
                sequence_defined_in_script.add(node.targets[0].id)
    return sequence_defined_in_script
