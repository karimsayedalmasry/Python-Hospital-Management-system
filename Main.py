def admin():
    admin_password_counter = 0
    while True:
        admin_password = input("please enter the password: ")
        if admin_password == "1234":
            print("access gratned")
            admin_options(1)
            break
        elif admin_password != "1234":
            admin_password_counter = admin_password_counter + 1
            print("wrong password")
        if admin_password_counter == 3:
            print("Wrong Password System Terminated")
            exit()


def admin_options(password_check):
    if password_check == 1:
        while True:
            option = input(
                "the List of options:\n<<=======================>>\nmanage patients: 1\nmanage doctors: 2\nbook an appointment: 3\nexit from admin mode 4: ")
            if option == '1':
                manage_patients()
            elif option == '2':
                manage_doctors()
            elif option == '3':
                booking()
            elif option == '4':
                break
    elif password_check != 1:
        print("Not allowed")
        exit()


def manage_patients():
    while True:
        manage_patients_option = input(
            "please enter what you want to do\n<<=========================>>\nadd patient 1:\nedit patient 2:\ndelete patient 3:\nview 4:\nback 5:\n")
        if manage_patients_option == '1':
            manage_patients_add_new_patient()
        elif manage_patients_option == '2':
            manage_patients_edit_patient()
        elif manage_patients_option == '3':
            manage_patients_delete_patient()
        elif manage_patients_option == '4':
            manage_patients_view_patient()
        elif manage_patients_option == '5':
            break


def manage_patients_add_new_patient():
    patient_list = [None]*9
    file = open('patients_list.txt', 'r+')
    while True:
        temp_patient_id = str(input("please enter a new patient ID: "))
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 9)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                found = '1'
                break
        if found == '0':
            break
        file.seek(0, 0)
    constants = ["Department:  ", "Dr. name: ", "Patient name: ",
                 "age: ", "gender: ", "Address: ", "Room: ", "His/her Condition: "]
    patient_list[0] = temp_patient_id
    file.write("\n")
    file.write(patient_list[0])
    for i in range(0, 8):
        print("please enter", constants[i])
        patient_list[i] = "_"+input()
        file.write(patient_list[i])

    file.close()


def manage_patients_edit_patient():

    file = open('patients_list.txt', 'r+')
    temp_patient_id = str(
        input("please enter the patient ID you want to edit: "))
    while True:
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 9)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                delete_test(temp_string)
                print("the patient you want to edit: " + temp_string)
                x = input("enter the wrong value that needs to be changed:")
                y = input("enter the right value that: ")
                # temp_list.replace(x, y)
                temp_list[temp_list.index(str.strip(x))] = str(y)
                file.write('\n')
                print(temp_list)
                for i in range(0, 9):
                    temp1 = temp_list[i]+"_"
                    file.write(temp1)
                break
                found = '1'
                break
        if found == '0':
            break
        file.seek(0, 0)
    file.close()
    print("<<==========edited==========>>")


def manage_patients_delete_patient():

    file = open('patients_list.txt', 'r+')
    temp_patient_id = str(
        input("please enter the patient ID you want to delete: "))
    while True:
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 9)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                delete_test(temp_string)
                found = '1'
                break
        if found == '0':
            break
        file.seek(0, 0)
    file.close()
    print("<<==========deleted==========>>")


def manage_patients_view_patient():
    patient_list = [None]*9
    file = open('patients_list.txt', 'r+')
    while True:
        temp_patient_id = str(input("please enter patient ID to display: "))
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 9)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                found = '1'
                print(temp_list)
                break

        if found == '0':
            print("did not find it !!!")

            break
        file.seek(0, 0)
        break

    file.close()


def delete_test(var):
    with open("patients_list.txt", "r") as f:

        lines = f.readlines()

    with open("patients_list.txt", "w") as f:

        for line in lines:

            if line.strip("\n") != var:
                f.write(line)


def manage_doctors():
    while True:
        manage_patients_option = input(
            "please enter what you want to do\n<<=========================>>\nadd doctor 1:\nedit doctor 2:\ndelete doctor 3:\nview 4:\nback 5:\n")
        if manage_patients_option == '1':

            manage_patients_add_new_doctor()
        elif manage_patients_option == '2':
            manage_patients_edit_doctor()
        elif manage_patients_option == '3':
            manage_patients_delete_doctor()
        elif manage_patients_option == '4':
            manage_patients_view_doctor()
        elif manage_patients_option == '5':
            break


def manage_patients_add_new_doctor():
    patient_list = [None]*7
    file = open('doctor_list.txt', 'r+')
    while True:
        temp_patient_id = str(input("please enter a new patient ID: "))
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                found = '1'
                break
        if found == '0':
            break
        file.seek(0, 0)
    constants = ["Department:  ", "Dr. name: ",
                 "age: ", "gender: ", "Address: ", "Phone: "]
    patient_list[0] = temp_patient_id
    file.write("\n")
    file.write(patient_list[0])
    for i in range(0, 6):
        print("please enter", constants[i])
        patient_list[i] = "_"+input()
        file.write(patient_list[i])

    file.close()


def manage_patients_edit_doctor():

    file = open('doctor_list.txt', 'r+')
    temp_patient_id = str(
        input("please enter the doctor ID you want to edit: "))
    while True:
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                delete_test1(temp_string)
                print("the doctor you want to edit: " + temp_string)
                x = input("enter the wrong value that needs to be changed:")
                y = input("enter the right value that: ")
                # temp_list.replace(x, y)
                temp_list[temp_list.index(str.strip(x))] = str(y)
                file.write('\n')
                print(temp_list)
                for i in range(0, 6):
                    temp1 = temp_list[i]+"_"
                    file.write(temp1)
                break
                found = '1'
                break
        if found == '0':
            break
        file.seek(0, 0)
    file.close()
    print("<<==========edited==========>>")


def manage_patients_delete_doctor():

    file = open('doctor_list.txt', 'r+')
    temp_patient_id = str(
        input("please enter the doctor ID you want to delete: "))
    while True:
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                delete_test1(temp_string)
                found = '1'
                break
        if found == '0':
            break
        file.seek(0, 0)
    file.close()
    print("<<==========deleted==========>>")


def manage_patients_view_doctor():
    patient_list = [None]*7
    file = open('doctor_list.txt', 'r+')
    while True:
        temp_patient_id = str(input("please enter doctor ID to display: "))
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                found = '1'
                print(temp_list)
                break

        if found == '0':
            print("did not find it !!!")

            break
        file.seek(0, 0)
        break

    file.close()


def delete_test1(var):
    with open("doctor_list.txt", "r") as f:

        lines = f.readlines()

    with open("doctor_list.txt", "w") as f:

        for line in lines:

            if line.strip("\n") != var:
                f.write(line)


def booking():
    while True:
        manage_patients_option = input(
            "please enter what you want to do\n<<=========================>>\nadd appointment 1:\nedit appointment 2:\ndelete appointment 3:\nback 4:\n")
        if manage_patients_option == '1':
            booking_book()
        elif manage_patients_option == '2':
            booking_edit()
        elif manage_patients_option == '3':
            booking_delete()
        elif manage_patients_option == '4':
            break


def booking_book():
    patient_list = [None]*6
    file = open('appointments.txt', 'r+')
    while True:
        temp_patient_id = str(input("please enter a  patient ID: "))
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                found = '1'
                print(temp_string)
                break
        if found == '0':
            break
        file.seek(0, 0)
    constants = ["Department:  ", "Dr. name: ", "Patient name: ",
                 "age: ", "gender: "]
    patient_list[0] = temp_patient_id
    file.write("\n")
    file.write(patient_list[0])
    for i in range(0, 5):
        print("please enter", constants[i])
        patient_list[i] = "_"+input()
        file.write(patient_list[i])

    file.close()


def booking_edit():

    file = open('appointments.txt', 'r+')
    temp_patient_id = str(
        input("please enter the patient ID you want to edit: "))
    while True:
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                delete_test11(temp_string)
                print("the patient's appointment you want to edit: " + temp_string)
                x = input("enter the wrong value that needs to be changed:")
                y = input("enter the right value that: ")

                temp_list[temp_list.index(str.strip(x))] = str(y)
                file.write('\n')
                print(temp_list)
                for i in range(0, 6):
                    temp1 = temp_list[i]+"_"
                    file.write(temp1)
                break
                found = '1'
                break
        if found == '0':
            print("not found")
            break
        file.seek(0, 0)
    file.close()
    print("<<==========edited==========>>")


def delete_test11(var):
    with open("appointments.txt", "r") as f:

        lines = f.readlines()

    with open("appointments.txt", "w") as f:

        for line in lines:

            if line.strip("\n") != var:
                f.write(line)


def booking_delete():

    file = open('appointments.txt', 'r+')
    temp_patient_id = str(
        input("please enter the patien ID you want to delete it's appointment: "))
    while True:
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                delete_test111(temp_string)
                found = '1'
                break
        if found == '0':
            break
        file.seek(0, 0)
    file.close()
    print("<<==========deleted==========>>")


def delete_test111(var):
    with open("appointments.txt", "r") as f:

        lines = f.readlines()

    with open("appointments.txt", "w") as f:

        for line in lines:

            if line.strip("\n") != var:
                f.write(line)


def user():
    print("here there is something i did not understande so i made them closely enough to what i understood!!!")

    while True:
        option = input(
            "view all departments 1:\nview all doctors 2:\nview all patients 3:\npatient infos 4:\nenterdr. id 5:\n back 6:\n ")
        if option == '1':
            user_view_dep()
        elif option == '2':
            user_view_dr()
        elif option == '3':
            user_view_pa()
        elif option == '4':
            user_view_id_pa()
        elif option == '5':
            user_view_id_dr()
        elif option == '6':
            break


def user_view_dep():

    file = open('doctor_list.txt', 'r+')
    for i, line in enumerate(file):
        temp_string = line.strip()
        temp_list = temp_string.split('_', 6)
        print(temp_list[1])

    file.close()


def user_view_dr():

    file = open('doctor_list.txt', 'r+')
    for i, line in enumerate(file):
        temp_string = line.strip()
        temp_list = temp_string.split('_', 6)
        print(temp_list[2])

    file.close()


def user_view_pa():

    file = open('patients_list.txt', 'r+')
    for i, line in enumerate(file):
        temp_string = line.strip()
        temp_list = temp_string.split('_', 6)
        print(temp_list[3])

    file.close()


def user_view_id_pa():

    file = open('patients_list.txt', 'r+')
    while True:
        temp_patient_id = str(input("please enter a patient ID: "))
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                found = '1'
                print(temp_string)
                return 0
                break
        if found == '0':
            print("not found")
            break

    file.close()


def user_view_id_dr():

    file = open('doctor_list.txt', 'r+')
    while True:
        temp_patient_id = str(input("please enter a DR. ID: "))
        found = '0'
        for i, line in enumerate(file):
            temp_string = line.strip()
            temp_list = temp_string.split('_', 6)
            if str.strip(temp_list[0]) == str(temp_patient_id):
                found = '1'
                print(temp_string)
                break
        if found == '0':
            print("not found")
            break
        if found == '1':

            break
    file.close()


print("Hospital Management system")
while True:
    user_mode = input(
        "type user if you are a user and admin if you are an admin: ")
    if user_mode == "user":
        print("__You are a user__")
        user()

    elif user_mode == "admin":
        print("__You are an admin__")
        admin()
