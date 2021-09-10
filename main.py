import pytest

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

fiveHunna = {
    'roman': 'D',
    'arabic': 500,
    'roman_subtractor': 'C',
    'arabic_subtractor': 100
  }


def convert(number):
  for key, val in Rules.items():
    if number in Rules:
      return Rules[number]
    elif number - key > 0:
      if number - arabic_subtractor > 0:
        return roman_subtractor + roman + convert(number - arabic + arabic_subtractor)
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