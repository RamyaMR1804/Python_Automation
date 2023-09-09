from pathlib import Path
from datetime import datetime
############################# RENAME FILES ##################################
# root_dir= Path("C:/Users/sussingh/Desktop/Python_Automation/Rename_file")
# file_path=root_dir.iterdir()
# count=1
# for path in file_path:
#     new_filepath=path.with_name("File_"+str(count)+path.suffix)
#     print(new_filepath)
#     path.rename(new_filepath)
#     count+=1

############################# RENAME FILES BASED ON SUB FOLDER ##################################
# root_dir= Path("C:/Users/sussingh/Desktop/Python_Automation/Rename_file")
# file_paths = root_dir.glob("**/*")

# for path in file_paths:
#     if path.is_file():
#         new_filepath=path.with_name(path.parts[-2] + "_" + path.name)
#         path.rename(new_filepath)

############################# RENAME FILES BASED ON TIME CREATED ##################################
root_dir= Path("C:/Users/sussingh/Desktop/Python_Automation/Rename_file")
file_paths = root_dir.glob("**/*")

for path in file_paths:
    if path.is_file():
        created_on=datetime.fromtimestamp(path.stat().st_ctime).strftime("%Y%m%d_%H%M%S")
        new_filepath=path.with_name( path.stem+"_"+created_on + path.suffix)
        path.rename(new_filepath)