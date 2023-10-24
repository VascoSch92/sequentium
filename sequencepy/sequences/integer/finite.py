from sequencepy.base.sequence import FiniteSequence


class A001228(FiniteSequence):
    """ Orders of sporadic simple groups (https://oeis.org/A001228) """

    def __init__(self):
        super().__init__()
        self.sequence = [
            7920, 95040, 175560, 443520, 604800, 10200960, 44352000, 50232960, 244823040, 898128000, 4030387200,
            145926144000, 448345497600, 460815505920, 495766656000, 42305421312000, 64561751654400, 273030912000000,
            51765179004000000, 90745943887872000, 4089470473293004800, 4157776806543360000, 86775571046077562880,
            1255205709190661721292800, 4154781481226426191177580544000000,
            808017424794512875886459904961710757005754368000000000,
        ]


class A003173(FiniteSequence):
    """ Heegner numbers: imaginary quadratic fields with unique factorization (https://oeis.org/A003173) """

    def __init__(self):
        super().__init__()
        self.sequence = [1, 2, 3, 7, 11, 19, 43, 67, 163]


class HeegnerNumbers(A003173):
    pass
