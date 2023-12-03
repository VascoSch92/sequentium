import argparse
import importlib
import sys

from sequence import __version__
from sequence.core.core import Sequence
from sequence.core.utils.exceptions import InfiniteSequenceError


def parser_command_line_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog='Sequentium',
        description='Sequentium is a tool for working with mathematical sequences.',
        epilog='For help with a specific command, see: `sequentium help <command>`.'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=f'{__version__}',
        help='Display the version information.',
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help="List a list of implemented sequences.")
    parser.add_argument(
        "sequence",
        type=str,
        nargs="?",
        help="Specify the name or identifier of the sequence to operate on.",
    )
    parser.add_argument(
        '-a',
        '--at',
        type=int,
        default=None,
        help='Retrieve the term at the specified index in the sequence.'
    )
    parser.add_argument(
        '-l',
        '--length',
        action='store_true',
        default=None,
        help='Display the length of the sequence.'
    )
    parser.add_argument(
        "--start",
        type=int,
        default=None,
        help="Define the starting point of the sequence.",
    )
    parser.add_argument(
        "--stop",
        type=int,
        default=10,
        help="End point of the sequence (excluded).",
    )
    parser.add_argument(
        '--step',
        type=int,
        default=1,
        help='Step size for iterating through the sequence.',
    )
    parser.add_argument(
        '-c',
        '--contains',
        type=int,
        default=None,
        help='Check if the sequence contains a specific value.',
    )

    return parser.parse_args()


def import_sequence_dynamically(sequence: str) -> Sequence:
    """Dynamically import a sequence class by name."""
    try:
        sequence_module = importlib.import_module('sequence')
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
        sys.exit('no sequence give.. please see --help')
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
            print(f'{sequence}: {sequence.as_list(start=args.start, stop=args.stop, step=args.step)}')
        elif args.contains is not None:
            print(args.contains in sequence)
        elif args.length:
            try:
                sequence_length = len(sequence)
            except InfiniteSequenceError:
                sys.exit(f'{sequence}: the sequence is infinite')
            else:
                print(f'{sequence} has order {sequence_length}')
        else:
            print(sequence)
