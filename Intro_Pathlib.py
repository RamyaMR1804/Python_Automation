from pathlib import Path

p1=Path("C:/Users/sussingh/Desktop/Python_Automation/Pathlib_file.txt")

if p1.exists():
    with open(p1,'r') as file:
        print(file.read())
else:
    with open(p1,'w') as file:
        file.write('Hello world')