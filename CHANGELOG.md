
# Changelog

---
### Legend

- API_CHANGE: Any changes to the project's API
- DEPRECATED: Indication of features that will be removed in future releases
- ENHANCEMENT: Improvements to existing features that do not introduce new functionality
- FEATURE: New features added to enhance functionality
- FIX: Resolved issues, bugs, or unexpected behavior
- REMOVED: Features or functionalities removed from the project

### Version Policy

The version is represented by three digits: a.b.c.
- Bump the first digit (a) for an API_CHANGE.
- Bump the second digit (b) for a FEATURE or a critical FIX.
- Bump the third digit (c) for an ENHANCEMENT or a small FIX.
- Once a digit is bumped, set all the digits to its right to zero.

---
## Unreleased

ENHANCEMENT:
- ruff.toml: config update with new rules
- README.md: add badges

---
## [0.0.2] - 2024-01-07

ENHANCEMENT:
- sequentium.github.workflows.release.yml: workflow for automatic upload on pypi
- sequentium.sequence.sequences.integer.periodic_generalised.py: added class for representing constant sequences
- sequentium.sequence.sequences.integer.recursive.py: added sequence A001608
- sequentium.sequence.sequences.integer.explicit.py: added sequence A000566 (heptagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A000567 (octagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A001106 (nonagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A001107 (decagonal numbers) 
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051682 (hendecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051624 (dodecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051865 (tridecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051866 (tetradecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051867 (pentadecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051868 (hexadecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051869 (heptadecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051870 (octadecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051871 (enneadecagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051872 (icosagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051873 (icosihenagonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051874 (Icosidigonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051875 (icositrigonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A051876 (icositetragonal numbers)
- sequentium.sequence.sequences.integer.explicit.py: added sequence A167149 (myriagonal numbers)


## [0.0.1] - 2024-01-02

ENHANCEMENT:
- sequentium.tests.sequence_tests_suite.py: self.ground_truth_length is removed as we can perform same tests without it.
- sequentium.core.core.py: added __str__ method in Sequence class
- sequentium.ruff.toml: added rule "ANN"
- sequentium.core.core.py: added __eq__ method in Sequence clas
- sequentium.core.mixin.py: new script for mixin classes
- sequentium.core.mixin.py: added AlmostMonotonicIncreasingMixin class
- sequentium.sequences.integer.recursive.py: added A000931

FIX:
- sequentium.core.core.py: method __getitem__ return a generator when the stop value in the slice is missing

## [0.0.0] - 2023-12-28

First version of Sequentium :-D 
