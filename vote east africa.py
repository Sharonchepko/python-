countries=["Kenya,Uganda,Tanzania"]
citizenship=input("enter citizenship:")
age=int(input("enter age:"))
if(citizenship not in "countries")and(age>18):
    print("elligible to vote")
else:
        print("not elligible to vote")
