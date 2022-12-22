from getpass import getpass
from prettytable import PrettyTable
import re
import csv

def Print_Invalid_Input():
    Print_String_With_Format("Invalid Input")
    return

def Print_String_With_Format(string):
    # Prints strings with the PrettyTable format
    format = PrettyTable()
    format.header = False
    format.add_row([string])
    print(format)
    return

def Search(searchKey, index):
    searchResult = PrettyTable()
    resultCount = list()
    with open('StudentProfile.csv', 'r') as studentFile:
        studentFileReader = csv.reader(studentFile)
        for row in studentFileReader:
            if studentFileReader.line_num == 1:
                searchResult.field_names = row
            elif studentFileReader.line_num != 1:
                if re.search(searchKey, row[index], re.IGNORECASE):
                    searchResult.add_row(row)     
                    resultCount.append(row)  
    if len(resultCount) != 0: 
        print(searchResult)
    else: 
        Print_String_With_Format("No Results")
    return 

def Search_Again():
    invalidInput = True
    while invalidInput:
        print("+---------------+")
        print("| Search Again? |")
        print("+-----------+---+")
        print("|     Yes   | Y |")
        print("+-----------+---+")
        print("|     No    | N |")
        print("+-----------+---+")
        match input("Input: "):
            case 'y' | 'Y':
                Search_Menu()
            case 'n' | 'N':
                Main_Menu()
            case _:
                Print_Invalid_Input()

def Print_Student_Header():
    print("+----------------------+---+----------------------+---+----------------------+---+")
    print("|       First Name     | A |       Middle Name    | B |        Last Name     | C |")
    print("+----------------------+---+----------------------+---+----------------------+---+")
    print("|       Birthdate      | D |          Sex         | E |        Course        | F |")
    print("+----------------------+---+----------------------+---+----------------------+---+")
    print("|       Semester       | G |   Enrollment Status  | H |          ID          | I |")
    print("+----------------------+---+----------------------+---+----------------------+---+")

def Birthdate_Input():
    correctDate = False
    while not correctDate:
        userBirthdate = input("Please insert birthdate (mm/dd/yyyy): ")
        #Checks whether the input is the correct date format
        if re.match('^[0-1]{1}[0-9]{1}/[1-3]{1}[0-9]{1}/[0-9]{4}$', userBirthdate):
            correctDate = True
        else:
            Print_String_With_Format("Incorrect formatting please try again")
            correctDate = False
    return userBirthdate
        
def Sex_Input():
    invalidSex = True
    while invalidSex:
        print("+----------------+")
        print("|      Sex       |")
        print("+----------------+")
        print("|    Male    | M |")
        print("+------------+---+")
        print("|   Female   | F |")
        print("+----------------+")
        match input("Input: "):
            case 'm' | 'M':
                invalidSex = False
                sex = "Male"
            case 'f' | 'F':
                invalidSex = False
                sex =  "Female"
            case _:
                invalidSex = True
                Print_Invalid_Input()
    return sex

def Course_Input():
    invalidCourse = True
    while invalidCourse:
        print("+----------------------------------------------------------------+")
        print("|                          Course:                               |")
        print("+----------------------------------------------------------------+")
        print("| Bachelor of Science in Computer Science (BSCS)             | A |")
        print("+------------------------------------------------------------+---+")
        print("| Bachelor of Entertainment and Multimedia Computing (BSEMC) | B |")
        print("+------------------------------------------------------------+---+")
        print("| Bachelor of Multimedia Arts (BMMA)                         | C |")
        print("+------------------------------------------------------------+---+")
        match input("Input: "):
            case 'a' | 'A':
                invalidCourse = False
                course = "BSCS"
            case 'b' | 'B':
                invalidCourse = False
                course =  "BSEMC"
            case 'c' | 'C':
                invalidCourse = False
                course = "BMMA"
            case _:
                invalidCourse = True
                Print_Invalid_Input()
    return course

def Semester_Input():
    invalidSemester = True
    while invalidSemester:
        print("+-------------------------------------+")
        print("|              Semester:              |")
        print("+-------------------------------------+")
        print("|          1st Semester           | A |")
        print("+---------------------------------+---+")
        print("|          2nd Semester           | B |")
        print("+---------------------------------+---+")
        match input("Input: "):
            case 'a' | 'A':
                invalidSemester = False
                semester = "1st Sem"
            case 'b' | 'B':
                invalidSemester = False
                semester =  "2nd Sem"
            case _:
                invalidSemester = True
                Print_Invalid_Input()
    return semester

def Enrollment_Status_Input():
    invalidStatus = False
    while invalidStatus:
        print("+-------------------------------------+")
        print("|         Enrollment Status:          |")
        print("+-------------------------------------+")
        print("|             Enrolled            | A |")
        print("+---------------------------------+---+")
        print("|           Not Enrolled          | B |")
        print("+---------------------------------+---+")
        match input("Input: "):
            case 'a' | 'A':
                invalidStatus = False
                enrollmentStatus = "Enrolled"
            case 'b' | 'B':
                invalidStatus = False
                enrollmentStatus = "Not Enrolled"
            case _:
                invalidStatus = True
                Print_Invalid_Input()
    return enrollmentStatus
        
def Search_Menu():
    invalidInput = True
    while invalidInput:
        Print_Student_Header()
        match input("Input: "):
            case 'a' | 'A':
                invalidInput = False
                Search(input("Please insert first name: "), 0)
                Search_Again()
            case 'b' | 'B':
                invalidInput = False
                Search(input("Please insert middle name: "), 1)
                Search_Again()
            case 'c' | 'C':
                invalidInput = False
                Search(input("Please insert last name: "), 2)
                Search_Again()
            case 'd' | 'D':
                invalidInput = False
                Search(Birthdate_Input(), 3)
                Search_Again()
            case 'e' | 'E':
                invalidInput = False
                Search(Sex_Input(), 4)
                Search_Again()
            case 'f' | 'F':
                invalidInput = False
                Search(Course_Input(), 5)
                Search_Again()
            case 'g' | 'G':
                invalidInput = False
                Search(Semester_Input(), 6)
                Search_Again()
            case 'h' | 'H':
                invalidInput = False
                Search(Enrollment_Status_Input(), 7)
                Search_Again()
            case 'i' | 'I':
                invalidInput = False
                Search(input("Input Student ID or Enrollment Reference Number: "), 8)
                Search_Again()
            case _:
                invalidInput = True
                Print_Invalid_Input()
                Search_Again()

def Overwrite_To_CSV(file, data):
    # Saves data by overwriting the CSV file
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    file.close()
    return

def Clear(inputFile):
    temp = list()
    with open(inputFile, 'r') as readFile:
        fileReader = csv.reader(readFile)
        for row in fileReader:
            temp.append(row)
            match inputFile:
                case 'EnrollmentReferenceNumbers.csv' | '.Backup/EnrollmentReferenceNumbers.csv':
                    temp.remove(row)
                case 'StudentProfile.csv' | '.Backup/StudentProfile.csv':
                    if fileReader.line_num != 1:
                        temp.remove(row)
    Overwrite_To_CSV(inputFile, temp)
    readFile.close()

               
def Clear_Menu():
    print("+----------------------------------------+---+")
    print("|   Clear Enrollment Reference Numbers   | A |")
    print("+----------------------------------------+---+")
    print("|        Clear Student Profile           | B |")
    print("+----------------------------------------+---+")
    print("|             Clear Backup               | C |")
    print("+----------------------------------------+---+")
    match input("Input: "):
        case 'a' | 'A':
            Clear('EnrollmentReferenceNumbers.csv')
            Main_Menu()
        case 'b' | 'B':
            Clear('StudentProfile.csv')
            Main_Menu()
        case 'c' | 'C':
            Clear('.Backup/EnrollmentReferenceNumbers.csv')
            Clear('.Backup/StudentProfile.csv')
            Main_Menu()
        case _:
            Print_Invalid_Input()

def Print_Ballpit_ASCII():
    print(r""" 
    ██████╗  █████╗ ██╗     ██╗     ██████╗ ██╗████████╗
    ██╔══██╗██╔══██╗██║     ██║     ██╔══██╗██║╚══██╔══╝
    ██████╔╝███████║██║     ██║     ██████╔╝██║   ██║   
    ██╔══██╗██╔══██║██║     ██║     ██╔═══╝ ██║   ██║   
    ██████╔╝██║  ██║███████╗███████╗██║     ██║   ██║   
    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝   ╚═╝                                                     
                    Admin Panel""")

def Login():
    adminUsername = "admin"
    adminPassword = "1234"

    Print_Ballpit_ASCII()
    usernameInput = input("Input Username: ")
    passwordInput = getpass("Input Password: ")
    if adminUsername == usernameInput and adminPassword == passwordInput:
        Main_Menu()
    else:
        Print_String_With_Format("incorrect password")
    return 

def Change_Student_Data(row, data, index, list):
    list.append(row)
    row[index] = data
    Overwrite_To_CSV('StudentProfile.csv', list)

def Main_Menu():
    invalidInput = True
    Print_Ballpit_ASCII()
    while invalidInput:
        print("+------------+---+")
        print("|   Search   | S |")
        print("+------------+---+")
        print("|   Modify   | M |")
        print("+------------+---+")
        print("|    Clear   | C |")
        print("+------------+---+")
        print("|    Quit    | Q |")
        print("+------------+---+")
        match input("Input: "):
            case 's' | 'S':
                invalidInput = False
                Search_Menu()
            case 'm' | 'M':
                invalidInput = False
                temp = list()
                inputID = input("Input Student ID or Enrollment Reference Number: ")
                with open('StudentProfile.csv', 'r') as studentFile:
                    studentFileReader = csv.reader(studentFile)
                    for row in studentFileReader:
                        if studentFileReader.line_num == 1:
                            temp.append(row)
                        if row[8] == inputID:
                            Search(inputID, 8)
                            Print_String_With_Format("Select data to change:")
                            Print_Student_Header()
                            match input("Input: "):
                                case 'a' | 'A':
                                    newData = input("Input new first name: ")
                                    Change_Student_Data(row, newData, 0, temp)
                                case 'b' | 'B':
                                    newData = input("Input new middle name: ")
                                    Change_Student_Data(row, newData, 1, temp)
                                case 'c' | 'C':
                                    newData = input("Input new last name: ")
                                    Change_Student_Data(row, newData, 2, temp)
                                case 'd' | 'D':
                                    Change_Student_Data(row, Birthdate_Input(), 3, temp)
                                case 'e' | 'E':
                                    Change_Student_Data(row, Sex_Input(), 4, temp)
                                case 'f' | 'F':
                                    Change_Student_Data(row, Course_Input(), 5, temp)
                                case 'g' | 'G':
                                    Change_Student_Data(row, Semester_Input(), 6, temp)
                                case 'h' | 'H':
                                    Change_Student_Data(row, Enrollment_Status_Input(), 7, temp)
                                case 'i' | 'I':
                                    pass
                                case _:
                                    invalidInput = True
                                    Print_Invalid_Input()              
            case 'c' | 'C':
                invalidInput = False
                Clear_Menu()
            case 'q' | 'Q':
                quit()
            case _:
                invalidInput = True
                Main_Menu()
                Print_Invalid_Input()

Login()