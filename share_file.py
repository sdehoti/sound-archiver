import sounds as sounds
from zipfile import ZipFile

class ShareFiles:
    def zip_files(audio_files):
    # audio_files: str list of audio file paths
        try:
            zip = ZipFile("./export/export.zip", "w")
            for file in audio_files:
                zip.write(file, arcname=file.split('/')[-1])
            zip.close()
        except:
            print("Cannot ZIP files")






