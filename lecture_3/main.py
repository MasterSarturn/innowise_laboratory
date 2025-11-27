
students = []

def in_list(name):
    """Return the index of a student with the given name, or -1 if not found.
    """
    for index, student in enumerate(students):
        if student['name'] == name:
            return index
    return -1

def add_user ():
    """Add a new student
    Currently, the program only accepts names consisting of alphabetic characters.
    If the name contains non-letter symbols, the user will be asked to try again.
    """
    while True:

        name = input('Enter student name: ').strip()
        if name.isalpha():

            if in_list(name) !=-1:
                    print('Such student does already exist.')
                    break
            else:
                students.append({"name": f"{name.capitalize()}", "grades": []})
            return
        
        print("The name should consist of letters only.\nIf your name consists of special symbols, ignore them. Try again!")
            
def add_grade ():
    """Add a grade to a student
    - check if at least one student is in list 'students'
    - repeatedly asks for grade input,
    - accepts 'done' to stop,
    - validates that grades are integers between 0 and 100.
    """
    if len(students) == 0:
        print("There are no students now.")
        return
    
    while True:

        name = input('Enter student name: ')
        name = name.strip()

        if name.isalpha():
            position = in_list(name.capitalize())

            if position == -1:
                print("No such student.")
                return
            
            else:
                while True:
                    try:
                        grade = (input("Enter a grade (or 'done' to finish): "))

                        if grade.strip().lower() == 'done':
                            return
                        grade = int(grade)
                        if grade <0 or grade>100:
                            print("Grade should be from 0 to 100.")
                            continue
                        students[position]['grades'].append(grade)
                        
                    except ValueError:
                        print("Grade should consist only of digits. Try again!")
        else: print("The name should consist of letters only. Try again!")
            
def show_report ():
    """Show the report of the grades of students
    - check if at least one student is in list 'students'
    For each student:
    - compute and display the average grade,
    - handle students with no grades (print N/A).
    """
    if len(students) == 0:
        print("There are no students now.")
        return
    max_average, min_average, overall_average,counter = 0,100,0,0
    for i in students:
        avg =0
        try:
            for j in i["grades"]:
                avg+= j
            avg = avg/len(i["grades"])
            if avg> max_average:
                max_average = avg
            if avg < min_average:
                min_average = avg
            overall_average +=avg
            counter+=1       
            print(f"{i['name']}'s average grade is {round(avg, 1)}.")
        except ZeroDivisionError:
            print(f"{i['name']}'s average grade is N/A.")
    print("---"*5)
    if counter==0:
        print("There are no grades added yet.")
        return
    print(f"Max Average: {round(max_average, 1)}\nMin Average: {round(min_average, 1)}\nOverall Average: {round(overall_average/counter, 1)}")
            


def find_top ():
    """Find the student with the highest average grade
    - check if at least one student is in list 'students'
    """
    if not students:
        print("There are no students now.")
        return
    best = max(students, key = lambda x: sum(x['grades'])/len(x['grades']) if len(x['grades'])>0 else -1)
    if not best['grades']:
        print("There are no grades added yet.")
    else:
        print(f"The student with the highest average is {best['name']} with a grade of {round(sum(best['grades'])/len(best['grades']), 1)}.")
        
"""Main loop of the program
"""
while True:
    try:
        answer = int(input("\n--- Student Grade Analyzer ---\n1. Add a new student\n2. Add grades for a student\n3. Show report (all students)\n4. Find top performer\n5. Exit\nEnter your choiсe: "))
    except ValueError:
        print('\nThat was not valid number. Try again!\n')
        continue
    match answer:
        case 1:
            add_user()
        case 2:
            add_grade()
        case 3:
            show_report()
        case 4:
            find_top()
        case 5:
            print("Exiting program.")
            break