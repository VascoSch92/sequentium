from tests.sequence_test_suite import SequenceTestSuite
from sequence.sequences.integer.recursive import *


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
        0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012,
        121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096,
        181997601, 334745777, 615693474, 1132436852,
    ]
    ground_truth_length = len(ground_truth)


class TestA000129(SequenceTestSuite):
    sequence = A000129()
    sequence_name = 'Pell numbers'
    ground_truth = [
        0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, 80782, 195025, 470832, 1136689, 2744210,
        6625109, 15994428, 38613965, 93222358, 225058681, 543339720, 1311738121, 3166815962, 7645370045, 18457556052,
        44560482149, 107578520350, 259717522849,
    ]
    ground_truth_length = len(ground_truth)


class TestA002203(SequenceTestSuite):
    sequence = A002203()
    sequence_name = 'Companion Pell numbers'
    ground_truth = [
        2, 2, 6, 14, 34, 82, 198, 478, 1154, 2786, 6726, 16238, 39202, 94642, 228486, 551614, 1331714, 3215042,
        7761798, 18738638, 45239074, 109216786, 263672646, 636562078, 1536796802, 3710155682, 8957108166, 21624372014,
        52205852194, 126036076402, 304278004998,
    ]
    ground_truth_length = len(ground_truth)


class TestA214733(SequenceTestSuite):
    sequence = A214733()
    sequence_name = 'sequence A214733'
    ground_truth = [
        0, 1, -1, -2, 5, 1, -16, 13, 35, -74, -31, 253, -160, -599, 1079, 718, -3955, 1801, 10064, -15467, -14725,
        61126, -16951, -166427, 217280, 282001, -933841, 87838, 2713685, -2977199, -5163856, 14095453, 1396115,
        -43682474, 39494129, 91553293, -210035680,
    ]
    ground_truth_length = len(ground_truth)

