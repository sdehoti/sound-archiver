import os
from zipfile import ZipFile
import tkinter as tk

class ShareFiles:
    """
    ShareFiles class provides methods to zip files and directories.
    """
    def zip_files(self, files):
        """
        Zips the provided files and directories into a single ZIP file.

        Parameters:
            files (list): List of file paths to be zipped.

        Returns:
            None

        Raises:
            None
        """
        # Creating a unique name for the zip file so that it does not overwrite any existing files.
        export_name = tk.simpledialog.askstring("Export Files", "Enter the name of the export file: ") + ".zip"
        export_path = "./export/" + export_name
        try:
            zip = ZipFile(export_path, "w")
            for file in files:
                print(file)
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
        except:
            print("Could not ZIP: " + file)





