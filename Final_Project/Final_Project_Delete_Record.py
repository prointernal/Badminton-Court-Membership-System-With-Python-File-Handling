import os
def delete_record():
    search = input("ENTER MEMBER ID : ")
    file = open("finalproject.txt", "r")
    tf = open("temp.txt", "w")
    d = 0
    while (True):
        t = file.readline()
        l = len(t)
        if (l == 0):
            break
        g = t.split('--')
        if (g[0] != search):
            tf.write(t)
        if (g[0] == search):
            d = 1
    file.close()
    tf.close()
    if (d == 1):
        print("Record Deleted Successfully")
        os.remove("finalproject.txt")
        os.rename("temp.txt", "finalproject.txt")
    elif (d == 1):
        print("Record Not Found")





