class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        n = len(words)
        for i in range(n):
            if words[i][0] == '$' and words[i][1:].isnumeric():
                val = words[i][1:]
                newprice = eval(f"{val} * (1 - {discount} / 100)")
                newprice = "{:.2f}".format(newprice)
                words[i] = f"${newprice}"
        return " ".join(words)