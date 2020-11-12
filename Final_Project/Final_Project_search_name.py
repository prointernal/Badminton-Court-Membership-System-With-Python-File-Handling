def search_name():
    search = input("Enter Member Name = ")
    file = open("finalproject.txt", "r")
    flag = 0
    while (True):
        t = file.readline()
        l = len(t)
        if l == 0:
            break
        g = t.split("--")
        if (g[1] == search):
            print("\nRecord Found")
            print("ID : ", g[0])
            print("NAME : ", g[1])
            print("EMAIL : ", g[2])
            print("PHONE NUMBER : ", g[3])
            print("PAYMENT : ", g[4])
            print("COURT : ", g[5])
            print("PLAY DAY : ", g[6])
            print("PLAY TIME : ", g[7])
            print("MEMBER DURATION :", g[8])
            print("EXPIRY DATE : ", g[9])
            flag = 1
            break
    if (flag == 0):
        print("Record Not Found")
    file.close()