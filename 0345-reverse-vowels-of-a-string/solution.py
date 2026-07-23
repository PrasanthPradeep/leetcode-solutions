class Solution:
    def reverseVowels(self, s: str) -> str:
        result = []
        vowel = []
        for i in s:
            if i in "aeiouAEIOU":
                vowel.append(i)
        vowel.reverse()
        j = 0
        for i in s:
            if i in "aeiouAEIOU":
                result.append(vowel[j])
                j += 1
            else:
                result.append(i)
        return "" .join(result)
