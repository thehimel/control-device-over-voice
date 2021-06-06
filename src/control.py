import speech_recognition as sr


def recognize():
    languages = {
        0: 'en-US',
        1: 'en-IN',
        2: 'bn-BD'
    }

    r = sr.Recognizer()

    # Select the microphone as source
    with sr.Microphone() as source:
        print('Please say something...')
        # print(source.list_microphone_names())

        # Get the audio
        audio = r.listen(source)

        try:
            # Get the text from the audio
            text = r.recognize_google(audio_data=audio, language=languages[2])
            print(f'Your speech: {text}')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    while True:
        recognize()
