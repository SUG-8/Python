import pandas
df=pandas.read_csv("dpdd-students.csv")

def name_check(Name):
    name = df[df["Name"] == Name]
    if not name.empty:
        ID= name["userID"]
        return ID
    else:
        return "not found"
def id_check(userID):
    ID=df[df["userID"]==userID]
    if not ID.empty:
        name=ID["Name"]
        return name
    else:
        return "UserID not found"


def main():
    grey=True
    flag = True
    while flag:
        try:
            choice= int(input("###### MENU #######\n##1. Enter student ID\n##2. Enter student name\nEnter choice: "))
            flag=False
        except:
            print("please enter a number")
            flag=True
        else:
            if choice<1 or choice>2:
                print("number entered is out of range")
                flag=True

            elif choice ==1:
                while grey:
                    try:
                        userID = int(input("enter userID:"))
                        ID = id_check(userID)
                        print(f"The student matching that information is \n{ID}")
                        grey = False
                    except:
                        print("enter a number")
                        grey = True

            else:
                while grey:

                    userName= str(input("enter student name:")).lower()
                    if userName.isalpha():
                        Name = name_check(userName)
                        print(f"The student ID of student entered is \n{Name}")
                        grey=False

                    else:
                        print("please enter a string with no numbers")
                        grey=True





main()

