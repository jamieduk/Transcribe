# YouTube Transcribe Python App

**Transcribe Python App** by **(c) J~Net 2024**

Automatically transcribe YouTube videos from the command line using Python.

**GitHub:** https://github.com/jamieduk/Transcribe
**Website:** https://jnetai.com

---

## Features

* 🎥 Transcribe YouTube videos from a URL
* 🐍 Python-based
* ⚙️ Simple automated setup
* 🚀 Start transcription with a single command
* 📄 Outputs the transcription for easy use

---

## Requirements

* Linux
* Python 3
* Internet connection
* A YouTube video with available transcripts

The setup script will install the required Python dependencies.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jamieduk/Transcribe.git
cd Transcribe
```

Set permission to run the setup and start scripts:

```bash
chmod +x *.sh
```

Run the setup:

```bash
./setup.sh
```

Once setup has completed, the application is ready to transcribe YouTube videos.

---

## Usage

Start a transcription by providing a YouTube video URL:

```bash
./start.sh "URL"
```

### Example

```bash
./start.sh "https://www.youtube.com/watch?v=_Sq5RqP27NY"
```

---

## How It Works

1. `setup.sh` prepares the Python environment and installs the required dependencies.
2. `start.sh` receives the YouTube URL.
3. The Python transcription application extracts the video ID.
4. The available YouTube transcript is retrieved.
5. The transcript is formatted and output for use.

---

## Project Structure

```text
Transcribe/
├── setup.sh
├── start.sh
├── transcribe.py
└── README.md
```

---

## Troubleshooting

### Permission denied

If you receive a permission error when running the scripts:

```bash
chmod +x *.sh
```

Then run the setup again:

```bash
./setup.sh
```

### No transcript available

Not every YouTube video has a transcript available. If the video does not provide a usable transcript, the application cannot retrieve one.

---

## License

Copyright © 2024 J~Net

https://jnetai.com

---

## Author

**J~Net**

GitHub: https://github.com/jamieduk/Transcribe

Website: https://jnetai.com
