import subprocess
import asyncio
from configparser import ConfigParser
from gtts import gTTS
from websockets import serve
import simpleaudio as sa

import pyttsx3
microsoft_engine = pyttsx3.init('sapi5')

config_object = ConfigParser()
config_object.read("config.ini")

CONFIG_VOICE_ENGINE = config_object['VoiceEngine']['engineName'].lower()
CONFIG_LOCAL_PLAYBACK = config_object['VoiceEngine']['localPlayback'].lower()
CONFIG_SERVER_PORT = config_object['ServerPort']['port']

CONFIG_GTTS_LANG = config_object['Google']['language'].lower()

CONFIG_MICROSOFT_VOICE = config_object['Microsoft']['voice'].lower()
CONFIG_MICROSOFT_RATE = config_object['Microsoft']['speechRate']

microsoft_voice_keys = {
    "david": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
    "eva": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_EvaM",
    "mark": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM",
    "hazel": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0",
    "zira": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
}

microsoft_voice = microsoft_voice_keys[CONFIG_MICROSOFT_VOICE]

gtts_language_tlds = {
    'en-au': ['en', 'com.au'],
    'en-uk': ['en', 'co.uk'],
    'en-us': ['en', 'com'],
    'en-ca': ['en', 'ca'],
    'en-in': ['en', 'co.in'],
    'en-ie': ['en', 'ie'],
    'en-za': ['en', 'co.za'],
    'fr-ca': ['fr', 'ca'],
    'fr-fr': ['fr', 'fr'],
    'zh-cn': ['zh-CN', 'com'],
    'zh-tw': ['zh-TW', 'com'],
    'pt-br': ['pt', 'com.br'],
    'pt-pt': ['pt', 'pt'],
    'es-mx': ['es', 'com.mx'],
    'es-es': ['es', 'es'],
    'es-us': ['es', 'com'],
}

gtts_language = gtts_language_tlds[CONFIG_GTTS_LANG]


async def gtts_message(message):
    tts = gTTS(message, lang=gtts_language[0], tld=gtts_language[1])
    tts.save('output.mp3')
    subprocess.call('mpv\\mpv.com output.mp3')


async def microsoft_sapi_message(message):
    microsoft_engine.setProperty('voice', microsoft_voice)
    microsoft_engine.setProperty("rate", int(CONFIG_MICROSOFT_RATE))
    microsoft_engine.save_to_file(message, 'output.mp3')
    microsoft_engine.runAndWait()
    if (CONFIG_LOCAL_PLAYBACK == "true"):
        play_local_audio()
    subprocess.call('mpv\\mpv.com output.mp3')

def play_local_audio():
    wave_object = sa.WaveObject.from_wave_file('output.mp3')
    wave_object.play()

async def NeosWSS(websocket):
    async for message in websocket:
        if (CONFIG_VOICE_ENGINE == 'google'):
            await gtts_message(message)
        elif (CONFIG_VOICE_ENGINE == 'microsoft'):
            await microsoft_sapi_message(message)
        await websocket.send(message)


async def main():
    print('Server started on port ', CONFIG_SERVER_PORT)
    async with serve(NeosWSS, "localhost", int(CONFIG_SERVER_PORT)):
        await asyncio.Future()

asyncio.run(main())
