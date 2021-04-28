Flatter
================

run this test::

~/Flatter$ nose2 -v
test_flatten_0 (tests.test_arrays.TestArrays) ... ok
test_flatten_1 (tests.test_arrays.TestArrays) ... ok
test_flatten_failed_0 (tests.test_arrays.TestArrays) ... FAIL
test_flatten_failed_1 (tests.test_arrays.TestArrays) ... FAIL

======================================================================
FAIL: test_flatten_failed_0 (tests.test_arrays.TestArrays)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/Flatter/tests/test_arrays.py", line 18, in test_flatten_failed_0
    self.assertEqual(_.flatten(self.testdata['input1']),
AssertionError: Lists differ: [1, 2, 3, 4, '5'] != [1, 2, 3, 4, 5]

First differing element 4:
'5'
5

- [1, 2, 3, 4, '5']
?              - -

+ [1, 2, 3, 4, 5] : invalid input only integer

======================================================================
FAIL: test_flatten_failed_1 (tests.test_arrays.TestArrays)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/Flatter/tests/test_arrays.py", line 27, in test_flatten_failed_1
    self.assertEqual(_.flatten(self.testdata['input3']),
AssertionError: Lists differ: ['14', 29, 28, 22, 2, 14, 14, 39, 29, 3, 1[4491 chars]3, 9] != [14, 29, 28, 22, 2, 14, 14, 39, 29, 3, 16,[4487 chars]3, 9]

First differing element 0:
'14'
14

Diff is 14658 characters long. Set self.maxDiff to None to see it. : invalid input only integer

----------------------------------------------------------------------
Ran 4 tests in 171.293s

FAILED (failures=2)