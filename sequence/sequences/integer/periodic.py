from sequence.core.finite_type import Periodic


class A087204(Periodic):
    """Sequence A087204 (https://oeis.org/A087204)."""
    sequence_name = 'sequence A087204'

    def __init__(self) -> None:
        super().__init__(_period=6)
        self.sequence = [2, 1, -1, -2, -1, 1]


class A128834(Periodic):
    """Sequence A128834 (https://oeis.org/A128834)."""
    sequence_name = 'sequence A128834'

    def __init__(self) -> None:
        super().__init__(_period=6)
        self.sequence = [0, 1, 1, 0, -1, -1]
