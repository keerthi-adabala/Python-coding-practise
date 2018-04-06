# calculate year when user turns 100
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
dob = int(input("Enter your birth year: "))
yr = int(input("Enter a future year: "))

# year = str((2018 - age)+100)
year = 2018 + (100 - age)
print("You will turn 100 in the year of :",+year)


# calculate his age given a future year
futureAge = str((yr - 2018) + age)
print("Your future age: "+futureAge)

# calculate his current age given DOB
currentAge = (2018 - dob)
print("Your current age is:",+currentAge)

# display life timetable by means of 16 years schooling; 25 yrs graduation; 28 yrs married; 32 yrs kids; 40 yrs business; 60 yrs retirement
print("Year You should finish your schooling: "+str(dob + 16))
print("Year You should finish your graduation and start a job: "+str(dob + 25))
print("Year You should get married: "+str(dob + 28))
print("Year You should have kids: "+str(dob + 32))
print("Year You can start your business: "+str(dob + 40))
print("Year You should retire: "+str(dob + 60))
