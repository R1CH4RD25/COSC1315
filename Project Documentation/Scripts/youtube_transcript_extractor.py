"""
YouTube Transcript Extractor for Educational Content
----------------------------------------------------
This script helps extract transcripts from YouTube videos for creating
educational materials like lesson plans, study guides, and objectives.

IMPORTANT: Requires youtube-transcript-api v1.2.3 or later
    pip install --upgrade youtube-transcript-api

Updated: October 2025 for new API syntax

Dependencies:
    pip install youtube-transcript-api

Usage Examples:
    1. Extract transcript from a specific time range:
       python youtube_transcript_extractor.py VIDEO_ID 6:08 8:08

    2. Extract full transcript:
       python youtube_transcript_extractor.py VIDEO_ID

    3. Save to file:
       python youtube_transcript_extractor.py VIDEO_ID --output lesson_01.txt
"""

import sys
import argparse
from datetime import datetime


def parse_timestamp(timestamp_str):
    """
    Convert timestamp string to seconds.
    Supports formats: MM:SS, H:MM:SS, HH:MM:SS
    
    Examples:
        "6:08" -> 368 seconds
        "1:20:40" -> 4840 seconds
    """
    parts = timestamp_str.split(':')
    parts = [int(p) for p in parts]
    
    if len(parts) == 2:  # MM:SS
        return parts[0] * 60 + parts[1]
    elif len(parts) == 3:  # H:MM:SS or HH:MM:SS
        return parts[0] * 3600 + parts[1] * 60 + parts[2]
    else:
        raise ValueError(f"Invalid timestamp format: {timestamp_str}")


def format_seconds(seconds):
    """Convert seconds to readable timestamp."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"


def extract_transcript(video_id, start_time=None, end_time=None):
    """
    Extract transcript from YouTube video using NEW API (v1.2.3+).
    
    Args:
        video_id: YouTube video ID (from URL)
        start_time: Start timestamp in seconds (optional)
        end_time: End timestamp in seconds (optional)
    
    Returns:
        Formatted transcript text
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("ERROR: youtube-transcript-api not installed!")
        print("Install it with: pip install --upgrade youtube-transcript-api")
        sys.exit(1)
    
    try:
        # NEW API: Create instance first
        api = YouTubeTranscriptApi()
        
        # Fetch transcript (returns FetchedTranscript object)
        transcript = api.fetch(video_id)
        
        # Filter by time range if specified
        filtered = []
        for entry in transcript:
            # entry has: text, start, duration (as attributes, not dict keys)
            entry_start = entry.start
            entry_end = entry.start + entry.duration
            
            # Check if entry overlaps with desired range
            if start_time is not None and entry_end < start_time:
                continue
            if end_time is not None and entry_start > end_time:
                break
                
            filtered.append(entry)
        
        # Use filtered list or full transcript
        entries_to_format = filtered if filtered else transcript
        
        # Format transcript
        result = []
        for entry in entries_to_format:
            timestamp = format_seconds(int(entry.start))
            text = entry.text
            result.append(f"[{timestamp}] {text}")
        
        return '\n'.join(result)
        
    except AttributeError as e:
        print(f"ERROR: You may have an old version of youtube-transcript-api")
        print(f"Update with: pip install --upgrade youtube-transcript-api")
        print(f"Details: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR extracting transcript: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Extract YouTube video transcripts for educational content creation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Extract transcript for Lesson 01 (6:08-8:08):
    python youtube_transcript_extractor.py _uQrJ0TkZlc 6:08 8:08
  
  Extract full video transcript:
    python youtube_transcript_extractor.py _uQrJ0TkZlc
  
  Save to file:
    python youtube_transcript_extractor.py _uQrJ0TkZlc 6:08 8:08 --output lesson_01.txt
        """
    )
    
    parser.add_argument('video_id', help='YouTube video ID (from URL)')
    parser.add_argument('start', nargs='?', help='Start timestamp (MM:SS or H:MM:SS)')
    parser.add_argument('end', nargs='?', help='End timestamp (MM:SS or H:MM:SS)')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    # Parse timestamps
    start_time = None
    end_time = None
    
    if args.start:
        start_time = parse_timestamp(args.start)
    if args.end:
        end_time = parse_timestamp(args.end)
    
    # Extract transcript
    print(f"Extracting transcript from video: {args.video_id}")
    if start_time or end_time:
        print(f"Time range: {args.start or '0:00'} to {args.end or 'end'}")
    
    transcript = extract_transcript(args.video_id, start_time, end_time)
    
    # Output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(transcript)
        print(f"\nTranscript saved to: {args.output}")
    else:
        print("\n" + "="*70)
        print(transcript)
        print("="*70)


if __name__ == '__main__':
    main()
