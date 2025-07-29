class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle_students = 0
        square_students = 0

        for s in students:
            if s == 0:
                circle_students += 1
            else:
                square_students += 1
        
        for n in range(len(sandwiches)):
            if sandwiches[n] == 0 and circle_students == 0:
                return square_students
            
            if sandwiches[n] == 1 and square_students == 0:
                return circle_students

            if sandwiches[n] == 0:
                circle_students -= 1
            else:
                square_students -= 1
        
        return 0