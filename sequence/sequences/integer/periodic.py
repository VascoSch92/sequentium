from sequence.core.finite_type import Periodic


class A033999(Periodic):
    """ Sequence of powers of -1 (https://oeis.org/A033999) """

    def __init__(self):
        super().__init__()
        self.sequence = [1, -1]
        self._period = 2
