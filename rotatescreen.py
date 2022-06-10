#Go To terminal Then
       #download
#pip install rotate-screen
#pip install pypiwin32

import time
import rotatescreen
screen = rotatescreen.get_primary_display()
screen.rotate_to(0)
for i in range(10):
    time.sleep(1)
    screen.rotate_to(i*90%360)

    #stop this problems fass ctrl + F2

