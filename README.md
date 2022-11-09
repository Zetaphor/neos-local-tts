# NeosVR Local TTS System

**The developer of this software and the software itself is in no way officially affiliated with or endorsed by Neos, Solirax, or any representative of the Neos staff.**

This is a hobby project built by an enthusiast as a community contribution. If you encounter issues please create open an issue on this repo and/or contact Zetaphor in Neos, Zetaphor#0237 on Discord, or Zetaphor on Guilded.

## About

This is a TTS system for NeosVR that enables you to generate TTS audio on your local machine and play it back over an audio output in Neos.
This means instead of generating audio on a server that every user must download to hear, you are able to play back your TTS audio on a standard microphone output.
This system is designed to support multiple TTS providers. Currently it supports Google TTS and Microsoft Windows SAPI. More integrations are planned.

There are two parts to this system, the application running on your computer that generates and plays the audio, and the in-world object that allows you to
create messages to be sent to the computer software. A modified version of the standard Mute Helper that is found in Neos Essentials has been created to work with this system.
You can get a copy of this modified Mute Helper by pasting the following link into your Neos window:

neosdb:///b49a42c5d2ce8d4bb516bf4fe27e3e28681bc61f5ad278926c3bcd03e2989a87.7zbson

## Usage

### Configuring Audio Output

The audio output device can be configured by running the `audio-output-selector.exe` utility located in the `audio-output-selector` subfolder. This utility will list all available audio outputs that can be used as a TTS playback target.
When you select an output, this updates the entry in `mpv/mpv.conf` to the correct device ID.

It is advised to install an [application like VB-Cable](https://vb-audio.com/Cable/) which provides you an dummy output that audio can be routed into.
Once installed you can set the output of VLC to the VB-Cable output, and specify that device as your microphone input in Neos.

### Running The Application

Once you have the modified Mute Helper installed to your avatar, launch the server executable, `neos-tts-server.exe`.

When you run for the first time, Windows Firewall may prompt you to allow the application through, click accept otherwise the server will not be able to communicate with Neos and/or Google.
The application should start and show "Server started on port X" where X is the port you configured (default is 7000).
Once the local server is started, check the settings in the Mute Helper menu, you should see a green section with a checkmark showing "Connected".
If you don't see the Mute Helper connected, try re-equipping an avatar that has the Mute Helper saved on it, or respawn.


## Configuration

Open the `config.ini` file in a text editor. This file is where you can change the TTS engine being used, and change settings for your current TTS engine choice. The INI file is includes comments to explain what each section and option does. If you make a mistake and want to revert your `config.ini`, you can always find a [fresh copy here](https://raw.githubusercontent.com/Zetaphor/neos-local-tts/master/config.ini).

### Google Text To Speech

**NOTE:** Using the Google TTS API requires the content of your messages to be sent to Google servers, where they will then be converted into audio. If you are not comfortable with this and prefer an entirely local provider, use the Microsoft SAPI engine instead.

The Google TTS engine supports multiple different regional accents. These can be configured in the `config.ini` under the Google section. Some regional accents may include translation for certain words.


### Microsoft SAPI

The Microsoft SAPI engine is built into Microsoft Windows and by default (in English distributions) includes a the David and Zira voices. Additional voices can be installed from the Voice Settings menu in Windows settings. [See this Microsoft Support article](https://support.microsoft.com/en-us/topic/download-voices-for-immersive-reader-read-mode-and-read-aloud-4c83a8d8-7486-42f7-8e46-2b0fdf753130) for more information on installing additional voices.

Additionally the speaking rate for any Microsoft voice can be configured in `config.ini`.

Currently the system has built-in support for the following English speaking voices:

* David (Installed by default in most English systems)
* Zira (Installed by default in most English systems)
* Hazel (Installed through Voice Settings)
* Mark (Installed from registry key)
* Eva (Installed from registry key)

Support for additional voices and languages can be added upon request, and/or will be added in future updates.

#### **Mark & Eva**

There are two additional US English voices available for Windows that are superior to the defaults in speaking quality, but for some reason are not available to be installed through the Voice Settings. These "hidden" voices can be enabled by installing the registry keys that allows windows to find their voice data. [A copy of these registry keys can be downloaded here](https://github.com/Zetaphor/neos-local-tts/raw/master/enable-eva-mark-voice-windows10.zip), and are included in this code repo. Extract the registry keys and double click them to install to your system registry. Once you've done this both the Mark and Eva options will be available to your system.


## Developers

This application was built with Python 3.10.8 and pip 22.3.1 on Windows 10.
It bundles a build of `mpv-x86_64-20221106-git-2590651` from https://mpv.io/

Binaries are created with PyInstaller 5.6.2

Contributions and issues are welcome!

### Building from source

Install requirements:

```pip install -r requirements.txt```

Build a new distributable with PyInstaller

```python -m PyInstaller neos-tts-server.py```

A batch script is provided to run this command