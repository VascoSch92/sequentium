import re
import sys
import argparse
from pathlib import Path

sequence_list_filepath = Path("sequence/SEQUENCES_LIST.md")


def execute_command_list(args: argparse.Namespace) -> None:
    """Prints a list of implemented sequences based on the provided argument."""
    with sequence_list_filepath.open() as file:
        content = file.read()

        if args.list == ["integer"]:
            integer_table = extract_table(text=content, start_point="| OEIS    |")
            sys.exit("\n" + integer_table + "\n")

        if args.list == ["generalised"]:
            # extract the part of text containing the table generalised sequences from the md
            generalised_sequences_pattern = re.compile(r"## Generalised sequences\n(.+?)(?=\n##|$)", re.DOTALL)
            match = re.search(generalised_sequences_pattern, content)
            text = match.group(1).strip()

            generalised_table = extract_table(text=text, start_point="| Sequence Name")
            sys.exit("\n" + generalised_table + "\n")


def extract_table(text: str, start_point: str) -> str:
    """Extract the table from a given text."""
    start_index = text.find(start_point)
    end_index = text.find("\n\n", text.find(start_point))
    return text[start_index:end_index].strip()
