TEST_CASES_ORDER_SCRIPT = [
    ('sequentium/sequences/integer/explicit.py', r'^A\d{6}$'),
    ('sequentium/sequences/integer/explicit_generalised_sequences.py', None),
    ('sequentium/sequences/integer/finite.py', r'^A\d{6}$'),
    ('sequentium/sequences/integer/periodic.py', r'^A\d{6}$'),
    ('tests/tests_integer_sequences/test_periodic.py', None),
    ('sequentium/sequences/integer/property_defined.py', r'^A\d{6}$'),
    ('sequentium/sequences/integer/property_defined_generalised_sequences.py', None),
    ('sequentium/sequences/integer/recursive.py', r'^A\d{6}$'),
    ('sequentium/sequences/integer/recursive_generalised_sequences.py', None),
    ('tests/tests_integer_sequences/test_explicit.py', None),
    ('tests/tests_integer_sequences/test_finite.py', None),
    ('tests/tests_integer_sequences/test_periodic.py', None),
    ('tests/tests_integer_sequences/test_recursive.py', None),
]

TEST_CASES_TESTED_SEQUENCES = [
    ('sequentium/sequences/integer/explicit.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_explicit.py'),
    ('sequentium/sequences/integer/finite.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_finite.py'),
    ('sequentium/sequences/integer/periodic.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_periodic.py'),
    ('sequentium/sequences/integer/recursive.py', r'^A\d{6}$', 'tests/tests_integer_sequences/test_recursive.py'),
]
