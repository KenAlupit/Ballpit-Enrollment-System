from prettytable import PrettyTable
import subprocess
import ctypes
import os
import csv
import re
import shutil
import random
import string

firststSemesterCSV = '1stSemesterSubjects.csv'
secondSemesterCSV = '2ndSemesterSubjects.csv'
enrollmentReferenceCSV = 'EnrollmentReferenceNumbers.csv'
studentProfileCSV = 'StudentProfile.csv'
adminPanelScript = 'Admin_Panel.py'

def Reference_Number_Generator():
    # Creates a random enrollment reference number
    randomReference = ''.join(random.choices(string.ascii_letters, k=8))
    with open(enrollmentReferenceCSV, 'r') as enrollmentFile:
        enrollmentFileReader = csv.reader(enrollmentFile)
        for row in enrollmentFileReader:
            if sum(1 for row in enrollmentFileReader) > 0:
                if randomReference == row[1]:
                    randomReference = ''.join(random.choices(string.ascii_letters, k=8))
    enrollmentFile.close()
    return randomReference

def ID_Number_Generator():
    # Creates a random ID number
    randomID = ''.join(random.choices(string.digits, k=2)) + "-" + ''.join(random.choices(string.digits, k=4))
    with open(studentProfileCSV, 'r') as studentFile:
        studentFileReader = csv.reader(studentFile)
        for row in studentFileReader:
             if sum(1 for row in studentFileReader) > 0:
                if randomID == row[8]:
                    randomID = ''.join(random.choices(string.digits, k=2)) + "-" + ''.join(random.choices(string.digits, k=4))
    studentFile.close()
    return randomID

def Search_Subjects(file, course):
    # Searches the subject file for the right subjects for the given course
    # it then returns the total tuition fee for all the subjects
    with open(file, 'r') as semesterFile:
        semesterFileReader = csv.reader(semesterFile)
        totalTuition = 0
        for row in semesterFileReader:
            if row[1] == "General" or row[1] == course:
                totalTuition += int(row[3])
        if totalTuition > 0:
            Print_Subjects(file, course)
        else:
            Print_String_With_Format("Subject file empty please fill up the subejct file")
    semesterFile.close()
    return totalTuition

def Semester_Picker(course, semester):
    # Picks the right semester then prints and returns the total tuition fee
    match semester:
        case "1st Sem":
            tuitionFee = Search_Subjects(firststSemesterCSV, course)
        case "2nd Sem":
            tuitionFee = Search_Subjects(secondSemesterCSV, course)
    return tuitionFee


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
        case '1stSemesterSubjects.csv':
            shutil.copy('.Backup/' + firststSemesterCSV, os.getcwd())
        case '2ndSemesterSubjects.csv':
            shutil.copy('.Backup/' + secondSemesterCSV, os.getcwd())
        case 'EnrollmentReferenceNumbers.csv':
            shutil.copy('.Backup/' + enrollmentReferenceCSV, os.getcwd())
        case 'StudentProfile.csv':
            shutil.copy('.Backup/' + studentProfileCSV, os.getcwd())
        case 'Admin_Panel.py':
            shutil.copy('.Backup/' + adminPanelScript, os.getcwd())
        case _:
            shutil.copy('.Backup/' + firststSemesterCSV, os.getcwd())
            shutil.copy('.Backup/' + secondSemesterCSV, os.getcwd())
            shutil.copy('.Backup/' + enrollmentReferenceCSV, os.getcwd())
            shutil.copy('.Backup/' + studentProfileCSV, os.getcwd())
            shutil.copy('.Backup/' + adminPanelScript, os.getcwd())
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

def Payment(reference):
    invalidPayment = True
    with open(enrollmentReferenceCSV, 'r') as enrollmentFile:
        enrollmentFileReader = csv.reader(enrollmentFile)
        for row in enrollmentFileReader:
            if reference == row[0]:
                while invalidPayment:
                    userPayment = input("Input your payment: ") 
                    if userPayment.isdigit():
                        invalidPayment = False
                        print("hello")
                        userPayment = int(userPayment)
                        if userPayment < int(row[1]):
                            invalidPayment = True
                            Print_String_With_Format("Payment error! Your payment is insufficient!")     
                        elif userPayment > int(row[1]):
                            invalidPayment = False
                            Print_String_With_Format("Payment Successful! Here is your change: " + str(userPayment - int(row[1])))                            
                        else:
                            invalidPayment = False
                            Print_String_With_Format("Payment Successful!")  
                    else:
                        Print_String_With_Format("Please input a number")       
                        if not Back_To_Main_Menu(2):
                            invalidPayment = True
    enrollmentFile.close()
    return not invalidPayment 

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

def Back_To_Main_Menu(type):
    invalidInput = True
    match type:
        case 1:
            while invalidInput:
                print("+-------------------+---+")
                print("| Back to main menu | B |")
                print("+-------------------+---+")
                match input("Input: "):
                    case 'b' | 'B':
                        invalidInput = False
                        Main_Menu()
                    case _:
                        invalidInput = True
                        Print_Invalid_Input()

        case 2:
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

def Print_Subjects(file, course):
    # Prints the subjects of a given course using PrettyTable
    table = PrettyTable()
    totalUnits = 0
    totalTuition = 0
    with open(file, 'r') as subjectFile:
        subjectFileReader = csv.reader(subjectFile)
        for row in subjectFileReader:
            if subjectFileReader.line_num == 1:
                table.field_names = [row[0], row[2], row[3]]
            if row[1] == "General" or row[1] == course:
                table.add_row([row[0], row[2], row[3]])
                totalUnits += float(row[2])
                totalTuition += int(row[3])
    table.add_row(["Total:", totalUnits, totalTuition])
    print(table)
    subjectFile.close()
    return

def Print_String_With_Format(string):
    # Prints strings with the PrettyTable format
    format = PrettyTable()
    format.header = False
    format.add_row([string])
    print(format)
    return

def Main_Menu():
    studentProfile = []
    correctDate = False
    invalidInput = True
    invalidGender = True
    invalidCourse = True
    invalidSemester = True

    print(r""" 
██████╗  █████╗ ██╗     ██╗     ██████╗ ██╗████████╗
██╔══██╗██╔══██╗██║     ██║     ██╔══██╗██║╚══██╔══╝
██████╔╝███████║██║     ██║     ██████╔╝██║   ██║   
██╔══██╗██╔══██║██║     ██║     ██╔═══╝ ██║   ██║   
██████╔╝██║  ██║███████╗███████╗██║     ██║   ██║   
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝   ╚═╝                                                     
                Enrollment System""")
    while invalidInput:
        print("+----------------+")
        print("| Enrollment | E |")
        print("+----------------+")
        print("|  Payment   | P |")
        print("+----------------+")
        print("|   Search   | S |")
        print("+----------------+")
        match input("Input: "):
            case 'e' | 'E':
                invalidInput = False
                studentProfile.append(input("First Name: "))
                userMiddleName = input("Middle Name (0 if not applicable): ")
                if userMiddleName != "0":
                    studentProfile.append(userMiddleName)
                else:
                    studentProfile.append("N/A")
                studentProfile.append(input("Last Name: "))
                while not correctDate:
                    userBirthdate = input("Birthdate (mm/dd/yyyy): ")
                    #Checks whether the input is the correct date format
                    if re.match('^[0-1]{1}[0-9]{1}/[1-3]{1}[0-9]{1}/[0-9]{4}$', userBirthdate):
                        studentProfile.append(userBirthdate)
                        correctDate = True
                    else:
                        Print_String_With_Format("Incorrect formatting please try again")
                        correctDate = False

                while invalidGender:
                    print("+----------------+")
                    print("|      Sex       |")
                    print("+----------------+")
                    print("|    Male    | M |")
                    print("+------------+---+")
                    print("|   Female   | F |")
                    print("+----------------+")
                    match input("Input: "):
                        case 'm' | 'M':
                            invalidGender = False
                            studentProfile.append("Male")
                        case 'f' | 'F':
                            invalidGender = False
                            studentProfile.append("Female")
                        case _:
                            invalidGender = True
                            Print_Invalid_Input()
                
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
                            studentProfile.append("BSCS")
                        case 'b' | 'B':
                            invalidCourse = False
                            studentProfile.append("BSEMC")
                        case 'c' | 'C':
                            invalidCourse = False
                            studentProfile.append("BMMA")
                        case _:
                            invalidCourse = True
                            Print_Invalid_Input()

                while invalidSemester:
                    print("+-------------------------------------+")
                    print("| What semester are you enrolling in? |")
                    print("+-------------------------------------+")
                    print("|          1st Semester           | A |")
                    print("+---------------------------------+---+")
                    print("|          2nd Semester           | B |")
                    print("+---------------------------------+---+")
                    match input("Input: "):
                        case 'a' | 'A':
                            invalidSemester = False
                            studentProfile.append("1st Sem")
                        case 'b' | 'B':
                            invalidSemester = False
                            studentProfile.append("2nd Sem")
                        case _:
                            invalidSemester = True
                            Print_Invalid_Input()
                tuitionFee = Semester_Picker(studentProfile[5], studentProfile[6])
                if tuitionFee > 0:
                    Print_String_With_Format("Total tuiton fee: " + str(tuitionFee))
                    enrollmentReferenceNumber = [Reference_Number_Generator(), tuitionFee]
                    studentProfile.append("Not Enrolled")
                    studentProfile.append(enrollmentReferenceNumber[0])
                    Print_String_With_Format("Your enrollment reference number to be presented for the payment: " + enrollmentReferenceNumber[0])
                    Save_To_CSV(enrollmentReferenceCSV, enrollmentReferenceNumber)
                    Recover(studentProfileCSV) # Recovers the StudentProfile.csv file before saving to ensure the data is complete
                    Save_To_CSV(studentProfileCSV, studentProfile)
                    Backup()
                Back_To_Main_Menu(1)
                
            case 'p' | 'P':
                invalidInput = False
                invalidReference = True
                with open(enrollmentReferenceCSV, 'r') as file:
                    reader = csv.reader(file)
                    if sum(1 for row in reader) == 0:
                        Print_String_With_Format("Data unavailable! Please enroll first")
                        Back_To_Main_Menu(1)
                    else:
                        while invalidReference:
                            userReference = (input("Input your reference number: "))
                            with open(enrollmentReferenceCSV, 'r') as enrollFile, open(studentProfileCSV, 'r') as studentFile:
                                enrollReader = csv.reader(enrollFile)
                                studentReader = csv.reader(studentFile)
                                for row in enrollReader:                  
                                    if row[0] == userReference: 
                                        invalidReference = False
                                        for row in studentReader:                  
                                            if row[8] == userReference:
                                                if row[1] != "N/A":
                                                    Print_String_With_Format ("Student Name: " + row[0] + " " + row[1] + " " + row[2])
                                                else:
                                                    Print_String_With_Format ("Student Name: " + row[0] + " " + row[2])
                                                tuitionFee = Semester_Picker(row[5], row[6])
                                                Print_String_With_Format("Total tuiton fee: " + str(tuitionFee))
                                                enrollFile.close()
                                                studentFile.close()

                                                if Payment(userReference):
                                                    Print_String_With_Format("You are now succesfully enrolled!")
                                                    userId = ID_Number_Generator()
                                                    Print_String_With_Format("Your student ID: " + userId)
                                                    lines = list()
                                                    with open(enrollmentReferenceCSV, 'r') as enrollFile, open(studentProfileCSV, 'r') as studentFile:
                                                        studentFilereader = csv.reader(studentFile)
                                                        enrollFilereader = csv.reader(enrollFile)
                                                        for row in studentFilereader:
                                                            lines.append(row)
                                                            if row[8] == userReference:
                                                                row[8] = userId
                                                                row[7] = "Enrolled"
                                                        Overwrite_To_CSV(studentProfileCSV, lines)
                                                        lines = list()
                                                        for row in enrollFilereader:
                                                            lines.append(row)
                                                            if row[0] == userReference:
                                                                lines.remove(row)
                                                        Overwrite_To_CSV(enrollmentReferenceCSV, lines)
                                                        Backup()
                                                        enrollFile.close()
                                                        studentFile.close()
                                                        if not Back_To_Main_Menu(2):
                                                            invalidReference = True
                            if invalidReference:
                                Print_String_With_Format("Invalid reference number") 
                                if not Back_To_Main_Menu(2):
                                    invalidReference = True           
            case 's' | 'S':
                invalidID = True
                studentInfo = PrettyTable()
                while invalidID:
                    userID = (input("Input your ID number (xx-xxxx): "))
                    if re.match('^[0-9]{2}-[0-9]{4}$', userID):
                        with open(studentProfileCSV, 'r') as file:
                            reader = csv.reader(file)
                            for row in reader: 
                                if reader.line_num == 1:
                                    studentInfo.field_names = row
                                elif reader.line_num != 1:
                                    if row[8] == userID and row[7] == "Enrolled":
                                        invalidID = False
                                        studentInfo.add_row(row) 
                                        print(studentInfo)
                                        if not Back_To_Main_Menu(2):
                                            invalidID = True
                    if invalidID:
                        Print_String_With_Format("Invalid ID Number")
                        if not Back_To_Main_Menu(2):
                            invalidID = True
            case 'a' | 'A':
                if not os.path.isfile(adminPanelScript): 
                    if os.path.isfile('.Backup/' + file):
                        Recover(adminPanelScript)   
                        subprocess.call(adminPanelScript, shell=True)
                    else:
                        Print_String_With_Format("Admin panel not found")
                        Main_Menu()
                else:
                    subprocess.call(adminPanelScript, shell=True)
                Main_Menu()
            case _:
                invalidInput = True
                Print_Invalid_Input()
    return
if __name__ == "__main__":
    File_Check_And_Recover(studentProfileCSV)
    File_Check_And_Recover(firststSemesterCSV)
    File_Check_And_Recover(secondSemesterCSV)
    File_Check_And_Recover(enrollmentReferenceCSV)

    if not os.path.isdir('.Backup'):
        os.mkdir('.Backup')
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW('.Backup', FILE_ATTRIBUTE_HIDDEN)
        Backup()

    Main_Menu()


