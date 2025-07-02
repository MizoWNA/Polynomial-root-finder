inp = [1, 0, -1, -1/3, 4]


def derive(x):
  x = x[:-1]
  derivedCoeff = []
  p = len(x)
  for i in x:
    derivedCoeff.append(i * p)
    p = p - 1
  return derivedCoeff

def to_superscript(text):
    superscript_map = {
        '0': '\u2070', '1': '\u00B9', '2': '\u00B2', '3': '\u00B3', '4': '\u2074',
        '5': '\u2075', '6': '\u2076', '7': '\u2077', '8': '\u2078', '9': '\u2079',
        'a': '\u1D43', 'b': '\u1D47', 'c': '\u1D9C', 'd': '\u1D48', 'e': '\u1D49',
        'f': '\u1DA0', 'g': '\u1D4D', 'h': '\u02B0', 'i': '\u2071', 'j': '\u02B2',
        'k': '\u1D4F', 'l': '\u02E1', 'm': '\u1D50', 'n': '\u207F', 'o': '\u1D52',
        'p': '\u1D56', 'q': '\u02B3', 'r': '\u02B3', 's': '\u02E2', 't': '\u1D57',
        'u': '\u1D58', 'v': '\u1D5B', 'w': '\u02B7', 'x': '\u02E3', 'y': '\u02B8',
        'z': '\u1DBB', '+': '\u207A', '-': '\u207B', '=': '\u207C', '(': '\u207D',
        ')': '\u207E'
    }
    
    superscripted_text = ""
    for char in str(text):
        superscripted_text += superscript_map.get(char, char)
    return superscripted_text
    
def printHelper():
  print("Original Polynomial >")
  originialPoly = []
  p = len(inp) - 1
  for i in inp:
    if i != 0:
      originialPoly.append(f"{i}x{to_superscript(str(p))}")
      p = p - 1
    else:
      p = p -1
  
  print(" + ".join(originialPoly).replace("+ -", "-").replace("x\u2070", ""))
  
  print("Derived Polynomial >")
  derivedPoly = []
  derivedCoeff2 = derive(inp)
  p = len(derivedCoeff2) - 1
  for i in derivedCoeff2:
    if i != 0:
      derivedPoly.append(f"{i}x{to_superscript(str(p))}")
      p = p - 1
    else:
      p = p -1
  print(" + ".join(derivedPoly).replace("+ -", "-").replace("x\u2070", ""))
  
def degree(x):
  return (len(x) - 1)
  
def polyDevide(devident, devisor):
  remainder = devident
  quotent = []
  
  
  
  



