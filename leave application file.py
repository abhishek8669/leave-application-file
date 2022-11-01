import calendar
from datetime import datetime

try:
    year = 2022
    Student Name = input("\nEnter your name :")
    Teachers Name = input("\nEnter your teachers name :")
    gettingMonth=int(input("\nEnter the Month : "))
    print("\n", calendar,month(year , gettingMonth))
    Date=input("\n select the date : ")
    DAte of application= datetime.today()
    leaveTenture = int(input("\nleave tenure (in days only :"))
    className = input("\nDepartment Name :")
    Department = input("\nEnter the subject line :")
    Subjectline = input("\nEnter the subject line :")
    Reason =str(input("\nReason of leave :"))
    print("\nApplication submitted sucessfully.")

    print("\n\ndetails is as per application -")
    print("\n\tApplicsnt Name =",StudentName)
    print("\tAuthorised teacher =",TeacherName)
    print("\tDate of Application=",DateofApplication)
    print("\tApllication submission time =",datetime.now()
    print("\trequested tenture leave =",leaveTenture)
    print("\tClass of the applicant =",ClassName)
    print("\tDepartmentof the candidate =",Department)

    except:
        print("unknown Error ocures")