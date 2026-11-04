#!/home/ubuntu/.hermes/tools/python-3.14.9+202****1021-linux-x64/bin/python3
"""Online video downloader using yt-dlp.

Usage:
    python3 video_downloader.py <URL> [--output-dir DIR] [--quality best|worst|720p|1080p]
"""
import argparse
import os
import sys

import glob, os, sys
# Locate yt_dlp's site-packages (installed under Hermes tools python)
for _sp in glob.glob("/home/ubuntu/.hermes/tools/python-*/lib/python*/site-packages"):
    if _sp not in sys.path:
        sys.path.insert(0, _sp)

import yt_dlp


def download(url, output_dir="~/hermes-work/downloads", quality="best"):
    output_dir = os.path.expanduser(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    if quality == "best":
        fmt = "bestvideo+bestaudio/best"
    elif quality == "worst":
        fmt = "worst"
    elif quality.endswith("p"):
        h = quality[:-1]
        fmt = f"bestvideo[height<={h}]+bestaudio/best[height<={h}]/best"
    else:
        fmt = "best"

    opts = {
        "format": fmt,
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        # adjust extension after merge
        base, _ = os.path.splitext(filename)
        mp4 = base + ".mp4"
        if os.path.exists(mp4):
            filename = mp4
        print(f"\n✅ Downloaded: {filename}")
        print(f"   Title: {info.get('title')}")
        print(f"   Duration: {info.get('duration')}s")
        return filename


def main():
    parser = argparse.ArgumentParser(description="Download online videos")
    parser.add_argument("url", help="Video URL")
    parser.add_argument("--output-dir", default="~/hermes-work/downloads", help="Output directory")
    parser.add_argument("--quality", default="best", help="Quality: best, worst, 720p, 1080p")
    args = parser.parse_args()
    try:
        download(args.url, args.output_dir, args.quality)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
