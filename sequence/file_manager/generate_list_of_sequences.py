from pathlib import Path
import ast
import re
from typing import Tuple


def get_information_from_docstring(docstring: str) -> Tuple[str, str]:
    """
    The method take as input a docstring of the form
        'The sequence name (http://reference_link.xx)'
    and return the sequence name and the reference link.
    """
    match = docstring.split('(')
    sequence_name = match[0][:-1]
    reference_link = match[1][:-1]
    return sequence_name, reference_link


if __name__ == '__main__':
    sequence_module_path = Path('sequence/sequences/integer/explicit.py')

    with open(sequence_module_path, 'r') as f:
        tree = ast.parse(f.read())

        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                row = {}
                docstring = ast.get_docstring(node)
                name, link = get_information_from_docstring(docstring=docstring)


                row['sequence_name'] = node.name
                row['sequence_link'] = link

        print(tree)
