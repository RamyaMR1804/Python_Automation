from pathlib import Path
import zipfile

root_dir= Path("C:/Users/sussingh/Desktop/Python_Automation/extract_zip")
Destination_path= root_dir / Path('Destination')

for path in root_dir.glob("*.zip"):
    with zipfile.ZipFile(path,'r') as zf:
        zf.extractall(path=Destination_path)