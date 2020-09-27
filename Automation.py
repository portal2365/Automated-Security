import cv2
import dropbox
import time
import random

startingTime = time.time()

def take_snapshot():
    num = random.randint(0,100)

    videoCaptureObject = cv2.VideoCapture(0)

    result = True

    while(result):
 
        ret,frame = videoCaptureObject.read()
 
        img_name = "img"+str(num)+".png"
        cv2.imwrite(img_name, frame)
        startingTime = time.time
        result = False
    return img_name
    print("Picture Taken Sucessfully")

    videoCaptureObject.release()

    cv2.destroyAllWindows()



def uploaded_file(img_name):
    access_token = "riFu6Ybhc9AAAAAAAAAAIJ_A5fl-EVHtEp33bdEjXapu5jLJLT38D6g_Hz25genB"

    file = img_counter
    file_from = file
    file_to="/Folder1/"+(img_name)

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - startingTime) >= 300):
            name = take_snapshot()
            uploaded_file(name)

main()
