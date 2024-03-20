import sys
import argparse
import importlib
from typing import Type

from sequence.core.core import Sequence


def execute_sequence_command(args: argparse.Namespace) -> None:
    """Executes a specific sequence command based on the provided arguments."""
    sequence = import_sequence_dynamically(sequence=args.sequence)
    if args.at is not None:
        execute_at_command(args=args, sequence=sequence)
    elif args.length is not None:
        execute_length_command(sequence=sequence)
    elif args.contains is not None:
        execute_contains_command(args=args, sequence=sequence)
    else:
        execute_as_list_command(args=args, sequence=sequence)


def import_sequence_dynamically(sequence: str) -> Type[Sequence]:
    """Dynamically import a sequence class by name."""
    try:
        sequence_module = importlib.import_module("sequence")
        sequence_class = getattr(sequence_module, f"{sequence}")
    except ImportError:
        sys.exit(f"Sequence {sequence} is not implemented yet!")
    else:
        return sequence_class()


def execute_as_list_command(args: argparse.Namespace, sequence: Type[Sequence]) -> None:
    """Execute the `as list` command, i.e., print a part of the sequence."""
    if args.start is None:
        args.start = 0
    if args.start < 0:
        sys.exit(f"invalid int value for --start: {args.start}. Expected a non-negative integer")
    if args.start > args.stop:
        sys.exit(f"invalid int value for --stop: {args.stop}. Expected a value bigger than --start")
    sys.exit(sequence[args.start : args.stop : args.step])


def execute_contains_command(args: argparse.Namespace, sequence: Type[Sequence]) -> None:
    sys.exit(f"{args.contains in sequence}")


def execute_length_command(sequence: Type[Sequence]) -> None:
    if sequence.is_finite:
        sys.exit(f"{len(sequence)}")
    else:
        sys.exit(f'{float("inf")}')


def execute_at_command(args: argparse.Namespace, sequence: Type[Sequence]) -> None:
    if args.at < 0:
        sys.exit(f"invalid int value for --start: {args.at}. Expected a non-negative integer!")
    else:
        sys.exit(f"{sequence[args.at]}")
