import cv2
import time

resolution = [(160,120),(176,144),(320,240),(352,288),(641,480),(800,600),(1280,1024)]

def change_resolution(w, h):

   capture = cv2.VideoCapture(1)

   num_frame = 0

   size = capture.get(cv2.CAP_PROP_FRAME_WIDTH), capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
   size_new = capture.set(cv2.CAP_PROP_FRAME_WIDTH, w),capture.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
   size_now = capture.get(cv2.CAP_PROP_FRAME_WIDTH), capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
   print (size_now)

   start = time.time()

   while(True):
       ret, frame = capture.read()
       cv2.imshow("Doyu", frame)
       #if num_frame < 60:
       #    num_frame = num_frame + 1
       #    time.sleep(0.001)
       #else:
       #    break
       if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   #total_time = (time.time() - start)
   #fps = (num_frame / total_time)
   #print (str(num_frame) + ' Frames ' + str(total_time) + ' Sekunden = ' + str(fps) + ' fps' + ' for width: ' + str(w) + ' height: ' + str(h))

   capture.release()
   cv2.destroyAllWindows()


for reso in resolution:
   change_resolution(reso[0], reso[1])
