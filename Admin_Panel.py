from getpass import getpass
from prettytable import PrettyTable
import re
import csv
import ctypes
import shutil
import os

firststSemesterCSV = '1stSemesterSubjects.csv'
secondSemesterCSV = '2ndSemesterSubjects.csv'
enrollmentReferenceCSV = 'EnrollmentReferenceNumbers.csv'
studentProfileCSV = 'StudentProfile.csv'
adminPanelScript = 'Admin_Panel.py'

def Backup(file = None):
    # Backs up every CSV file to a hidden backup folder
    match file:
        case '1stSemesterSubjects.csv':
            shutil.copy(firststSemesterCSV, '.Backup')
        case '2ndSemesterSubjects.csv':
            shutil.copy(secondSemesterCSV, '.Backup')
        case 'EnrollmentReferenceNumbers.csv':
            shutil.copy(enrollmentReferenceCSV, '.Backup')
        case 'StudentProfile.csv':
            shutil.copy(studentProfileCSV, '.Backup')
        case 'Admin_Panel.py':
            shutil.copy(adminPanelScript, '.Backup')
        case _:
            shutil.copy(firststSemesterCSV, '.Backup')
            shutil.copy(secondSemesterCSV, '.Backup')
            shutil.copy(enrollmentReferenceCSV, '.Backup')
            shutil.copy(studentProfileCSV, '.Backup')
            shutil.copy(adminPanelScript, '.Backup')
    return

def Recover(file = None):
    # Recovers CSV files from the hidden backup folder
    match file:
        case 'EnrollmentReferenceNumbers.csv':
            shutil.copy('.Backup/' + enrollmentReferenceCSV, os.getcwd())
        case 'StudentProfile.csv':
            shutil.copy('.Backup/' + studentProfileCSV, os.getcwd())
        case _:
            shutil.copy('.Backup/' + enrollmentReferenceCSV, os.getcwd())
            shutil.copy('.Backup/' + studentProfileCSV, os.getcwd())
    return

def File_Check_And_Recover(file):
    # Checks whether a file exist in the main directory if not it will check 
    # the hidden backup folder for the file if available it will restore 
    # the file to the main directory
    studentProfileHeader = ["First Name", "Middle Name", "Last Name", "Birthdate", "Sex", "Course", "Semester", "Enrollment status", "ID"]
    if not os.path.isfile(file):
        if not os.path.isfile('.Backup/' + file):
            open(file, 'a')
            if file == studentProfileCSV:
                Save_To_CSV(file, studentProfileHeader)
            Backup(file)
        else:
             Recover(file)
    return

def Save_To_CSV(CSVfile, data):
    # Saves data to a CSV file by appending
    with open(CSVfile, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    file.close()
    return

def Overwrite_To_CSV(file, data):
    # Saves data by overwriting the CSV file
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    file.close()
    return

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
    # Searches specific details in StudentProfile.CSV 
    searchResult = PrettyTable()
    resultCount = list()
    with open(studentProfileCSV, 'r') as studentFile:
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
        if not Back_To_Main_Menu():
            Search_Menu()
    return 

def Print_Student_Header():
    print("+----------------------+---+----------------------+---+----------------------+---+")
    print("|       First Name     | A |       Middle Name    | B |        Last Name     | C |")
    print("+----------------------+---+----------------------+---+----------------------+---+")
    print("|       Birthdate      | D |          Sex         | E |        Course        | F |")
    print("+----------------------+---+----------------------+---+----------------------+---+")
    print("|       Semester       | G |   Enrollment Status  | H |          ID          | I |")
    print("+----------------------+---+----------------------+---+----------------------+---+")
    print("                           |   Back to Main Menu  | J |                          |")
    print("                           +----------------------+---+                           ")
    return

def Back_To_Main_Menu():
    invalidInput = True
    while invalidInput:
        print("+--------------------+")
        print("| Back to Main Menu? |")
        print("+----------------+---+")
        print("|       Yes      | Y |")
        print("+----------------+---+")
        print("|       No       | N |")
        print("+----------------+---+")
        match input("Input: "):
            case 'y' | 'Y':
                invalidInput = False
                Main_Menu()
            case 'n' | 'N':
                invalidInput = False
                backToMainMenu = False
            case _:
                invalidInput = True
                Print_Invalid_Input()
    return backToMainMenu

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
        
def ID_Input():
    invalidFormat = True
    while invalidFormat:
        idInput = input("Input Student ID or Enrollment Reference Number: ")
        # Checks whether the input format is correct
        if re.match('^[0-9]{2}-[0-9]{4}$', idInput) or re.match('^[a-zA-Z]{8}$', idInput):
            invalidFormat = False
            id = idInput
        else:
            invalidFormat = True
            Print_String_With_Format("Invalid Format")
    return id

def Search_Menu():
    invalidInput = True
    while invalidInput:
        Print_Student_Header()
        match input("Input: "):
            case 'a' | 'A':
                invalidInput = False
                Search(input("Please insert first name: "), 0)
            case 'b' | 'B':
                invalidInput = False
                Search(input("Please insert middle name: "), 1)
            case 'c' | 'C':
                invalidInput = False
                Search(input("Please insert last name: "), 2)
            case 'd' | 'D':
                invalidInput = False
                Search(Birthdate_Input(), 3)
            case 'e' | 'E':
                invalidInput = False
                Search(Sex_Input(), 4)
            case 'f' | 'F':
                invalidInput = False
                Search(Course_Input(), 5)
            case 'g' | 'G':
                invalidInput = False
                Search(Semester_Input(), 6)                
            case 'h' | 'H':
                invalidInput = False
                Search(Enrollment_Status_Input(), 7)                
            case 'i' | 'I':
                invalidInput = False
                Search(ID_Input(), 8)    
            case 'j' | 'J':            
                Main_Menu()
            case _:
                invalidInput = True
                Print_Invalid_Input()                
    if not Back_To_Main_Menu():
        Search_Menu()
    return

def Clear(inputFile):
    # Clears the details of a whole file if the said file is StudentProfile.CSV
    # it will retain the header details
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
    Print_String_With_Format("Succesfully Cleared")
    readFile.close()
    return

               
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
            if Login():
                Clear(enrollmentReferenceCSV)
            if not Back_To_Main_Menu():
                Clear_Menu()
        case 'b' | 'B':
            if Login():
                Clear(studentProfileCSV)
            if not Back_To_Main_Menu():
                Clear_Menu()
        case 'c' | 'C':
            if Login():
                Clear('.Backup/EnrollmentReferenceNumbers.csv')
                Clear('.Backup/StudentProfile.csv')
            if not Back_To_Main_Menu():
                Clear_Menu()
        case _:
            Print_Invalid_Input()
    return

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
    successfulLogin = False
    adminUsername = "admin"
    adminPassword = "1234"
    
    while not successfulLogin:
        usernameInput = input("Input Username: ")
        passwordInput = getpass("Input Password: ")
        if adminUsername == usernameInput and adminPassword == passwordInput:
            successfulLogin = True
        else:
            successfulLogin = False
            Print_String_With_Format("incorrect password")
    return successfulLogin

def Change_Student_Data(row, data, index, list):
    # Modifies a detail from the given student profile
    list.append(row)
    row[index] = data
    Overwrite_To_CSV(studentProfileCSV, list)
    Backup(studentProfileCSV)
    Print_String_With_Format("Sucessfully Modified")
    return

def Modify_Menu():
    temp = list()
    inputID = ID_Input()
    invalidInput = True
    with open(studentProfileCSV, 'r') as studentFile:
        studentFileReader = csv.reader(studentFile)
        for row in studentFileReader:
            if studentFileReader.line_num == 1:
                temp.append(row)
            if row[8] == inputID:
                invalidID = False
                Search(inputID, 8)
                while invalidInput:
                    Print_String_With_Format("Select data to change:")
                    Print_Student_Header()
                    match input("Input: "):
                        case 'a' | 'A':
                            invalidInput = False
                            newData = input("Input new first name: ")
                            Change_Student_Data(row, newData, 0, temp)
                        case 'b' | 'B':
                            invalidInput = False
                            newData = input("Input new middle name: ")
                            Change_Student_Data(row, newData, 1, temp)
                        case 'c' | 'C':
                            invalidInput = False
                            newData = input("Input new last name: ")
                            Change_Student_Data(row, newData, 2, temp)
                        case 'd' | 'D':
                            invalidInput = False
                            Change_Student_Data(row, Birthdate_Input(), 3, temp)
                        case 'e' | 'E':
                            invalidInput = False
                            Change_Student_Data(row, Sex_Input(), 4, temp)
                        case 'f' | 'F':
                            invalidInput = False
                            Change_Student_Data(row, Course_Input(), 5, temp)
                        case 'g' | 'G':
                            invalidInput = False
                            Change_Student_Data(row, Semester_Input(), 6, temp)
                        case 'h' | 'H':
                            invalidInput = False
                            Change_Student_Data(row, Enrollment_Status_Input(), 7, temp)
                        case 'i' | 'I':
                            invalidInput = False
                            Change_Student_Data(row, ID_Input(), 8, temp)
                        case 'j' | 'J':            
                            Main_Menu()
                        case _:
                            invalidInput = True
                            Print_Invalid_Input() 
                break 
            else:
                invalidID = True 
        if invalidID:
            Print_String_With_Format("ID not found")
        if not Back_To_Main_Menu():
            Modify_Menu()  
    studentFile.close()
    return

def Delete_Student():
    temp = list()
    inputID = ID_Input()
    with open(studentProfileCSV, 'r') as studentFile:
        studentFileReader = csv.reader(studentFile)
        for row in studentFileReader:
            temp.append(row)
            if row[8] == inputID:
                temp.remove(row)
    Overwrite_To_CSV(studentProfileCSV, temp)
    Backup(studentProfileCSV)
    Print_String_With_Format("Deleted")
    if not Back_To_Main_Menu():
        Delete_Student()
    studentFile.close()
    return

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
        print("|   Delete   | D |")
        print("+------------+---+")
        print("|    Quit    | Q |")
        print("+------------+---+")
        match input("Input: "):
            case 's' | 'S':
                invalidInput = False
                Search_Menu()
            case 'm' | 'M':
                invalidInput = False
                Modify_Menu()
            case 'c' | 'C':
                invalidInput = False
                Clear_Menu()
            case 'd' | 'D':
                invalidInput = False
                Delete_Student()
            case 'q' | 'Q':
                quit()
            case _:
                invalidInput = True
                Print_Invalid_Input()
    return

if __name__ == "__main__":
    File_Check_And_Recover(enrollmentReferenceCSV)
    File_Check_And_Recover(studentProfileCSV)

    if not os.path.isdir('.Backup'):
        os.mkdir('.Backup')
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW('.Backup', FILE_ATTRIBUTE_HIDDEN)
        Backup()

    Print_Ballpit_ASCII()
    if Login():
        Main_Menu()