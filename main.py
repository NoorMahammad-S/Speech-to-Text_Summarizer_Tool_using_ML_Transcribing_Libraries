import speech_recognition as sr
from gensim.summarization import summarize

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def summarize_text(text):
    summary = summarize(text)
    return summary

def main():
    audio_path = "path/to/your/audio/file.wav"

    # Step 1: Transcribe audio to text
    transcribed_text = transcribe_audio(audio_path)

    if transcribed_text:
        # Step 2: Summarize the transcribed text
        summarized_text = summarize_text(transcribed_text)

        # Step 3: Display the results
        print("Transcribed Text:")
        print(transcribed_text)
        print("\nSummarized Text:")
        print(summarized_text)
    else:
        print("Failed to transcribe the audio.")

if __name__ == "__main__":
    main()
