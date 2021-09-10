import unittest

#  The Romans wrote numbers using letters - I, V, X, L, C, D, M.
#  (notice these letters have lots of straight lines
#  and are hence easy to hack into stone tablets)
#
#  The Kata says you should write a function to
#  convert from normal numbers to Roman Numerals: eg
#
#    1 --> I
#    10 --> X
#    7 --> VII
#    etc.
#
#  I = 1 V = 5 X = 10
#  L = 50 C = 100
#  D = 500 M = 1000
#
#  There is no need to be able to convert numbers larger
#  than about 3000. (The Romans themselves didn't tend to go any higher)
#
# Note that you can't write numerals like "IM" for 999. Wikipedia says:
# Modern Roman numerals are written by expressing each digit
# separately starting with the left most digit and skipping any digit
# with a value of zero. To see this in practice, consider the example
# of 1990. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC;
# resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII.

Conversions = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
  }


def convert(number):
  for key, val in Conversions.items():
    if number in Conversions:
      return Conversions[number]
    elif number - key > 0:
      return val + convert(number - key)

    
class Tests(unittest.TestCase):
  def test_convert1(self):
    self.assertEqual("I", convert(1))
  def test_convert5(self):
    self.assertEqual("V", convert(5))
  def test_convert10(self):
    self.assertEqual("X", convert(10))
  def test_convert50(self):
    self.assertEqual("L", convert(50))
  def test_convert100(self):
    self.assertEqual("C", convert(100))
  def test_convert500(self):
    self.assertEqual("D", convert(500))
  def test_convert1000(self):
    self.assertEqual("M", convert(1000))
  def test_convert6(self):
    self.assertEqual("VI", convert(6))
  def test_convert4(self):
    self.assertEqual("IV", convert(4))
  def test_convert3(self):
    self.assertEqual("III", convert(3))
  def test_convert1990(self):
    self.assertEqual("MCMXC", convert(1990))
  def test_convert2008(self):
    self.assertEqual("MMVIII", convert(2008))

    
unittest.main()
