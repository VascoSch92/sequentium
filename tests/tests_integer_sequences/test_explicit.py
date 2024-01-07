from sequence.sequences.integer.explicit import *
from tests.sequence_test_suite import SequenceTestSuite


class TestA000027(SequenceTestSuite):
    sequence = A000027()
    sequence_name = 'natural numbers'
    ground_truth = list(range(100))


class TestA000217(SequenceTestSuite):
    sequence = A000217()
    sequence_name = 'triangular numbers'
    ground_truth = [
        0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253,
        276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903,
        946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431,
    ]


class TestA000290(SequenceTestSuite):
    sequence = A000290()
    sequence_name = 'square numbers'
    ground_truth = [n**2 for n in range(100)]


class TestA000326(SequenceTestSuite):
    sequence = A000326()
    sequence_name = 'pentagonal numbers'
    ground_truth = [
        0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287,
        330, 376, 425, 477, 532, 590, 651, 715, 782, 852, 925, 1001,
        1080, 1162, 1247, 1335, 1426, 1520, 1617, 1717, 1820, 1926,
        2035, 2147, 2262, 2380, 2501, 2625, 2752, 2882, 3015, 3151,
    ]


class TestA000384(SequenceTestSuite):
    sequence = A000384()
    sequence_name = 'hexagonal numbers'
    ground_truth = [
        0, 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378, 435, 496, 561, 630, 703, 780, 861, 946, 1035,
        1128, 1225, 1326, 1431, 1540, 1653, 1770, 1891, 2016, 2145, 2278, 2415, 2556, 2701, 2850, 3003, 3160, 3321,
        3486, 3655, 3828, 4005, 4186, 4371, 4560,
    ]


class TestA000566(SequenceTestSuite):
    sequence = A000566()
    sequence_name = 'heptagonal numbers'
    ground_truth = [
        0, 1, 7, 18, 34, 55, 81, 112, 148, 189, 235, 286, 342, 403, 469, 540, 616, 697, 783, 874, 970, 1071, 1177,
        1288, 1404, 1525, 1651, 1782, 1918, 2059, 2205, 2356, 2512, 2673, 2839, 3010, 3186, 3367, 3553, 3744, 3940,
        4141, 4347, 4558, 4774, 4995, 5221, 5452, 5688,
    ]


class TestA000567(SequenceTestSuite):
    sequence = A000567()
    sequence_name = 'octagonal numbers'
    ground_truth = [
        0, 1, 8, 21, 40, 65, 96, 133, 176, 225, 280, 341, 408, 481, 560, 645, 736, 833, 936, 1045, 1160, 1281, 1408,
        1541, 1680, 1825, 1976, 2133, 2296, 2465, 2640, 2821, 3008, 3201, 3400, 3605, 3816, 4033, 4256, 4485, 4720,
        4961, 5208, 5461,
    ]


class TestA001045(SequenceTestSuite):
    sequence = A001045()
    sequence_name = 'Jacobsthal numbers'
    ground_truth = [
        0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691, 87381, 174763, 349525,
        699051, 1398101, 2796203, 5592405, 11184811, 22369621, 44739243, 89478485, 178956971, 357913941, 715827883,
        1431655765, 2863311531, 5726623061, 11453246123,
    ]


class TestA003215(SequenceTestSuite):
    sequence = A003215()
    sequence_name = 'hex numbers'
    ground_truth = [1, 7, 19, 37, 61, 91, 127, 169, 217]


class TestA005408(SequenceTestSuite):
    sequence = A005408()
    sequence_name = 'odd numbers'
    ground_truth = [2 * index + 1 for index in range(50)]


class TestA014551(SequenceTestSuite):
    sequence = A014551()
    sequence_name = 'Jacobsthal-Lucas numbers'
    ground_truth = [
        2, 1, 5, 7, 17, 31, 65, 127, 257, 511, 1025, 2047, 4097, 8191, 16385, 32767, 65537, 131071, 262145, 524287,
        1048577, 2097151, 4194305, 8388607, 16777217, 33554431, 67108865, 134217727, 268435457, 536870911, 1073741825,
        2147483647, 4294967297, 8589934591,
    ]


class TestA033999(SequenceTestSuite):
    sequence = A033999()
    sequence_name = 'sequence of powers of -1'
    ground_truth = [(-1)**index for index in range(50)]
