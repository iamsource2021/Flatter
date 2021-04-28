import unittest
import json
import os
from flatter import Flatter

class TestArrays(unittest.TestCase):

  @classmethod
  def setUpClass(cls):      
      filename = open(os.getcwd() + '/tests/data/arrays.json',)
      cls.testdata = json.load(filename)
      filename.close()
    
  def test_flatten_0(self):
    f=Flatter(self.testdata['input0'])
    self.assertEqual(f.flattenInteger(),
                         self.testdata['case0'], 'can flatten nested arrays')

  def test_flatten_failed_0(self):
    f=Flatter(self.testdata['input1'])
    self.assertEqual(f.flattenInteger(),
                         self.testdata['case1'], 'invalid input only integer')

  def test_flatten_1(self):
    f=Flatter(self.testdata['input2'])
    self.assertEqual(f.flattenInteger(),
                         self.testdata['case2'], 'can flatten nested arrays')

  def test_flatten_failed_1(self):
    f=Flatter(self.testdata['input3'])
    #self.assertEqual.__self__.maxDiff = None
    self.assertEqual(f.flattenInteger(),
                         self.testdata['case3'], 'invalid input only integer') 
if __name__ == "__main__":

    unittest.main()