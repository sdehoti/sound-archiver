import os
from zipfile import ZipFile

class ShareFiles:
    def zip_files(self, files):
        export_name = input("Enter the name of the export file: ") + ".zip" #creating a unique name for the zip file so that it does not overwrite any existing files. 
        export_path = "./export/" + export_name
        try:
            zip = ZipFile(export_path, "w")
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
            print("ZIP file created successfully.")
            input("Press Enter to continue...")
        except:
            print("Could not ZIP: " + file)





