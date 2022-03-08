import math
class rationals():
  def __init__(self,numerator,denominator):
    self.num = numerator
    self.den = denominator

  def convert(self,other):
    if type(other) == int:
      return(rationals(other,1))
  
  def __float__(self):
    return(self.num/self.den)

  def __int__(self):
    return(self.num//self.den)
  
  def __str__(self):
    return(str(self.num)+"/"+str(self.den))
  
  def __add__(self,other):
    other = self.convert(other)
    self.num = self.num*other.den+other.num*self.den
    self.den = self.den*other.den
    return(self.reduce())

  def __radd__(self,other):
    return(self+other)
  
  def __mul__(self,other):
    other = self.convert(other)
    return(rationals(self.num*other.num,self.den*other.den).reduce())

  def __rmul__(self,other):
    return(self*other)
  
  def  __truediv__(self,other):
    other = self.convert(other)
    return((self*other.invert()).reduce())

  def __rtruediv__(self,other):
    return(self.invert()*other)

  def __sub__(self,other):
    other = self.convert(other)
    print(self.den*other.den)
    self.num = self.num*other.den-other.num*self.den
    self.den = self.den*other.den
    return(self)

  def __rsub__(self,other):
    return(-self+other)

  def reduce(self):
    gcm = math.gcd(self.num,self.den)
    self.num = self.num//gcm
    self.den = self.den//gcm
    if self.den < 0:
      self.num = self.num*-1
      self.den = self.den*-1 
    return(self)

  def invert(self):
    return(rationals(self.den,self.num).reduce())

  def __neg__(self):
    return(rationals(self.num*-1,self.den))

def continued_fraction(stuff):
  stuff.reverse()
  end = rationals(stuff.pop(0),1)
  for i in stuff:
    end = i+1/end
  return(end)
  

def golden_ratio(depth):
  ratio = rationals(1,1)
  ratios = {}
  for i in range(depth-1):
    ratio = 1+1/ratio
    ratios[i]=ratio
  return(ratio)
    
    

def main():
  stuff = [3,7,15,1,292,1,1,1,2,1,3,1,14,2,1,1,2,2,2,2]
  print((float(continued_fraction(stuff))-math.pi))
main()