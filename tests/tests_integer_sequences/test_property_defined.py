from tests.sequence_test_suite import SequenceTestSuite
from sequencepy.sequences.integer.property_defined import *


class TestA000040(SequenceTestSuite):
    sequence = PrimeNumbers()
    ground_truth = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    ground_truth_length = len(ground_truth)
