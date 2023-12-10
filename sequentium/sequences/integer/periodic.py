from sequentium.core.finite_type import Periodic


class A128834(Periodic):
    """Sequence A128834 (https://oeis.org/A128834)."""

    def __init__(self):
        super().__init__(_period=6)
        self.sequence = [0, 1, 1, 0, -1, -1]

    def __str__(self):
        return 'sequentium A128834'
