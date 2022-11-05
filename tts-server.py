import subprocess
from gtts import gTTS
from gtts import gTTS



import asyncio
from websockets import serve

async def echo(websocket):
    async for message in websocket:
        print("Received:", message)
        tts = gTTS(message)
        tts.save('gtts.mp3')
        subprocess.call('vlc\\vlc.exe gtts.mp3 --play-and-exit')
        await websocket.send(message)

async def main():
    print('Server Started')
    async with serve(echo, "localhost", 7000):
        await asyncio.Future()  # run forever

asyncio.run(main())


