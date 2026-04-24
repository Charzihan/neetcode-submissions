class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            print("not even")

        c1 = '('
        c2 = ')'
        c3 = '{'
        c4 = '}'
        c5 = '['
        c6 = ']'
        c_list = []
        for char in s:
            if char == c2 and c_list and c_list[-1] == c1:
                c_list.pop()
            elif char == c4 and c_list and c_list[-1] == c3:
                c_list.pop()
            elif char == c6 and c_list and c_list[-1] == c5:
                c_list.pop()
            else:
                c_list.append(char)

        if not c_list:
            return True
        return False