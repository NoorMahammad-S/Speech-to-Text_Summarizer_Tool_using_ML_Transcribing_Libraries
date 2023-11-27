# Speech to Text Summarizer Tool using ML Transcribing Libraries

This Python script serves as a Speech Summarizer Tool that utilizes Google Speech Recognition for audio transcription and Gensim's summarization module for generating summaries of the transcribed text.

## Prerequisites

Make sure you have Python installed on your machine. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/NoorMahammad-S/Speech-to-Text_Summarizer_Tool_using_ML_Transcribing_Libraries.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Speech-to-Text_Summarizer_Tool_using_ML_Transcribing_Libraries
   ```

3. Place your audio file in the project directory and update the `audio_path` variable in the script with the correct file path.

4. Run the script:

   ```bash
   python main.py
   ```

## Project Structure

- `main.py`: The main Python script.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `requirements.txt`: Lists the Python packages required for the project.
- `README.md`: This file.

## Notes

- The script uses Google Speech Recognition for audio transcription and Gensim for text summarization.
- Ensure that your audio file is in a supported format (e.g., WAV) and located in the specified path.
- The summarization process may vary in effectiveness depending on the content and length of the transcribed text.
