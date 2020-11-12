import os
def update_record():
    search = input("Enter Member ID : ")
    u = 0
    file = open("finalproject.txt", "r")
    tf = open("temp.txt", "w")
    while (True):
        t = file.readline()
        l = len(t)
        if (l == 0):
            break
        g = t.split("--")
        if (g[0] == search):
            print("Current Detail is\n", t)
            print("----------------------")
            newNAME = input("Enter New Name or press enter to skip it : ")
            newEMAIL = input("Enter New Email or press enter to skip it : ")
            newPHONE = input("Enter New Phone Number or press enter to skip it : ")
            newPAYMENT = input("Enter New Payment or press enter to skip it : ")
            newCOURT = input("Enter New Court Number or press enter to skip it : ")
            newPLAYDAY = input("Enter New Play day or press enter to skip it : ")
            newPLAYTIME = input("Enter New Play Time or press enter to skip it : ")
            newMEMBERDURATION = input("Enter New Member Duration or press enter to skip it : ")
            newEXPIRYDATE = input("Enter New Expiry Date or press enter to skip it : ")
            if len(newNAME) == 0:
                newNAME = g[1]
            if (len(newEMAIL) == 0):
                newEMAIL = g[2]
            if (len(newPHONE) == 0):
                newPHONE = g[3]
            if (len(newPAYMENT) == 0):
                newPAYMENT = g[4]
            if (len(newCOURT) == 0):
                newCOURT = g[5]
            if (len(newPLAYDAY) == 0):
                newPLAYDAY = g[6]
            if (len(newPLAYTIME) == 0):
                newPLAYTIME = g[7]
            if (len(newMEMBERDURATION) == 0):
                newMEMBERDURATION = g[8]
            if (len(newEXPIRYDATE) == 0):
                newEXPIRYDATE = g[9]
            tf.write(g[0] + "--" + newNAME + "--" + newEMAIL + "--" + newPHONE + "--"
                     + newPAYMENT + "--" + newCOURT + "--" + newPLAYDAY + "--" +
                     newPLAYTIME + "--" + newMEMBERDURATION + "--" + newEXPIRYDATE)
            u = 1
        else:
            tf.write(t)
    file.close()
    tf.close()
    if (u == 1):
        print("Recorded Updated Successfully")
        os.remove("finalproject.txt")
        os.rename("temp.txt", "finalproject.txt")
    elif (u == 0):
        print("Record No Exist")
