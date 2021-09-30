import time
import mido
from pynput import keyboard
import playsound
from controls import turn_on, turn_off
from mingus.midi.midi_file_in import MidiFile
from multiprocessing import Process
from threading import Thread
from playsound import playsound

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
        turn_off(out_port,keys.index(key.char)+1,20)
    except AttributeError:
        pass

def play_music():
    playsound("E:/Downloads/Britney Spears - Work B_ch (Official Music Video).mp3")

turn_off(out_port)
mid = mido.MidiFile("test2.MID")

file = MidiFile()
parsed = file.parse_midi_file("test2.mid")
spt = (5/parsed[0][2]["ticks_per_beat"])/10     # seconds per tick
# print(spt)
T = Thread(target=play_music) # create thread
T.start() # Launch created thread

dec_next = 0
for i,msg in enumerate(mid.tracks[0]):
    
    if msg.time == 0:
        mid_tick = 2
        dec_next += 2
    else:
        mid_tick = msg.time - dec_next    
        dec_next = 0
    time.sleep(spt*mid_tick)
    print(msg.time)
    print(i)
    print(msg)
    out_port.send(msg)


# turn_on(out_port,5,vel = 60)
# for msg in mido.MidiFile('test.mid').play():
#     print(msg)
#     out_port.send(msg)
# with mido.open_input("PD 12 1") as inport:
#     for msg in inport:
#         turn_on(out_port,msg.note,msg.velocity)
#         print(msg)

# asdCollect events until released
# with keyboard.Listener(
#         suppress=True,
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
