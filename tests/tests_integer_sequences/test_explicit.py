from sequence.sequences.integer.explicit import *
from tests.sequence_test_suite import SequenceTestSuite


class TestA000027(SequenceTestSuite):
    sequence = A000027() # Natural numbers
    ground_truth = list(range(100))
    ground_truth_length = len(ground_truth)


class TestA000326(SequenceTestSuite):
    sequence = A000326()  # Pentagonal numbers
    ground_truth = [
        0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287,
        330, 376, 425, 477, 532, 590, 651, 715, 782, 852, 925, 1001,
        1080, 1162, 1247, 1335, 1426, 1520, 1617, 1717, 1820, 1926,
        2035, 2147, 2262, 2380, 2501, 2625, 2752, 2882, 3015, 3151,
    ]
    ground_truth_length = len(ground_truth)


class TestA003215(SequenceTestSuite):
    sequence = A003215()  # Hex numbers
    ground_truth = [1, 7, 19, 37, 61, 91, 127, 169, 217]
    ground_truth_length = len(ground_truth)


class TestA005408(SequenceTestSuite):
    sequence = A005408()  # Odd numbers
    ground_truth = [2 * index + 1 for index in range(50)]
    ground_truth_length = len(ground_truth)


class TestA033999(SequenceTestSuite):
    sequence = A033999()  # Sequence of powers of -1
    ground_truth = [(-1)**index for index in range(50)]
    ground_truth_length = len(ground_truth)
