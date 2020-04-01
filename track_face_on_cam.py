import face_recognition
import cv2
import matplotlib.patches as patches
from IPython.display import clear_output
from matplotlib.pyplot import imshow
import matplotlib.pylab as plt
from PIL import Image, ImageDraw

# Loading video for face detection
#video_capture = cv2.VideoCapture("D:/Download/projet-reconnaissance-faciale/track face on video/face_recognition_test.mp4")
video_capture = cv2.VideoCapture(0)
video_capture.read()
frame_count = 0
if not (video_capture.isOpened()):

    print("Could not open video device")
while (video_capture.isOpened()):    
    # Grab a single frame of video
    ret, frame = video_capture.read()
    
    # We will search face in every 15 frames to speed up process.
    frame_count += 1
    if frame_count % 15 == 0:    
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

 all the faces and face encodings in the current frame of video
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        #pil_image = Image.fromarray(frame)

        #draw = ImageDraw.Draw(pil_image)

        # If faces were found, we will mark it on frame with blue dots
        for face_location in face_locations:       
           # draw.rectangle(((face_location[0], face_location[1]), (face_location[2], face_location[3])), outline=(255,255,0))
            plt.plot(face_location[1], face_location[0],'bo')
            plt.plot(face_location[1], face_location[2],'bo')
            plt.plot(face_location[3], face_location[2],'bo')
            plt.plot(face_location[3], face_location[0],'bo')
        # Show frame...
        #del draw
        plt.show() 
        # ... and hold it until a new frame appears
        clear_output(wait=True)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
#pil_image.show()

video_capture.release()

cv2.destroyAllWindows()

