unit= input("what is the unit of measurement? (C or F)?")
temp= float(input("what is the temperature?"))
if unit == "C":
    temp= round((temp * 9) /5 + 32,1)
    print(f'the temperature is {temp}<UNK>f')
elif unit == "F":
    temp= round((temp -32) * 5 / 9,1)
    print(f'the temperature is {temp}<UNK>c')
else:
    print("invalid unit")
