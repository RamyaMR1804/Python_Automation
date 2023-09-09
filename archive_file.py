from pathlib import Path
import zipfile

root_dir= Path("C:/Users/sussingh/Desktop/Python_Automation/Create_file")
archive_path= root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path,'w') as zf:
    for path in root_dir.rglob("*.txt"):
        zf.write(path)
        path.unlink()
