import cv2
import time

# Create a video capture object, in this case we are reading the video from a file
vid_capture = cv2.VideoCapture('images/Lesswork App.mp4')

if (vid_capture.isOpened() == False):
    print("Error opening the video file")

# Read witdh, height, fps and frame count
else:

    print("Witdh: ",vid_capture.get(3))
    print("Height: ",vid_capture.get(4))

    # Get frame rate information
    # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
    fps = vid_capture.get(5)
    print('Frames per second : ', fps,'FPS')
    # Get frame count
    # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
    frame_count = vid_capture.get(7)
    print('Frame count : ', frame_count)



while(vid_capture.isOpened()):
    # vid_capture.read() methods returns a tuple, first element is a bool 
    # and the second is frame

    ret, frame = vid_capture.read()
    if ret == True:
        time.sleep(0.01) # if we want to see the video in a normal speed

        cv2.imshow('Frame',frame)

        # 20 is in milliseconds, try to increase the value, say 50 and observe
        key = cv2.waitKey(20)
        
        if key == ord('q'):
            break
    else:
        break

# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()