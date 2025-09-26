print("Subject marks")
student_name=input("Enter student name")
student_class=input("enter student class")
names = ["Maths" , "Science" , "English" , "Urdu" , "History"]
subject_marks =[]
ch='y'
for subject in range(len(names)):
    while ch=='y' or ch=='Y':
        marks=int(input(f"Enter marks for {subject}"))
        if 0<= marks <=100:
            names.append(subject_marks)
            break
        else:
            print("Invalid input")
        user=int(input("press 1 if you want to continue"))
#         if user==1:
#             continue
#         else:
#             break
        ch=input("Enter y to continue:")
total=sum of names
percentage= (total/500)*100
if percentage >=90:
    print("A+ grade")
elif percentage >=80:
    print("A grade")
elif percentage >=70:
    print("B grade")
elif percentage >=60:
    print("C grade")
else:
    print("Fail")
    
print(f"marks: {marks}")
print(f"total: {total}")
print(f"percentage: {percentage}")
    



    