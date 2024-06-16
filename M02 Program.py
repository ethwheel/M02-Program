deanList = []
honorList = []
while True:
    name = input("Enter student's first and last name, or type ZZZ to end: ")
    if name == "ZZZ":
        break
    value = float(input("Enter that student's GPA: "))
    if value >= 2.5:
        honorList += name
    elif value >= 3.5:
        deanList += name
    
print(honorList)
print(deanList)
    



