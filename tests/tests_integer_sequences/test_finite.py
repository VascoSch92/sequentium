from sequence.sequences.integer.finite import *
from tests.sequence_test_suite import FiniteSequenceTestSuite


class TestA001228(FiniteSequenceTestSuite):
    sequence = A001228()  # Orders of sporadic simple groups
    ground_truth = [
        7920, 95040, 175560, 443520, 604800, 10200960, 44352000, 50232960, 244823040, 898128000, 4030387200,
        145926144000, 448345497600, 460815505920, 495766656000, 42305421312000, 64561751654400, 273030912000000,
        51765179004000000, 90745943887872000, 4089470473293004800, 4157776806543360000, 86775571046077562880,
        1255205709190661721292800, 4154781481226426191177580544000000,
        808017424794512875886459904961710757005754368000000000,
    ]
    ground_truth_length = len(ground_truth)


class TestA003173(FiniteSequenceTestSuite):
    sequence = A003173()  # Heegner numbers
    ground_truth = [1, 2, 3, 7, 11, 19, 43, 67, 163]
    ground_truth_length = len(ground_truth)


class TestCollatzSequence(FiniteSequenceTestSuite):
    sequence = CollatzSequence(start_value=19)  # Collatz sequence
    ground_truth = [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    ground_truth_length = len(ground_truth)
