class Solution:
    def finalString(self, s: str) -> str:
        temp = ""
        for char in s:
            if char != "i":
                temp += char
            if char == "i":
                temp = temp[::-1]
        return temp