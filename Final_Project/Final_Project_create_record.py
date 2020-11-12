def create_record():
    print("\nEnter Member Detail")
    print("----------------------------------------")
    id = input("Enter id : ")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone Number: ")
    payment = input("Enter Member Payment: ")
    court = input("Enter Member Court :")
    playday = input("Enter Member Play Day :")
    playtime = input("Enter Member Play Time :")
    member_duration = input("Enter Member duration: ")
    expiry_date = input("Enter Expiry date: ")
    file = open("finalproject.txt", "a")
    file.write(
        id + "--" + name + "--" + email + "--" + phone + "--" + payment + "--" + court + "--" +
        playday + "--" + playtime + "--" + member_duration + "--" + expiry_date + "\n")
    file.close()
