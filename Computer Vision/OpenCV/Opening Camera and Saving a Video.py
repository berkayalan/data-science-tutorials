import cv2

# capture video
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width, height)

# save the video
writer = cv2.VideoWriter("/images/video_file.mp4", cv2.VideoWriter_fourcc(*"XVID"),20,(width, height)) # 20 is frame rate per second

while True:
    
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()

