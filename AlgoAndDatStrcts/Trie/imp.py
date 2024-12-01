print("shitty calculator")
bill = float(input("what total bill bitch "))
tip = float(input("tip "))
tip = tip * 0.01
people = float(input("people "))
total= (bill+(bill*tip))/people
total = round(total, 2)
print("total is " + str(total))