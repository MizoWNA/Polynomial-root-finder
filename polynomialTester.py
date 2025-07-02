from mySuperscript import to_superscript
from polyTools import derive


def printHelper(inputOriginal):
  print("Original Polynomial >")
  originialPoly = []
  p = len(inputOriginal) - 1
  for i in inputOriginal:
    if i != 0:
      originialPoly.append(f"{i}x{to_superscript(str(p))}")
      p = p - 1
    else:
      p = p -1
  
  print(" + ".join(originialPoly).replace("+ -", "- ").replace("x\u2070", "").replace("x\u00B9 ", "x "))
  
  print("Derived Polynomial >")
  derivedPoly = []
  derivedCoeff2 = derive(inputOriginal)
  p = len(derivedCoeff2) - 1
  for i in derivedCoeff2:
    if i != 0:
      derivedPoly.append(f"{i}x{to_superscript(str(p))}")
      p = p - 1
    else:
      p = p -1
  print(" + ".join(derivedPoly).replace("+ -", "- ").replace("x\u2070", "").replace("x\u00B9 ", "x "))


printHelper([1, 0, -1, -1/3, 4])