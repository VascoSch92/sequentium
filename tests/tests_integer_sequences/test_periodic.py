from tests.sequence_test_suite import PeriodicSequenceTestSuite
from sequence.sequences.integer.periodic import *


class TestA087204(PeriodicSequenceTestSuite):
    sequence = A087204()
    sequence_name = 'sequence A087204'
    period_length = 6
    ground_truth = [
        2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1,
        -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1,
        -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2, -1, 1, 2, 1, -1, -2,
        -1, 1, 2, 1, -1, -2, -1, 1,
    ]


class TestA128834(PeriodicSequenceTestSuite):
    sequence = A128834()
    sequence_name = 'sequence A128834'
    period_length = 6
    ground_truth = [
        0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1,
        0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1,
        0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0,
        -1, -1, 0, 1, 1,
    ]
