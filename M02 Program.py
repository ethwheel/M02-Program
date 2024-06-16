# Ethan Wheeler
# M02 Program
# Takes student names and makes two lists featuring them if thier GPA is within either 3.25 or 3.5.


# Initializes lists
deanList = []
honorList = []

# Main loop logic, appends name if value is within range, ends loop on 'ZZZ' input
while True:
    name = input("Enter student's first and last name, or type ZZZ to end: ")
    if name == "ZZZ":
        break
    value = float(input("Enter that student's GPA: "))
    if value >= 3.25:
        honorList.append(name)
    if value >= 3.5:
        deanList.append(name)

# Displays output          
print("Honor's List: ",honorList)
print("Dean's List: ",deanList)
    



