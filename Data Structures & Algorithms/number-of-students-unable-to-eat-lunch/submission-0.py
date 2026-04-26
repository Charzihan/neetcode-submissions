class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        current_rejection = 0
        while current_rejection != len(students):
            if students[0] == sandwiches[0]:
                current_rejection = 0
                del students[0]
                del sandwiches[0]
            else:
                current_rejection += 1
                students.append(students.pop(0))
    
        return current_rejection
