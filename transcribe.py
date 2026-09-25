#
# Function Example 
# transcribe "https://www.youtube.com/watch?v=GwfMCDgMs_E"
#
# Script Example
# transcribe.py "https://www.youtube.com/watch?v=GwfMCDgMs_E"
#
import os
import sys
import time
from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_id(url):
    """Extract the YouTube video ID from a URL."""
    try:
        parsed=urlparse(url.strip())

        if parsed.hostname in ("www.youtube.com", "youtube.com", "m.youtube.com"):
            video_id=parse_qs(parsed.query).get("v", [None])[0]
            if video_id:
                return video_id

        if parsed.hostname in ("youtu.be", "www.youtu.be"):
            video_id=parsed.path.strip("/")
            if video_id:
                return video_id.split("/")[0]

    except Exception:
        pass

    return None

def fetch_transcript(url):
    video_id=get_video_id(url)

    if not video_id:
        return None, "Invalid YouTube URL."

    try:
        ytt_api=YouTubeTranscriptApi()

        transcript=ytt_api.fetch(video_id)

        formatter=TextFormatter()
        formatted_transcript=formatter.format_transcript(transcript)

        return formatted_transcript, None

    except Exception as e:
        return None, f"An error occurred: {e}"

def save_transcript(transcript):
    timestamp=time.strftime("%Y%m%d_%H%M%S")
    file_name=f"transcript_{timestamp}.txt"
    full_path=os.path.join(os.getcwd(), file_name)

    with open(full_path, "w", encoding="utf-8") as file:
        file.write(transcript)

    return full_path

def main():
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <YouTube_URL>")
        sys.exit(1)

    url=sys.argv[1]

    transcript, error=fetch_transcript(url)

    if error:
        print(error)
        sys.exit(1)

    print(transcript)

    full_path=save_transcript(transcript)

    print(f"\nTranscript saved as {full_path}")

if __name__ == "__main__":
    main()
