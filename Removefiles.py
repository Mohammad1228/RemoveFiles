import time
import shutil 
import os

def main():
    days = 30
    path = "/Users/Damani/Downloads/Thumbs (2)"
    seconds = time.time() - days*24*60*60
    #checking if path exists then we delete
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= checkTimeOfFile(root_folder):
                removeFolder(root_folder)
            else:
                for folder in folders:
                    folderpath = os.path.join(root_folder,folder)
                    if seconds >= checkTimeOfFile(folderpath):
                        removeFolder(folderpath)
                for file in files:
                    filepath = os.path.join(root_folder,file)
                    if seconds>= checkTimeOfFile(filepath):
                        removeFile(filepath)
    else:
        print("path is not found")



def removeFolder(path):
    if not shutil.rmtree(path):
        print("removed successfully")
    else:
        print('unable to delete')



def removeFile(path):
    if not os.remove(path):
        print('removed successfully')
    else:
        print("unable to delete")




def checkTimeOfFile(path):
    ctime=os.stat(path).st_ctime

    return ctime

if (__name__=="__main__"):
    main()
