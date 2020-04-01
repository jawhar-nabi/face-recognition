import glob
import face_recognition
images = []
encodings=[]
for file in glob.glob("*.jpg"):
    images.append(file)
    print("".join(file.split('.')[0:-1]))
    encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(file))[0])
print('*********')

