 # shannu

student_info = {}
# calcluting grades
def calculate_grade(avg):
    if avg >= 90 and avg <101:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "FAIL !"

"""# **REMARKS FEEDBACK**
I created some block of code ( function ) to return the remarks to the student based on their grade and status

def is used to create modules in py and we can re call at any time them
"""

#generating remarks
def remarks_gen(grade, status):
    if status == "FAIL":
        return "You failed in one or more subjects. Focus more and improve."

    if grade == "A":
        return "Excellent performance! Keep it up."
    elif grade == "B":
        return "Good job! You can do even better."
    elif grade == "C":
        return "Average performance. Improve your weak subjects."
    elif grade == "D":
        return "You passed, but you need more improvement."
    else:
        return "Invalid marks."

"""# **MARKS CALCULATION AND STORING DATA** in `dict`

mark calculation done by mark_calc() ,where it caclulates total marks ,average,persentage,remarks,student status percentage,student grade etc,.

these student attributes are stored in a 'dict' *`student_info`*
"""

# mark calculation
def mark_calc(name, roll_no, branch):
    sn = int(input("ENTER NUMBER OF SUBJECTS :: "))

    marks = []
    for i in range(sn):
        marks.append(int(input(f"Enter marks for Subject {i+1}: ")))
# marks input from user (student)
    avg = sum(marks) / sn
    grade = calculate_grade(avg)
    status = "PASS" if min(marks) >= 35 else "FAIL"
    percent = int(avg)
    rmk = remarks_gen(grade, status)
    rmk ="invalid marks! " if max(marks) >100 else rmk
    student_info[roll_no] = {
        "std_name": name,
        "std_branch": branch,
        "marks": marks,
        "avrg": avg,
        "grade": grade,
        "status": status,
        "percent": percent,
        "maxm": max(marks),
        "minm": min(marks),
        "remarks": rmk
    }

"""# **DATA COLLECTION**

this block collects some basic info about the student
"""

#primary data of student
def student_data_collection():
    name = input("ENTER STUDENT NAME :: ")
    roll_no = input("ENTER STUDENT ROLL NUMBER :: ")
    branch = input("ENTER STUDENT BRANCH (AIDS / CSC / AIML / CSD / CSM):: ").upper()
    mark_calc(name, roll_no, branch)

"""# **UPDATE MARKS**

this up_marks() module enables to modify student marks dynamically

It also modifies total ,avg and all student mark attributes
"""

# marks updating module
def up_marks(roll):
    if roll not in student_info:
        print("ROLL NUMBER NOT FOUND!")
        return

    print("\n++++++ MODIFY MARKS ++++++")

    marks = student_info[roll]["marks"]
    print("Old Marks:", marks)

    print("Enter new marks (press ENTER to keep old mark):")

    for i in range(len(marks)):
        new = input(f"Subject {i+1} new marks: ")
        if new != "":
            marks[i] = int(new)

    avg = sum(marks) / len(marks)
    grade = calculate_grade(avg)
    status = "PASS" if min(marks) >= 35 else "FAIL"
    percent = int(avg)
    rmk = remarks_gen(grade, status)

    student_info[roll]["marks"] = marks
    student_info[roll]["avrg"] = avg
    student_info[roll]["grade"] = grade
    student_info[roll]["status"] = status
    student_info[roll]["percent"] = percent
    student_info[roll]["maxm"] = max(marks)
    student_info[roll]["minm"] = min(marks)
    student_info[roll]["remarks"] = rmk

    print("\nMarks Updated Successfully!")

"""# **STUDENT PROGRASS REPORT**

this shows the final report of the student performence

I CREATED THE THIS BLOCK SOME STRUCURED CONTENTS SO EVERY ONE CAN UNDERSTAND EASILY

INCLUDES REMARKS OF STUDENT NAME AND ALL DATA OF THE STUDENT
"""

#-- student prograss report
def student_P_R(roll):
    if roll not in student_info:
        print("ROLL NUMBER NOT FOUND.")
        return

    data = student_info[roll]

    print("\n\n  _-+=================================================================+-_")
    print("-::|:-:                   STUDENT PROGRESS REPORT                   :-:|::-")
    print("   +===================================================================+")

    print("\nSTUDENT ROLL NUMBER  ::", roll)
    print("STUDENT NAME         ::", data["std_name"])
    print("STUDENT BRANCH       ::", data["std_branch"])
    print("STUDENT AVERAGE MARKS::", data["avrg"])
    print("STUDENT GRADE        ::", data["grade"])
    print("STUDENT STATUS       ::", data["status"])
    print("STUDENT PERCENTAGE   ::", data["percent"])
    print("MAX MARK             ::", data["maxm"])
    print("MIN MARK             ::", data["minm"])

    print("\n--- REMARKS ---")
    print(data["remarks"])

    print("\nSUBJECT MARKS:")
    for i, m in enumerate(data["marks"], 1):
        print(f"Subject {i}: {m}")

    print("\n===========================::      THE END    ::==============================")

"""# **THE FILE CREATION BLOCK**

>this may be doest work on coding platforms due to file path but i executed this program in my system i got a file ` <student_roll no>.txt`

this module creates and writes the data into a file
"""

def cre_wri_file(roll):
    if roll not in student_info:
        print("ROLL NUMBER NOT FOUND.")
        return

    filename = roll + ".txt"
    data = student_info[roll]

    with open(filename, "w") as f:
        f.write("STUDENT PROGRESS REPORT\n")
        f.write("------------------------\n")
        f.write(f"Roll No : {roll}\n")
        f.write(f"Name    : {data['std_name']}\n")
        f.write(f"Branch  : {data['std_branch']}\n")
        f.write(f"Average : {data['avrg']}\n")
        f.write(f"Grade   : {data['grade']}\n")
        f.write(f"Status  : {data['status']}\n")
        f.write(f"Percent : {data['percent']}\n\n")

        f.write("Marks:\n")
        for i, m in enumerate(data["marks"], 1):
            f.write(f"Subject {i}: {m}\n")

        f.write("\nRemarks:\n")
        f.write(data["remarks"])

    print(f"DATA SAVED SUCCESSFULLY IN FILE {filename}")

"""# **AM SEPARATING THE FUNCTION TO REPATE IT SELF BY FUNCTION CALLING**"""

def start():
    print("+======================================+")
    print("|   STUDENT PROGRESS TRACKING SYSTEM   |")
    print("+======================================+")

    student_data_collection()

    while True:
        print("\n============:     MENU     :===============")
        print(":: ENTER [ 1 ] NEW STUDENT ENROLLMENT ::")
        print(":: ENTER [ 2 ] SHOW STUDENT PROGRESS REPORT ::")
        print(":: ENTER [ 3 ] SAVE DATA TO TEXT FILE ::")
        print(":: ENTER [ 4 ] MODIFY MARKS ::")
        print(":: ENTER [ 5 ] EXIT AND RESTART WHOLE SYSTEM AGAIN ::")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("ENTER ONLY NUMBERS!")
            continue

        if choice == 1:
            student_data_collection()

        elif choice == 2:
            roll = input("ENTER STUDENT ROLL NO :: ")
            student_P_R(roll)

        elif choice == 3:
            roll = input("ENTER STUDENT ROLL NO TO SAVE :: ")
            cre_wri_file(roll)

        elif choice == 4:
            roll = input("ENTER YOUR ROLL NO TO MODIFY :: ")
            up_marks(roll)

        elif choice == 5:
            print("\nTHANK YOU FOR USING MY PROGRAM!")
            break

        else:
            print("INVALID OPTION. TRY AGAIN.")

"""NOW `re_sys()` this method works as a called function to the `start()`"""

def re_sys():
    while True:
        start()
        i = input("\nDO YOU WANT TO RESTART SYSTEM? (Y/N): ").lower()
        if i != "y":
            print("PROGRAM TERMINATED.")
            break

"""#**DRIVER CODE**


---

this is main block or driver code which run all the modules in the program by using while to act like a do while loop for atleast one time

where `__name__` == `__main__` that simply difines as the block only executes when we run `MINI_PROJECT.ipynb` dirctly otherwise it doesn't executes

Here i added some strings that prints some structural format of data representation for better user understandability
"""

1if __name__ == "__main__":
    re_sys()
