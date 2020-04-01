import cv2
from matplotlib.pyplot import imshow
import matplotlib.pylab as plt
import face_recognition
import glob
# Open the device at the ID 0

cap = cv2.VideoCapture(0)
results = []
#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):

    print("Could not open video device")

#To set the resolution

#cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)

#cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

images = []
encodings=[]
for file in glob.glob("*.jpg"):
    images.append("".join(file.split('.')[0:-1]))
    encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(file))[0])



count_faces = 0

while(True):

    # Capture frame-by-frame

    ret, frame = cap.read()
    # Display the resulting frame
    face_locations = face_recognition.face_locations(frame)
    name = "No face detected !"
    if(len(face_locations) != count_faces):
        
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(encodings, face_encoding)

            name = "Unknown Person"
            if True in matches:
                first_match_index = matches.index(True)
                name = images[first_match_index]
                if name not in results:
                    results.append(name)
        # If match

        # Compare faces
       # results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
       # if results[0]:
       #     print('This is jawhar')
        
        count_faces = len(face_locations)
        print(f'There are {len(face_locations)} people in this image {count_faces}')
        #print(name)


    # for face_location in face_locations:       
    #     plt.plot(face_location[1], face_location[0],'bo')
    #     plt.plot(face_location[1], face_location[2],'bo')
    #     plt.plot(face_location[3], face_location[2],'bo')
    #     plt.plot(face_location[3], face_location[0],'bo')
    #cv2.imshow('preview',cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    cv2.imshow('preview',frame)
    #plt.show()
    #Waits for a user input to quit the application

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

    # When everything done, release the capture
cap.release()

cv2.destroyAllWindows()
print(results)