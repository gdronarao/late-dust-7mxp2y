weight = input("weight:")
unit = input("(k)g or (l)bs: ")
if unit.upper() == "k":
converted = weight / 0.45
print("weight in (l)bs"+ converted)
else:
    converted