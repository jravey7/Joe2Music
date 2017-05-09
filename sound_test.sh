#! /bin/sh

# stereo sound test
# the 3.5mm audio jack on the pi is mono only
# USB sound card is stereo 

aplay /usr/share/sounds/alsa/Front_Center.wav
aplay /usr/share/sounds/alsa/Side_Left.wav
aplay /usr/share/sounds/alsa/Side_Right.wav
