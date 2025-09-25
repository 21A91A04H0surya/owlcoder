class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ct=0
        n=len(sandwiches)
        while True:
            ct+=1
            i=0
            if len(sandwiches)==0 or ct>=n*n:
                return len(sandwiches)
            
            elif students[i]==sandwiches[i]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students[0])
                students.pop(0)
                print(students)
        


        