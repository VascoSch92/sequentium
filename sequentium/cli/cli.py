import argparse
import importlib
import sys
from sequentium.cli.parser import CliParser
from sequentium import __version__
from sequentium.core.core import Sequence
from sequentium.core.utils.exceptions import InfiniteSequenceError


def parser_command_line_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog='Sequentium',
        description='Sequentium is a tool for working with mathematical sequences.',
        epilog='For help with a specific command, see: `sequentium help <command>`.',
    )
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-v',
        '--version',
        action='version',
        version=f'{parser.prog}: v{__version__}',
        help='Display the version information.',
    )

    group.add_argument(
        '--list',
        action='store_true',
        help="List a list of implemented sequences.",
    )

    group.add_argument(
        "sequentium",
        type=str,
        nargs="?",
        help="Specify the name or identifier of the sequentium to operate on.",
    )
    parser.add_argument(
        '-a',
        '--at',
        type=int,
        default=None,
        help='Retrieve the term at the specified index in the sequentium.',
    )
    parser.add_argument(
        '-l',
        '--length',
        action='store_true',
        default=None,
        help='Display the length of the sequentium.',
    )
    parser.add_argument(
        "--start",
        type=int,
        default=None,
        help="Define the starting point of the sequentium.",
    )
    parser.add_argument(
        "--stop",
        type=int,
        default=None,
        help="End point of the sequentium (excluded).",
    )
    parser.add_argument(
        '--step',
        type=int,
        default=None,
        help='Step size for iterating through the sequentium.',
    )
    parser.add_argument(
        '-c',
        '--contains',
        type=int,
        default=None,
        help='Check if the sequentium contains a specific value.',
    )

    return parser.parse_args()


def import_sequence_dynamically(sequence: str) -> Sequence:
    """Dynamically import a sequentium class by name."""
    try:
        sequence_module = importlib.import_module('sequentium')
        sequence_class = getattr(sequence_module, f'{sequence}')
    except ImportError:
        sys.exit(f'Sequence {sequence} is not implemented yet!')
    else:
        return sequence_class()


def command_line_interface() -> None:
    """Parses command-line arguments and performs the requested actions."""
    args = parser_command_line_arguments()

    if args.list:
        with open('SEQUENCES_LIST.md', 'r') as file:
            content = file.read()
            print(content)
        sys.exit(1)

    if not args.sequence:
        sys.exit('no sequentium give.. please see --help')
    else:
        sequence = import_sequence_dynamically(sequence=args.sequence)
        if args.at:
            if args.at < 0:
                sys.exit(f'invalid int value for --start: {args.at}. Expected a non-negative integer!')
            print(sequence[args.at])
            sys.exit(-1)
        elif args.start is not None:
            if args.start < 0:
                sys.exit(f'invalid int value for --start: {args.start}. Expected a non-negative integer!')
            print(f'{sequence}: {sequence._as_list(start=args.start, stop=args.stop, step=args.step)}')
        elif args.contains is not None:
            print(args.contains in sequence)
        elif args.length:
            try:
                sequence_length = len(sequence)
            except InfiniteSequenceError:
                sys.exit(f'{sequence}: the sequentium is infinite')
            else:
                print(f'{sequence} has order {sequence_length}')
        else:
            print(sequence)


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
            print(content)
        sys.exit(1)

    def execute_sequence_command(self, args: argparse.Namespace) -> None:
        if not args.sequence:
            sys.exit('no sequentium given.. please see --help')
        else:
            sequence = import_sequence_dynamically(sequence=args.sequence)
            if args.at:
                self.execute_at_command(args, sequence)
            elif args.length:
                self.execute_length_command(sequence)
            elif args.contains:
                self.execute_contains_command(args, sequence)
            elif args.start is not None:
                if args.start < 0:
                    sys.exit(f'invalid int value for --start: {args.start}. Expected a non-negative integer!')
                print(f'{sequence}: {sequence._as_list(start=args.start, stop=args.stop, step=args.step)}')
            else:
                print(sequence.__str__().capitalize())

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
