class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCount = Counter(students)

        for s in sandwiches:
            if studentCount[s] > 0 :
                studentCount[s] -= 1
            else:
                return sum(studentCount.values())
        
        return 0