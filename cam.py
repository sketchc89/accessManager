import cv2
import datetime 


class FaceDetector:
    def __init__(self, face_cascade_path):
        self.faceCascade = cv2.CascadeClassifier(face_cascade_path)

    def detect(self, image, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30)):
        rects = self.faceCascade.detectMultiScale(image,
                                                scaleFactor = scaleFactor, 
                                                minNeighbors = minNeighbors, 
                                                minSize = minSize, 
                                                flags = cv2.CASCADE_SCALE_IMAGE)
        return rects

def CaptureFace(wait_time=1):
    face_cascade_path = './haarcascade_frontalface_default.xml'
    face_detect = FaceDetector(face_cascade_path)
    camera = cv2.VideoCapture(0)
    time_init = datetime.datetime.now()
    rects = []
    padding = 30
    i = 0
    while not rects and (datetime.datetime.now() - time_init < datetime.timedelta(seconds=wait_time)):
        (grabbed, frame) = camera.read()
        if not grabbed:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rect = face_detect.detect(gray)
        if len(rect) > 0 and i < 10:
            i += 1
            print(rect)
            (x,y,w,h) = rect[0]
            cv2.imwrite('face{0}{1}.jpg'.format(datetime.datetime.now(), i), gray[y-padding:y+h+padding, x-padding:x+w+padding])
    camera.release()
    cv2.destroyAllWindows()
