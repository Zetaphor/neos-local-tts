import subprocess
import os
output = subprocess.check_output('..\mpv\\mpv.com --audio-device=help').decode('utf-8').strip().split('\r\n')

output_devices = {}

x = 1
for line in output:
  if (line.__contains__('wasapi')):
    output_devices[x] = [line.split("' (")[1::2][0][:-1], line.split("'")[1::2][0]]
    x += 1
output_devices[x] = ["Cancel", "cancel"]

def print_menu():
    for key in output_devices.keys():
        print (key, '--', output_devices[key][0])

def set_audio_option(index):
  if (os.path.exists("..\mpv\mpv.conf")):
    os.remove("..\mpv\mpv.conf")
  mpv_config = open("..\mpv\mpv.conf", "w")
  mpv_config.write('audio-device=' + output_devices[index][1])
  mpv_config.close()
  mpv_config = open("..\mpv\mpv.conf", "r")
  print('\nSet Neos TTS server output to ' + output_devices[index][0])
  input("\nPress Enter to continue...")

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
            set_audio_option(option)
            exit()
        except:
          exit()