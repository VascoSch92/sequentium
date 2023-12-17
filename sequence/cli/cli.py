import argparse
import importlib
import re
import sys

from sequence.cli.parser import CliParser
from sequence.core.core import Sequence


def import_sequence_dynamically(sequence: str) -> Sequence:
    """Dynamically import a sequence class by name."""
    try:
        sequence_module = importlib.import_module('sequence')
        sequence_class = getattr(sequence_module, f'{sequence}')
    except ImportError:
        sys.exit(f'Sequence {sequence} is not implemented yet!')
    else:
        return sequence_class()


class CommandLineInterface:
    """A command-line interface for interacting with sequences."""

    def execute(self) -> None:
        """
        Parses command-line arguments using CliParser and executes either the print_list or execute_sequence_command
        based on the arguments.
        """
        args = CliParser().parser()

        if args.list:
            self.print_list(args=args)
        else:
            self.execute_sequence_command(args=args)

    def print_list(self, args: argparse.Namespace) -> None:
        """Prints a list of implemented sequences based on the provided argument."""
        with open('sequence/SEQUENCES_LIST.md', 'r') as file:
            content = file.read()

            if args.list == 'integer':
                # extract the table integer sequences from the md
                integer_sequences_pattern = re.compile(
                    r'## Integer sequences\n(.+?)\n## Generalised sequences',
                    re.DOTALL,
                )
                match = re.search(integer_sequences_pattern, content)
                generalised_sequences_table = match.group(1).strip()
                sys.exit(generalised_sequences_table)
            elif args.list == 'generalised':
                # extract the table generalised sequences from the md
                generalised_sequences_pattern = re.compile(r'## Generalised sequences\n(.+?)(?=\n##|$)', re.DOTALL)
                match = re.search(generalised_sequences_pattern, content)
                generalised_sequences_table = match.group(1).strip()
                sys.exit(generalised_sequences_table)
            else:
                # Define a regular expression to match the table content
                table_pattern = re.compile(r'\|.*\|', re.DOTALL)
                tables = table_pattern.findall(content)[0]
                sys.exit(tables)


    def execute_sequence_command(self, args: argparse.Namespace) -> None:
        """Executes a specific sequence command based on the provided arguments."""
        if not args.sequence:
            sys.exit('no sequence given.. please see --help')
        else:
            sequence = import_sequence_dynamically(sequence=args.sequence)
            if args.at:
                self.execute_at_command(args, sequence)
            elif args.length:
                self.execute_length_command(sequence)
            elif args.c:
                self.execute_contains_command(args, sequence)
            elif args.stop is not None:
                self.execute_as_list_command(args, sequence)
            else:
                print(sequence.__str__().capitalize())

    def execute_as_list_command(self, args, sequence):
        if args.start is None:
            args.start = 0
        if args.start < 0:
            sys.exit(f'invalid int value for --start: {args.start}. Expected a non-negative integer!')
        if args.start > args.stop:
            sys.exit(f'invalid int value for --stop: {args.stop}. Expected a value bigger than --start')
        print(f'{sequence}: {sequence[args.start:args.stop:args.step]}')

    def execute_contains_command(self, args, sequence) -> None:
        sys.exit(f'{args.c in sequence}')

    def execute_length_command(self, sequence) -> None:
        if sequence.is_finite:
            sys.exit(f'{sequence.__str__().capitalize()} has order {len(sequence)}')
        else:
            sys.exit(f'{sequence.__str__().capitalize()} is infinite')

    def execute_at_command(self, args, sequence) -> None:
        if args.at < 0:
            sys.exit(f'invalid int value for --start: {args.at}. Expected a non-negative integer!')
        sys.exit(f'{sequence.__str__().capitalize()} at index {args.at} is {sequence[args.at]}')


def execute_command_line_interface() -> None:
    CommandLineInterface().execute()
