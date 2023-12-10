from tests.sequence_test_suite import PeriodicSequenceTestSuite
from sequentium.sequences.integer.periodic import *


class TestA128834(PeriodicSequenceTestSuite):
    sequence = A128834()
    sequence_name = 'sequentium A128834'
    period_length = 6
    ground_truth = [
        0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1,
        0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1,
        0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1, 1, 0,
        -1, -1, 0, 1, 1,
    ]
    ground_truth_length = len(ground_truth)



