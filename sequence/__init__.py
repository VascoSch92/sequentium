from sequence.cli.cli import execute_command_line_interface

from sequence.sequences.integer.explicit import *
from sequence.sequences.integer.finite import *
from sequence.sequences.integer.periodic import *
from sequence.sequences.integer.property_defined import *
from sequence.sequences.integer.recursive import *


def main():
    execute_command_line_interface()


if __name__ == '__main__':
    main()
