
Flatter
--------

run this test::

~/Flatter$ python setup.py test
running test
WARNING: Testing via this command is deprecated and will be removed in a future version. Users looking for a generic test entry point independent of test runner are encouraged to use tox.
running egg_info
creating flatter.egg-info
writing flatter.egg-info/PKG-INFO
writing dependency_links to flatter.egg-info/dependency_links.txt
writing requirements to flatter.egg-info/requires.txt
writing top-level names to flatter.egg-info/top_level.txt
writing manifest file 'flatter.egg-info/SOURCES.txt'
reading manifest file 'flatter.egg-info/SOURCES.txt'
writing manifest file 'flatter.egg-info/SOURCES.txt'
running build_ext
..FF
======================================================================
FAIL: test_flatten_failed_0 (tests.test_arrays.TestArrays)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/Flatter/tests/test_arrays.py", line 21, in test_flatten_failed_0
    self.assertEqual(f.flattenInteger(),
AssertionError: Lists differ: [] != [1, 2, 3, 4, 5]

Second list contains 5 additional elements.
First extra element 0:
1

- []
+ [1, 2, 3, 4, 5] : invalid input only integer

======================================================================
FAIL: test_flatten_failed_1 (tests.test_arrays.TestArrays)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/runner/Flatter/tests/test_arrays.py", line 32, in test_flatten_failed_1
    self.assertEqual(f.flattenInteger(),
AssertionError: Lists differ: [] != [14, 29, 28, 22, 2, 14, 14, 39, 29, 3, 16,[4487 chars]3, 9]

Second list contains 1200 additional elements.
First extra element 0:
14

Diff is 8139 characters long. Set self.maxDiff to None to see it. : invalid input only integer

----------------------------------------------------------------------
Ran 4 tests in 0.199s

FAILED (failures=2)