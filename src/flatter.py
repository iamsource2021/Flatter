from underscore import _

class Flatter():

  def __init__(self,arr):
    self.arr = arr
    
  def hasListInteger(self, n:int):
    for i in range(0,n):
      if type(self.arr[i]) != int:
        return False
        continue
    return True    

  def flattenInteger(self)->list:
    self.arr = _.flatten(self.arr)
    n = len(self.arr)
    if self.hasListInteger(n): return self.arr
    else: return []