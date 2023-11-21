from sequence.sequences.integer.periodic import *
from tests.sequence_test_suite import PeriodicSequenceTestSuite


class TestA033999(PeriodicSequenceTestSuite):
    sequence = A033999()  # Sequence of powers of -1
    ground_truth = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
    ground_truth_length = len(ground_truth)
    period_length = 2

