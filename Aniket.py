from datetime import datetime
cd=datetime.now()
print(" Welcome user ")
un="Aniket"
pw="Aniket@!1!23"


USER_NAME=input("Enter User Name")
PASSWORD=input("Enter Password ")

if un==USER_NAME and pw == PASSWORD:
    print("successful login ",un,"At",cd)

else:
    print("  Failed to login At",cd)