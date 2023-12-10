import argparse
from sequentium import __version__


class CliParser:

    def parser(self) -> argparse.Namespace:
        parser = self.create_parser()
        parser = self.add_groups_to_parser(parser=parser)
        parser = self.add_arguments(parser=parser)
        return parser.parse_args()

    def create_parser(self) -> argparse.ArgumentParser:
        return argparse.ArgumentParser(
            prog='Sequentium',
            description='Sequentium is a tool for working with mathematical sequences.',
            epilog='For help with a specific command, see: `sequentium help <command>`.',
        )

    def add_groups_to_parser(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
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
        return parser

    def add_arguments(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        sequence_group = parser.add_argument_group('sequentium options')
        sequence_group.add_argument(
            '-a',
            '--at',
            type=int,
            default=None,
            help='Retrieve the term at the specified index in the sequentium.',
        )
        sequence_group.add_argument(
            '-l',
            '--length',
            action='store_true',
            default=None,
            help='Display the length of the sequentium.',
        )
        sequence_group.add_argument(
            "--start",
            type=int,
            default=None,
            help="Define the starting point of the sequentium.",
        )
        sequence_group.add_argument(
            "--stop",
            type=int,
            default=None,
            help="End point of the sequentium (excluded).",
        )
        sequence_group.add_argument(
            '--step',
            type=int,
            default=None,
            help='Step size for iterating through the sequentium.',
        )
        sequence_group.add_argument(
            '-c',
            type=int,
            default=None,
            help='Check if the sequentium contains a specific value.',
        )
        return parser
