class Solution:
    def romanToInt(self, s: str) -> int:
        hashTable = {"I" :1,
                    "V"  :5,
                    "X"  :10,
                    "L"  :50,
                    "C"  :100,
                    "D"  :500,
                    "M"  :1000}
        hashTable2 = {"V":"I",
                    "X":"I",
                    "L":"X",
                    "C":"X",
                    "D":"C",
                    "M":"C"
                    }
        i = 1
        x = hashTable[s[0]]
        while i < len(s):
            x += hashTable[s[i]]
            if (s[i] in hashTable2) and (s[i-1] == hashTable2[s[i]]):
                x -= 2 * hashTable[s[i-1]]
            i += 1
        return x
