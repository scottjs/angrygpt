# AngryGPT

A silly project I created to play around with the GPT 4 API, this started as an experiment to see if I could get a normal continuous conversation working with the Siri prompt, but then it turned into whatever the hell this is. 

The results are honestly just hilarious to me, see the [video demo](https://www.youtube.com/watch?v=kLlTWm_SpRk). 

## Introduction

This is a MacOS shortcut that allows you to have a continuous conversation with GPT-4 via the Siri interface, using Python.

A simple python is used to generate a unique conversation ID that keeps track of each message within chat session, the conversation is reset when a new Siri chat is started. 

The GPT system message has been set to instruct the chatbot to be offensive, insulting and to include lots of swearing. Feel free to change the system prompt however you like.

Text responses are then optionally piped into the [elevenlabs.io](https://beta.elevenlabs.io) text to speach voice synthesis API, which changes the tone of the voice based on context.

**Note:** Conversations are stored in `~/conversations.json`, you can change this location in the Python script, line 27.

## How to use with the default Siri voice (easy)

This will use Siri's own voice to read back the responses from GPT. This is easier to set up.

**Prerequisites:**

1. Python3
2. OpenAI packages, run `pip install openai requests`
3. An [openai.com](https://platform.openai.com/account/api-keys) API key
4. Ensure that Siri's **Voice Feedback** option is enabled in **System Preferences** > **Siri** 

**To set up:**

1. Checkout this repo somewhere.
2. Edit the `start_conversation.py` file and add your OpenAI API key, line 8
3. Download the MacOS shortcut from [here](https://www.icloud.com/shortcuts/c60a78691ed84e30a7eea9b71c1b3183).
4. Open the shortcut
   - Edit the two `Shell Script` shortcut actions and update the location of the `start_conversation.py` file, also make sure the python command is correct. The default location is set to your home directory.
   - Remove the `AppleScript` action from the shortcut.

**To use:**

1. Start Siri and say "Activate AngryGPT", or whatever you decided to call the shortcut
2. Start talking to Siri

## How to use with ElevenLabs voice (less easy)

Similar to the above, but this will replace the default Siri voice with a synthesied voice from ElevenLabs.

**Prerequisites:**

1. Python3
2. OpenAI packages, run `pip install openai requests`
3. FFmpeg, run `brew install ffmpeg`
4. An [elevenlabs.io](https://beta.elevenlabs.io) API key
5. An [openai.com](https://platform.openai.com/account/api-keys) API key
6. Disable Siri's **Voice Feedback** option in **System Preferences** > **Siri** 
   - This is a total hack but important, otherwise Siri's own voice overrides the ElevenLabs stream

**To set up:**

1. Checkout this repo somewhere.
2. Edit the `start_conversation.py` file and add your OpenAI API key, line 8
3. Download the MacOS shortcut from [here](https://www.icloud.com/shortcuts/c60a78691ed84e30a7eea9b71c1b3183).
4. Open the shortcut
   - Edit the two `Shell Script` shortcut actions and update the location of the `start_conversation.py` file, also make sure the python command is correct. The default location is set to your home directory.
   - Edit the `AppleScript` action to add your ElevenLabs API key 
   - Check to make sure the `ffmpeg` and `ffplay` commands in the `AppleScript` are pointing to the correct location on your machine, you can run the command `which ffmpeg` and `which ffplay` to find the full path and set them accordingly

**To use:**

1. Start Siri and say "Activate AngryGPT", or whatever you decided to call the shortcut
2. Click the Siri logo and start talking

## Changing the ElevenLabs voice

You can change the ElevenLabs voice by editing the the `AppleScript` and changing the following line:

```
set apiUrl to "https://api.elevenlabs.io/v1/text-to-speech/MF3mGyEYCl7XYWbV9V6O/stream"
```

The value `MF3mGyEYCl7XYWbV9V6O` is the voice ID being used, you can query for a list of available voices (or even upload your own) by using the `v1/voices` endpoint and then update the line above with the new ID, see the official docs [here](https://api.elevenlabs.io/docs). 

You can also tweak the voice setting values for stability and similarity.

## Apple Shortcut

Download the MacOS shortcut from [here](https://www.icloud.com/shortcuts/c60a78691ed84e30a7eea9b71c1b3183).

<img width="610" alt="Screenshot 2023-04-12 at 23 52" src="https://user-images.githubusercontent.com/994732/231603864-e80bf0fc-5324-4370-9f11-11b4c5852145.png">
