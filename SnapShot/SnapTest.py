import os
import sys
import time
import Image
import ImageGrab

SaveDirectory=r'C:\Temp'

for i in range(5):
    img=ImageGrab.grab()
    saveas= os.path.join(SaveDirectory,'Screenshot_'+time.strftime("%Y-%m-%d_%H-%M-%S")+'.jpg')
    img.save(saveas)
    time.sleep(5)
    
