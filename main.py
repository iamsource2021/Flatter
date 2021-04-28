from src.flatter import Flatter

if __name__ == '__main__':    
  f=Flatter([1, [2, [3, [4, 5]]]])
  arrIntegerFlatt = f.flattenInteger()
  print(arrIntegerFlatt)

