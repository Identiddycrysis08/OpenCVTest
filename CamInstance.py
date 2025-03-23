import cv2
def caminst():
    cam=cv2.VideoCapture(0)
    frame_w= int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_h= int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc= cv2.VideoWriter_fourcc(*'X264')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_w,frame_h))
    while True:
        ret, frame = cam.read()
        
        if ret==True:
            cv2.rectangle(frame, (100, 100), (500, 500), (0, 255, 0), 3)         
            out.write(frame)
            cv2.imshow('Camera', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        
    cam.release()
    out.release()
    cv2.destroyAllWindows()
