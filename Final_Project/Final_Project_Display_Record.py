def display_all():
    print("\nList of Members \n")
    print("ID -- NAME -- EMAIL -- PHONE NUMBER -- PAYMENT -- COURT -- "
          "PLAY DAY -- PLAY TIME -- MEMBER DURATION -- EXPIRY DATE")
    file = open("finalproject.txt", "r")
    while (True):
        t = file.readline()
        l = len(t)
        if (l == 0):
            break
        print(t.strip())
    file.close()
