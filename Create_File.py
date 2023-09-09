from pathlib import Path
root_dir= Path("C:/Users/sussingh/Desktop/Python_Automation/Create_file")

for i in range(1,11):
    filename=str(i)+'.txt'
    filepath=root_dir/Path(filename)
    filepath.touch()