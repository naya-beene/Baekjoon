students = [i for i in range(1, 31)] 

for _ in range(28): 
    student_num = int(input())
    students.remove(student_num) #소거
    
print(min(students))
print(max(students))