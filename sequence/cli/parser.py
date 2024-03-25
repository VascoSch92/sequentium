import argparse

from sequence.__version__ import __version__


class CliParser:
    """A command-line interface parser"""

    def parse(self) -> argparse.Namespace:
        """Parses command-line arguments and returns the parsed arguments as a namespace."""
        parser = self.create_parser()
        parser = self.add_version_command(parser=parser)
        parser = self.add_groups_to_parser(parser=parser)
        parser = self.add_sequence_arguments(parser=parser)
        namespace = parser.parse_args()
        self.validate_parser(namespace=namespace, parser=parser)
        return namespace

    def create_parser(self) -> argparse.ArgumentParser:
        """Creates an ArgumentParser with program name, description, and epilog."""
        return argparse.ArgumentParser(
            prog="Sequentium",
            description="Sequentium is a user-friendly package that implements various well-known sequences, "
            "providing a seamless and intuitive experience for the user",
            epilog="For help with a specific command, see: `sequence help <command>`",
        )

    def add_version_command(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"{parser.prog}: v{__version__}",
            help="Display the version information.",
        )
        return parser

    def add_groups_to_parser(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """
        Adds mutually exclusive argument groups for version information, listing sequences,
        and sequence identification.
        """
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            "--list",
            nargs="+",
            choices=["integer", "generalised"],
            help="List of implemented sequences.",
        )
        group.add_argument(
            "sequence",
            type=str,
            nargs="?",
            help="Specify the name or identifier of the sequence to operate on.",
        )
        return parser

    def add_sequence_arguments(self, parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        """
        Adds arguments related to sequence operations such as retrieving terms, displaying length,
        defining start/stop points, specifying step size, and checking for a specific value.
        """
        sequence_group = parser.add_argument_group("sequence options")
        sequence_group.add_argument(
            "-a",
            "--at",
            type=int,
            default=None,
            help="Retrieve the term at the specified index in the sequence.",
        )
        sequence_group.add_argument(
            "-l",
            "--length",
            action="store_true",
            default=None,
            help="Display the length of the sequence.",
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
            "--step",
            type=int,
            default=None,
            help="Step size for iterating through the sequence.",
        )
        sequence_group.add_argument(
            "-c",
            "--contains",
            type=int,
            default=None,
            help="Check if the sequence contains a specific value.",
        )
        return parser

    def validate_parser(
        self,
        namespace: argparse.Namespace,
        parser: argparse.ArgumentParser,
    ) -> argparse.Namespace:
        """Validate the provided namespace using the given parser."""
        if namespace.list is None and namespace.sequence is None:
            parser.error(message="No sequence or option provided. Please see --help")
        elif namespace.list is not None and namespace.sequence is not None:
            parser.error(message="argument --list: not allowed with argument sequence")
        elif namespace.list is not None and namespace.sequence is None:
            if len(namespace.list) > 1:
                parser.error(
                    message=f"argument --list: too many options provided. Expected 1, got {len(namespace.list)}"
                )
        else:
            namespace = self.validate_sequence_options(namespace=namespace, parser=parser)
        return namespace

    def validate_sequence_options(
        self,
        namespace: argparse.Namespace,
        parser: argparse.ArgumentParser,
    ) -> argparse.Namespace:
        """Validate the selected options for a sequence in the provided namespace using the given parser."""
        selected_options = {key for key, value in vars(namespace).items() if value is not None}
        selected_options.remove("sequence")

        if len(selected_options) == 0:
            parser.error(message=f"No options chosen for sequence {namespace.sequence.__str__()}")
        elif len(selected_options) > 1:  # noqa: SIM102
            if "at" in selected_options or "c" in selected_options or "length" in selected_options:
                parser.error(message=f"options {list(selected_options)}: not allowed together")

        return namespace
