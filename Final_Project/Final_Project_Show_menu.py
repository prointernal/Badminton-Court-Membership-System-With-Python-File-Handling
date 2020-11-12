from Final_Project_Delete_Record import delete_record
from Final_Project_Update_Record import update_record
from Final_Project_create_record import create_record
from Final_Project_Display_Record import display_all
from Final_Project_search_id import search_id
from Final_Project_search_name import search_name

def show_menu():
    while (True):
        print("----------------------------------------")
        print("BADMINTON COURT MEMBERSHIP SYSTEM")
        print("ADMIN MENU")
        print("1.Add New Record")
        print("2.Display All Record")
        print("3.Search Member Record By Name")
        print("4.Search Member Record By id")
        print("5.Delete Member Record By id")
        print("6.Update Member Record")
        print("7.Exit")
        print("----------------------------------------")
        option = int(input("Enter your choice : "))

        if option == 1:
            create_record()
        elif option == 2:
            display_all()
        elif option == 3:
            search_name()
        elif option == 4:
            search_id()
        elif option == 5:
            delete_record()
        elif option == 6:
            update_record()
        elif option == 7:
            break
