import os
import speech_recognition as sr
from gensim.summarization import summarize


def transcribe_audio(audio_path):
    if not os.path.exists(audio_path):
        print(f"Error: Audio file not found at {audio_path}")
        return None

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        try:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Error: Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error: Could not request results from Google Speech Recognition service; {e}")

    return None


def summarize_text(text):
    if text:
        summary = summarize(text)
        return summary
    else:
        return None


def main():
    audio_path = "path/to/your/audio/file.wav"

    # Step 1: Transcribe audio to text
    transcribed_text = transcribe_audio(audio_path)

    if transcribed_text:
        # Step 2: Summarize the transcribed text
        summarized_text = summarize_text(transcribed_text)

        if summarized_text:
            # Step 3: Display the results
            print("Transcribed Text:")
            print(transcribed_text)
            print("\nSummarized Text:")
            print(summarized_text)
        else:
            print("Failed to summarize the transcribed text.")
    else:
        print("Failed to transcribe the audio.")


if __name__ == "__main__":
    main()
