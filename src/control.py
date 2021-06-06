import speech_recognition as sr

global text


def recognize():
    global text

    languages = {
        0: 'en-US',
        1: 'en-IN',
        2: 'bn-BD'
    }

    # Select the microphone as source.
    with sr.Microphone() as source:
        try:
            print('Please say something...')
            # print(source.list_microphone_names())
            r = sr.Recognizer()

            # Get the audio from the source within timeout seconds.
            audio = r.listen(source=source, timeout=2)

            # Get the text from the audio in the specified language.
            text = r.recognize_google(audio_data=audio, language=languages[1])
            if text:
                print(f'Your speech: {text}')

        except sr.WaitTimeoutError as e:
            recognize()

        except sr.UnknownValueError as e:
            print(e)

    recognize()


if __name__ == "__main__":
    recognize()
