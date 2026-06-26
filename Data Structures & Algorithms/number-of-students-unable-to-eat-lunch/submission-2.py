class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCount = Counter(students)
        numStudents = len(students)

        for s in sandwiches:
            if studentCount[s] > 0 :
                studentCount[s] -= 1
                numStudents -= 1
            else:
                return numStudents
        
        return 0