#set and variables
gradeList=[]
namesList=[]
courseworkMarkList=[]
prelimMarkList=[]
resultList=[]

#opening file at location, the reading and splitting the contents into a list then closing the file
testFile = open("grades.txt","r")
content = testFile.read().split()

testFile.close()

#this loop goes through the list and added the names and each other student mark to individual lists
for i in range(0, len(content) -2,3):
    namesList.append(content[i])
    courseworkMarkList.append(int(content[i+1]))
    prelimMarkList.append(int(content[i+2]))
    
#declaring a function that goes through the list of marks and performs the percentage calculation.
def Calculate_Grade():  
        for i in range(len(courseworkMarkList)):
            sum = int(courseworkMarkList[i]) + int(prelimMarkList[i])
            mult = int(sum * 100)
            result = int(mult / 150)
            resultList.append(int(result))               
            
            #here we see each students percentage get checked and if they are within a certain range we
            #assign a grade and add to a list
            if result >= 70:
                gradeList.append("A")
                print("Well done " + namesList[i] + " you got an 'A'")
            elif result >= 60 and result <= 69:
                gradeList.append("B")
                print("Well done " + namesList[i] + " you got an 'B'")
            elif result >=50 and result <=59:
                gradeList.append("C")
                print("Well done " + namesList[i] + " you got an 'C'")
            elif result >=45 and result <=49:
                gradeList.append("D")
                print("Well done " + namesList[i] + " you got an 'D'")
            else:
                gradeList.append("No Award")
                print("Unfortunately " + namesList[i]+ " you failed")
        

#defining a function that, looks over a list and counts how many times it passes over the same value
#it then prints to line. It respeats this for each value
def Count_Occurrences():    
    count = 0  
    for i in gradeList:      
        if i == "A":          
            count+= 1 
    print("There are: ", count, " 'A' passes in the class.")

    count=0
    for i in gradeList:        
        if i == "B":           
            count+= 1
    print("There are: ", count, " 'B' passes in the class.")

    count=0
    for i in gradeList:     
        if i == "C":            
            count+= 1
    print("There are: ", count, " 'C' passes in the class.")

    count=0
    for i in gradeList:      
        if i == "D":             
            count+= 1 
    print("There are: ", count, " 'D' passes in the class.")

    count=0
    for i in gradeList:        
        if i =="No Award":            
            count+= 1     
    print("There are: ", count, " No Awards in the class.")

#after the percentage calculations, I assigned the results to a list. See line 26.
#defining the max check function. Defaulting the first value in the list as the highest then
#looking through the list and for each value higher than definied, it sets that to the value to check against
#then compares that to the list of names and prints to line
def max_check():
    max_val = resultList[0]
    for i in resultList:
        if i > max_val:
            max_val = i 
        maxpos = resultList.index(max(resultList))
        beststudent = namesList[maxpos]
    print("hightest score: ", max_val, " was achieved by ", beststudent)


#here I am calling all the functions above
Calculate_Grade()
max_check()
Count_Occurrences()

#here, I'm being daft
print("Craig, signing off")