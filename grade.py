print("Enter Marks Obtained in 3 Subjects: ")
sub1= int(input("enter markone"))
sub2 = int(input("enter marktwo"))
sub3 = int(input("enter mark3"))


tot = sub1+sub2+sub3
avg = tot/3
if avg>=70 and avg<=100:
    print("Your Grade is A")
elif avg>=60 and avg<69:
    print("Your Grade is B")
elif avg>=50 and avg<59:
    print("Your Grade is C")
elif avg>=40 and avg<49:
    print("Your Grade is D")
else:
    print("Fail")
