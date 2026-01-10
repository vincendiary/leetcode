class Solution:
    def romanToInt(self, s: str) -> int:
        roman2Value = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        # base case
        if len(s) == 1 and s in roman2Value:
            return roman2Value[s]

        summ = 0
        left = 0
        right = 1
        while right < len(s):
            if s[left:right] not in roman2Value:
                summ += roman2Value[s[left:right-1]]
                left = right - 1
                right -= 1
            right += 1
        summ += roman2Value[s[left:right]]

        return summ
