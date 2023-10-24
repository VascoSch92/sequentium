from tests.sequence_test_suite import SequenceTestSuite
from sequencepy.sequences.integer.recursive import *


class TestA000045(SequenceTestSuite):
    sequence = A000045()  # Fibonacci numbers
    ground_truth = [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
        10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309,
        3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155,
    ]
    ground_truth_length = len(ground_truth)


class TestA000073(SequenceTestSuite):
    sequence = A000073()  # Tribonacci numbers
    ground_truth = [
        0, 1, 0, 1, 2, 3, 6, 11, 20, 37, 68, 125, 230, 423, 778, 1431, 2632, 4841, 8904, 16377, 30122,
        55403, 101902, 187427, 344732, 634061, 1166220, 2145013, 3945294, 7256527, 13346834, 24548655,
        45152016, 83047505, 152748176, 280947697, 516743378, 950439251
    ]
    ground_truth_length = len(ground_truth)
