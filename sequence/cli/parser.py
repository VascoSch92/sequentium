import argparse
from sequence.__version__ import __version__


class CliParser:
    """ A command-line interface parser"""

    def parser(self) -> argparse.Namespace:
        """Parses command-line arguments and returns the parsed arguments as a namespace."""
        parser = self.create_parser()
        parser = self.add_groups_to_parser(parser=parser)
        parser = self.add_sequence_arguments(parser=parser)
        return parser.parse_args()

    def create_parser(self) -> argparse.ArgumentParser:
        """Creates an ArgumentParser with program name, description, and epilog."""
        return argparse.ArgumentParser(
            prog='Sequentium',
            description='Sequentium is a tool for working with mathematical sequences.',
            epilog='For help with a specific command, see: `sequence help <command>`.',
        )

    def add_groups_to_parser(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """
        Adds mutually exclusive argument groups for version information, listing sequences,
        and sequence identification.
        """
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
            nargs='+',
            choices=['all', 'integer', 'generalised'],
            help="List of implemented sequences.",
        )
        group.add_argument(
            'sequence',
            type=str,
            nargs='?',
            help='Specify the name or identifier of the sequence to operate on.',
        )
        return parser

    def add_sequence_arguments(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """
        Adds arguments related to sequence operations such as retrieving terms, displaying length,
        defining start/stop points, specifying step size, and checking for a specific value.
        """
        sequence_group = parser.add_argument_group('sequence options')
        sequence_group.add_argument(
            '-a',
            '--at',
            type=int,
            default=None,
            help='Retrieve the term at the specified index in the sequence.',
        )
        sequence_group.add_argument(
            '-l',
            '--length',
            action='store_true',
            default=None,
            help='Display the length of the sequence.',
        )
        sequence_group.add_argument(
            "--start",
            type=int,
            default=None,
            help="Define the starting point of the sequence.",
        )
        sequence_group.add_argument(
            "--stop",
            type=int,
            default=None,
            help="End point of the sequence (excluded).",
        )
        sequence_group.add_argument(
            '--step',
            type=int,
            default=None,
            help='Step size for iterating through the sequence.',
        )
        sequence_group.add_argument(
            '-c',
            type=int,
            default=None,
            help='Check if the sequence contains a specific value.',
        )
        return parser
