import pytest

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

Rules = {
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
  for key, val in Rules.items():
    if number in Rules:
      return Rules[number]
    elif number - key > 0:
      return val + convert(number - key)

  
@pytest.mark.parametrize("arabic,roman", [
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (9, 'IX'),
    (10, 'X'),
    (16, 'XVI'),
    (20, 'XX'),
    (40, 'XL'),
    (50, 'L'),
    (90, 'XC'),
    (100, 'C'),
    (400, 'CD'),
    (500, 'D'),
    (900, 'CM'),
    (1000, 'M')
  ]
)
def test_arabic_to_roman_conversion(arabic, roman):
  assert convert(arabic) == roman
