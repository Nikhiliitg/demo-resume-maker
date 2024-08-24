from gtts import gTTS
import os

def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("mpg321 output.mp3")  # On Mac/Linux you may need to install mpg321 or afplay
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Text-to-Speech system! Type 'exit' to quit.")
    while True:
        user_input = input("Enter text to convert to speech: ")

        if user_input.lower() == "exit":
            print("Exiting the TTS system.")
            break

        text_to_speech(user_input)


