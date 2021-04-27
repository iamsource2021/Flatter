import unittest
import json
import os
from underscore import _

class TestArrays(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
      filename = open(os.getcwd() + '/tests/data/arrays.json',)
      cls.testdata = json.load(filename)
      filename.close()
    
  def test_flatten_0(self):
    self.assertEqual(_.flatten(self.testdata['input0']),
                         self.testdata['case0'], 'can flatten nested arrays')

  def test_flatten_failed_0(self):
          self.assertEqual(_.flatten(self.testdata['input1']),
                         self.testdata['case1'], 'invalid input only integer')

  def test_flatten_1(self):
    self.assertEqual(_.flatten(self.testdata['input2']),
                         self.testdata['case2'], 'can flatten nested arrays')

  def test_flatten_failed_1(self):
    #self.assertEqual.__self__.maxDiff = None
    self.assertEqual(_.flatten(self.testdata['input3']),
                         self.testdata['case3'], 'invalid input only integer') 
if __name__ == "__main__":
    unittest.main()
