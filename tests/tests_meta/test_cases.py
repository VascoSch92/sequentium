TEST_CASES_ORDER_SCRIPT = [
    ('sequence/sequences/integer/explicit.py', r'^A\d{6}$'),
    ('sequence/sequences/integer/explicit_generalised.py', None),
    ('sequence/sequences/integer/finite.py', r'^A\d{6}$'),
    ('sequence/sequences/integer/periodic.py', r'^A\d{6}$'),
    ('tests/tests_integer_sequences/test_periodic.py', None),
    ('sequence/sequences/integer/property_defined.py', r'^A\d{6}$'),
    ('sequence/sequences/integer/property_defined_generalised.py', None),
    ('sequence/sequences/integer/recursive.py', r'^A\d{6}$'),
    ('sequence/sequences/integer/recursive_generalised.py', None),
    ('tests/tests_integer_sequences/test_explicit.py', None),
    ('tests/tests_integer_sequences/test_finite.py', None),
    ('tests/tests_integer_sequences/test_periodic.py', None),
    ('tests/tests_integer_sequences/test_recursive.py', None),
]

TEST_CASES_TESTED_SEQUENCES = [
    ('sequence/sequences/integer/explicit.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_explicit.py'),
    ('sequence/sequences/integer/finite.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_finite.py'),
    ('sequence/sequences/integer/periodic.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_periodic.py'),
    ('sequence/sequences/integer/recursive.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_recursive.py'),
]
