import os
from zipfile import ZipFile

## Current issue is that if you export two files at the same time, the second file will overwrite the first file. Is there a way to fix this?
## Is there way to name the exported file with the name of the folder that the files are in or maybe something unique?
class ShareFiles:
    def zip_files(self, files):
    # files: str list of audio file path(s) or directory path(s)
        try:
            zip = ZipFile("./export/export.zip", "w")
            for file in files:
                if file[-4:] == '.wav':
                    zip.write(file, arcname=file.split('/')[-1])
                elif os.path.isdir(file):
                    for root, dirs, files in os.walk(file):
                        for file in files:
                            path = os.path.join(root, file)
                            zip.write(path, arcname=os.path.relpath(path, os.path.dirname(files[0])))
                        for dir in dirs:
                            path = os.path.join(root, dir)
                            zip.write(path, arcname=os.path.relpath(path, start=os.path.dirname(file)))
                
            zip.close()
        except:
            print("Could not ZIP: " + file)





