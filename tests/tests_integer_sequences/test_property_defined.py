from tests.sequence_test_suite import SequenceTestSuite
from sequence.sequences.integer.property_defined import *


class TestA000040(SequenceTestSuite):
    sequence = A000040()
    sequence_name = 'prime numbers'
    ground_truth = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    ground_truth_length = len(ground_truth)


class TestA002808(SequenceTestSuite):
    sequence = A002808()
    sequence_name = 'composite numbers'
    ground_truth = [
        4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38,
        39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69,
        70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88,
    ]
    ground_truth_length = len(ground_truth)
