import argparse
import importlib
import sys
import re

from sequentium.cli.parser import CliParser
from sequentium.core.core import Sequence


def import_sequence_dynamically(sequence: str) -> Sequence:
    """Dynamically import a sequentium class by name."""
    try:
        sequence_module = importlib.import_module('sequentium')
        sequence_class = getattr(sequence_module, f'{sequence}')
    except ImportError:
        sys.exit(f'Sequence {sequence} is not implemented yet!')
    else:
        return sequence_class()


class CommandLineInterface:

    def execute(self) -> None:
        args = CliParser().parser()

        if args.list:
            self.print_list()
        else:
            self.execute_sequence_command(args=args)

    def print_list(self) -> None:
        with open('SEQUENCES_LIST.md', 'r') as file:
            content = file.read()

            # Define a regular expression to match the table content
            table_pattern = re.compile(r'\|.*\|', re.DOTALL)
            matches = table_pattern.findall(content)

            print('Integer Sequences'.center(200, '-'))
            print(matches[0])

        sys.exit(1)

    def execute_sequence_command(self, args: argparse.Namespace) -> None:
        if not args.sequence:
            sys.exit('no sequence given.. please see --help')
        else:
            sequence = import_sequence_dynamically(sequence=args.sequence)
            if args.at:
                self.execute_at_command(args, sequence)
            elif args.length:
                self.execute_length_command(sequence)
            elif args.contains:
                self.execute_contains_command(args, sequence)
            elif args.stop is not None:
                self.execute_as_list_command(args, sequence)
            else:
                print(sequence.__str__().capitalize())

    def execute_as_list_command(self, args, sequence):
        if args.start < 0:
            sys.exit(f'invalid int value for --start: {args.start}. Expected a non-negative integer!')
        if args.start > args.stop:
            sys.exit(f'invalid int value for --stop: {args.stop}. Expected a value bigger than --start')
        print(f'{sequence}: {sequence[args.start:args.stop:args.step]}')

    def execute_contains_command(self, args, sequence) -> None:
        sys.exit(args.contains in sequence)

    def execute_length_command(self, sequence) -> None:
        if sequence.is_finite:
            sys.exit(f'{sequence.__str__().capitalize()} has order {len(sequence)}')
        else:
            sys.exit(f'{sequence.__str__().capitalize()} is infinite')

    def execute_at_command(self, args, sequence) -> None:
        if args.at < 0:
            sys.exit(f'invalid int value for --start: {args.at}. Expected a non-negative integer!')
        sys.exit(f'{sequence.__str__().capitalize()} at index {args.at} is {sequence[args.at]}')
