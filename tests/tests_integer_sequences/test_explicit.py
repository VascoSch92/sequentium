from sequence.sequences.integer.explicit import *
from tests.sequence_test_suite import SequenceTestSuite


class TestA000027(SequenceTestSuite):
    sequence = A000027()
    sequence_name = 'natural numbers'
    ground_truth = list(range(100))
    ground_truth_length = len(ground_truth)


class TestA000326(SequenceTestSuite):
    sequence = A000326()
    sequence_name = 'pentagonal numbers'
    ground_truth = [
        0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287,
        330, 376, 425, 477, 532, 590, 651, 715, 782, 852, 925, 1001,
        1080, 1162, 1247, 1335, 1426, 1520, 1617, 1717, 1820, 1926,
        2035, 2147, 2262, 2380, 2501, 2625, 2752, 2882, 3015, 3151,
    ]
    ground_truth_length = len(ground_truth)


class TestA001045(SequenceTestSuite):
    sequence = A001045()
    sequence_name = 'Jacobsthal numbers'
    ground_truth = [
        0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, 87381, 174763, 349525,
        699051, 1398101, 2796203, 5592405, 11184811, 22369621, 44739243, 89478485, 178956971, 357913941, 715827883,
        1431655765, 2863311531, 5726623061, 11453246123,
    ]
    ground_truth_length = len(ground_truth)


class TestA003215(SequenceTestSuite):
    sequence = A003215()
    sequence_name = 'hex numbers'
    ground_truth = [1, 7, 19, 37, 61, 91, 127, 169, 217]
    ground_truth_length = len(ground_truth)


class TestA005408(SequenceTestSuite):
    sequence = A005408()
    sequence_name = 'odd numbers'
    ground_truth = [2 * index + 1 for index in range(50)]
    ground_truth_length = len(ground_truth)


class TestA014551(SequenceTestSuite):
    sequence = A014551()
    sequence_name = 'Jacobsthal-Lucas numbers'
    ground_truth = [
        2, 1, 5, 7, 17, 31, 65, 127, 257, 511, 1025, 2047, 4097, 8191, 16385, 32767, 65537, 131071, 262145, 524287,
        1048577, 2097151, 4194305, 8388607, 16777217, 33554431, 67108865, 134217727, 268435457, 536870911, 1073741825,
        2147483647, 4294967297, 8589934591,
    ]
    ground_truth_length = len(ground_truth)


class TestA033999(SequenceTestSuite):
    sequence = A033999()
    sequence_name = 'sequence of powers of -1'
    ground_truth = [(-1)**index for index in range(50)]
    ground_truth_length = len(ground_truth)
