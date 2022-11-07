# NeosVR Local TTS System

**This is beta software and is still under development. If you encounter issues please contact Zetaphor in Neos, Zetaphor#0237 on Discord, or

This is a TTS system for NeosVR that enables you to generate TTS audio on your local machine and play it back over an audio output in Neos.
This means instead of generating audio on a server that every user must download to hear, you are able to play back your TTS audio on a standard microphone output.
This system is designed to support multiple TTS providers. Currently it supports Google TTS and Microsoft Windows SAPI. More integrations are planned.

There are two parts to this system, the application running on your computer that generates and plays the audio, and the in-world object that allows you to
create messages to be sent to the computer software. A modified version of the standard Mute Helper that is found in Neos Essentials has been created to work with this system.
You can get a copy of this modified Mute Helper by pasting the following link into your Neos window:

neosdb:///b49a42c5d2ce8d4bb516bf4fe27e3e28681bc61f5ad278926c3bcd03e2989a87.7zbson

## Usage

Once you have the modified Mute Helper installed to your avatar, launch the server executable, `neos-tts-server.exe`.
When you run for the first time, Windows Firewall may prompt you to allow the application through, click accept otherwise the server will not be able to communicate with Neos and/or Google.
The application should start and show "Server started on port X" where X is the port you configured (default is 7000).
Once the local server is started, check the settings in the Mute Helper menu, you should see a green section with a checkmark showing "Connected".
If you don't see the Mute Helper connected, try re-equipping an avatar that has the Mute Helper saved on it, or respawn.

### Configuring Audio Output

The audio output device can be configured by running the utility located in the `audio-output-selector` subfolder. This utility will list all available audio outputs that can be used as a TTS playback target.
When you select an output, this updates the entry in `mpv/mpv.conf` to the correct device ID.

It is advised to install an [application like VB-Cable](https://vb-audio.com/Cable/) which provides you an dummy output that audio can be routed into.
Once installed you can set the output of VLC to the VB-Cable output, and specify that device as your microphone input in Neos.

## Configuration

All configuration is done through the config.ini file.

### Google Text To Speech

You can specify different languages/accents

### Microsoft SAPI

You can specify the language and speech rate. The language needs to be present on the system. I need to include a way to list these for users.
Possibly generate a separate file that contains all available voices and expose them to the engine for users in other language locales that I don't have.

Read here for adding additional voices to Windows.

https://support.microsoft.com/en-us/topic/download-voices-for-immersive-reader-read-mode-and-read-aloud-4c83a8d8-7486-42f7-8e46-2b0fdf753130

To enable the Eva and Mark voices for Windows, install the two registry key hives in `ms-sapi-additional-voices`

## Building from source

Built with Python 3.10.8 and pip 22.3.1 on Windows 10

Install requirements:

```pip install -r requirements.txt```

Build a new distributable with PyInstaller

```python -m PyInstaller neos-tts-server.py```

A batch script is provided to run this command


mpv.com --audio-device=help
document include reg zip
option to not listen to local
Need to actually add cancel check in audio selector