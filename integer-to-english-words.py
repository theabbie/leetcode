class Solution:
    def threeDigit(self, num):
        res = []
        for x in [2, 1, 0]:
            pw = 10 ** x
            if num // pw:
                if x == 2:
                    res.append(f"{self.ones[num // pw]} hundred")
                if x == 1:
                    if num // pw == 1:
                        res.append(self.tenToNineteen[num % pw])
                        break
                    else:
                        res.append(self.hundreds[num // pw])
                if x == 0:
                    res.append(self.ones[num // pw])
            num -= pw * (num // pw)
        return " ".join(res)
    
    def numberToWords(self, num: int) -> str:
        self.hundreds = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.tenToNineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        self.ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        capitalize = lambda s: " ".join(w[0].upper() + w[1:] for w in s.split())
        res = []
        for x in [9, 6, 3, 0]:
            pw = 10 ** x
            if num // pw:
                if x == 9:
                    res.append(f"{self.threeDigit(num // pw)} billion")
                if x == 6:
                    res.append(f"{self.threeDigit(num // pw)} million")
                if x == 3:
                    res.append(f"{self.threeDigit(num // pw)} thousand")
                if x == 0:
                    res.append(f"{self.threeDigit(num // pw)}")
            num -= pw * (num // pw)
        return capitalize(" ".join(res) or "zero")