from sequence.cli.parser import CliParser
from sequence.cli.commands.list import execute_command_list
from sequence.cli.commands.sequence import execute_sequence_command


class CommandLineInterface:
    """A command-line interface for interacting with sequences."""

    @staticmethod
    def execute() -> None:
        """
        Parses command-line arguments using CliParser and executes either the print_list or execute_sequence_command
        based on the arguments.
        """
        args = CliParser().parse()

        if args.list:
            execute_command_list(args=args)
        else:
            execute_sequence_command(args=args)


def execute_command_line_interface() -> None:
    CommandLineInterface.execute()
