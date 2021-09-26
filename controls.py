import time
import mido

def turn_off(port,faders=(1,48),vel=127):
    if type(faders) is not tuple:
        faders = (faders,)
    for fader in range(faders[0],faders[-1]+1):
        msg = mido.Message('note_off',note=fader,velocity=vel)
        port.send(msg)
        time.sleep(0.00001)

def turn_on(port,faders=(1,48),vel=127):
    if type(faders) is not tuple:
        faders = (faders,)
    for fader in range(faders[0],faders[-1]+1):
        msg = mido.Message('note_on',note=fader,velocity=vel)
        port.send(msg)
        time.sleep(0.00001)