class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            print("not even")

        brackets = {')':'(', '}':'{', ']':'['}
        c_list = []
        for char in s:
            if char in brackets:
                if c_list and c_list[-1] ==  brackets[char]:
                    c_list.pop()
                else:
                    return False
            else:
                c_list.append(char)

        if not c_list:
            return True
        return False