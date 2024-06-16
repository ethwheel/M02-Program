d = {}
while True:
    key = input("Enter student's first and last name, or type ZZZ to end: ")
    if key == "ZZZ":
        break
    value = float(input("Enter that student's GPA: "))
    d[key] = value
    if value >= 3.5:
        d[key] + "made the Dean's List"
    



