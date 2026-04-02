import os
import playsound as sa
from elevenlabs import Voices, TTS


API_KEY = "Put your API here"


os.environ["ELEVENLABS_API_KEY"] = API_KEY


def speak(text, voice_index=0):
    """
    Convert text to speech and play it.
    voice_index: choose which ElevenLabs voice to use
    """
    voices_list = Voices.get(api_key=API_KEY)  # get available voices
    if not voices_list:
        print("No voices available.")
        return
    
    if voice_index >= len(voices_list):
        voice_index = 0  # fallback
    
    voice = voices_list[voice_index]
    tts = TTS(voice=voice, api_key=API_KEY)
    
    # Generate audio bytes
    audio_bytes = tts.speak(text)
    
 
    play_obj = sa.play_buffer(audio_bytes, 1, 2, 22050)
    play_obj.wait_done()


speak("Hello! I am your AI assistant. How can I help you today?")


    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        speak("Goodbye! Have a great day!")
        break
    
   
    response = f"You said: {user_input}"
    print(response)
    speak(response)
