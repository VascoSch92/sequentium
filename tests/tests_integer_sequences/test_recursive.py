from tests.sequence_test_suite import SequenceTestSuite
from sequentium.sequences.integer.recursive import *


class TestA000032(SequenceTestSuite):
    sequence = A000032()
    sequence_name = 'Lucas numbers'
    ground_truth = [
        2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603,
        64079, 103682, 167761, 271443, 439204, 710647, 1149851, 1860498, 3010349, 4870847, 7881196, 12752043, 20633239,
        33385282, 54018521, 87403803,
    ]
    ground_truth_length = len(ground_truth)


class TestA000045(SequenceTestSuite):
    sequence = A000045()
    sequence_name = 'Fibonacci numbers'
    ground_truth = [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765,
        10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309,
        3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155,
    ]
    ground_truth_length = len(ground_truth)


class TestA000073(SequenceTestSuite):
    sequence = A000073()
    sequence_name = 'Tribonacci numbers'
    ground_truth = [
        0, 1, 0, 1, 2, 3, 6, 11, 20, 37, 68, 125, 230, 423, 778, 1431, 2632, 4841, 8904, 16377, 30122,
        55403, 101902, 187427, 344732, 634061, 1166220, 2145013, 3945294, 7256527, 13346834, 24548655,
        45152016, 83047505, 152748176, 280947697, 516743378, 950439251,
    ]
    ground_truth_length = len(ground_truth)

