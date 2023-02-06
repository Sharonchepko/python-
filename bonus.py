sal=int(input("enter amount of salary:"))
yrs=int(input("enter years of service:"))
if(yrs>10):
    print(("Netbonus"),sal+(sal*0.1))
elif((yrs>=6)and(yrs<=10)):
    print(("Netbonus"),sal+(sal*0.08))
else:
    print(("NetbonuS"),sal+(sal*0.05))
