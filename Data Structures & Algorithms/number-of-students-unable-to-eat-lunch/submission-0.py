class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCount = Counter(students)

        for s in sandwiches:
            if s in studentCount:
                studentCount[s] -= 1
                if studentCount[s] == 0:
                    del studentCount[s]
            else:
                return sum(studentCount.values())
        
        return 0