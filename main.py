import time
import mido
from pynput import keyboard
from controls import turn_on, turn_off

out_port = mido.open_output('USB20MIDI 1')
keys = "1234567890qwertzuiopüasdfghjklöäyxcvbnm"

def on_press(key):
    try:
        turn_on(out_port,keys.index(key.char)+1)
        # print(key.char)

    except AttributeError:
        pass
        # print(key)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
        turn_off(out_port,keys.index(key.char)+1,64)
    except AttributeError:
        pass

# Collect events until released
with keyboard.Listener(
        suppress=True,
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

