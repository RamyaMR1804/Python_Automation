from pathlib import Path

p1=Path(input("Enter the path of the folder:-  "))

if p1.exists():
    print("List of files in folder are- ")
    print("--------------------------------------------------------------------------------------------------------------------")
    for i in p1.iterdir():
        print(i)
    print("--------------------------------------------------------------------------------------------------------------------")    
else:
    print("Folder doesnot exists try again.")