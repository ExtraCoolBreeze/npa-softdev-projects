
#set and initialise loop
loop = 1

#start while loop, get user inputs, check if inputs are within correct range, if yes break loop, if not print response
while loop==1:
    courseworkMark = int(input("Enter coursework mark within range 0 - 60:"))
    if courseworkMark >= 0 and courseworkMark <= 60:
        prelimMark = int(input("Enter prelim mark within range 0 - 90:"))
        if prelimMark >= 0 and prelimMark <= 90:
            break
        else: 
            print ("Please enter a prelim mark within range 0 - 90:")
    else:
        print ("Please enter a prelim mark within range 0 - 60:")

#defining a seperate function for calculating the students grade
#passing in the user inputs, courseworkMark and PrelimMark and performing calculations, setting variables and returning the value

def find_grade(courseworkMark, prelimMark):
        Grade = ((courseworkMark + prelimMark) *100) / 150
        if Grade >= 70:
            result="A"
        elif Grade >= 60 and Grade <= 69:
            result="B"
        elif Grade >=50 and Grade <=59:
            result="C"
        elif Grade >=45 and Grade <=49:
            result="D"
        else: result="No grade"
        return result

#printing the results of the find_grade function by calling the above function
print (find_grade(courseworkMark, prelimMark))

#setting the percent variable with formatting, performing a calculation and then printing the student mark as a percentage.
Percent = "Percentage {:.0f} %"
Grade = ((courseworkMark + prelimMark) *100) / 150
print (Percent.format(Grade))