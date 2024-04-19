class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
        number = roman_numbers[s[0]]
        sum = 0
        for x in s:
            if(number < roman_numbers[x]):
                sum += roman_numbers[x] - (number * 2)
            else:
                sum += roman_numbers[x]
            number = roman_numbers[x]
        return sum