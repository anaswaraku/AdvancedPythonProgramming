import datetime
def getdob(str):
    print("Enter DOB of",str," in YYYY-MM-DD format")
    date = input()
    year, month, day = map(int, date.split('-'))
    dob = datetime.date(year, month, day)
    return dob
def age(dob):
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

dob1,dob2=getdob("person1"),getdob("person2")

print("Person1 is older" if age(dob1) > age(dob2)else "Person2 is older" if age(dob2)> age(dob1) else "Both persons are of the same age")

ages=input("Do you want to know age(Y/N) ?")
if ages == "Y"or"y":
    print("Person1 =", age(dob1))
    print("Person2 =", age(dob2))
elif ages == "N"or"n":
    print("Ok, fine.")
else:
    print("Invalid Input")