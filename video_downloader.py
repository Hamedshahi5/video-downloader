#!/usr/bin/env python3
"""Online Video Downloader — powered by yt-dlp.

Download videos from 1000+ websites (YouTube, Instagram, Vimeo, TikTok, ...).

Usage:
    python3 video_downloader.py "URL" [options]
"""
import argparse
import glob
import json
import os
import sys

# Locate yt-dlp installed under Hermes tools python
for _sp in glob.glob("/home/ubuntu/.hermes/tools/python-*/lib/python*/site-packages"):
    if _sp not in sys.path:
        sys.path.insert(0, _sp)

try:
    import yt_dlp
except ImportError:
    print("❌ yt-dlp not found. Install: pip install yt-dlp", file=sys.stderr)
    sys.exit(1)


CONFIG_PATH = os.path.expanduser("~/.config/video-downloader/config.json")
DEFAULT_OUTPUT = os.path.expanduser("~/hermes-work/downloads")


def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH) as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_config(cfg):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)


def progress_hook(d):
    if d["status"] == "downloading":
        pct = d.get("_percent_str", "").strip()
        speed = d.get("_speed_str", "").strip()
        eta = d.get("_eta_str", "").strip()
        print(f"\r  ⬇ {pct} at {speed} ETA {eta}   ", end="", flush=True)
    elif d["status"] == "finished":
        print(f"\r  ✅ Downloaded: {os.path.basename(d['filename'])}          ")


def download(url, output_dir=DEFAULT_OUTPUT, quality="best", audio_only=False,
            subtitles=False, playlist=False, cookies_browser=None):
    output_dir = os.path.expanduser(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    if audio_only:
        fmt = "bestaudio/best"
        outtmpl = os.path.join(output_dir, "%(title)s.%(ext)s")
        postprocessors = [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}]
    else:
        if quality == "best":
            fmt = "bestvideo+bestaudio/best"
        elif quality == "worst":
            fmt = "worst"
        elif quality.endswith("p"):
            h = quality[:-1]
            fmt = f"bestvideo[height<={h}]+bestaudio/best[height<={h}]/best"
        else:
            fmt = "best"
        outtmpl = os.path.join(output_dir, "%(title)s.%(ext)s")
        postprocessors = [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}]

    opts = {
        "format": fmt,
        "outtmpl": outtmpl,
        "noplaylist": not playlist,
        "quiet": True,
        "no_warnings": True,
        "progress_hooks": [progress_hook],
        "postprocessors": postprocessors,
        "merge_output_format": "mp4",
    }

    if subtitles:
        opts["writesubtitles"] = True
        opts["writeautomaticsub"] = True
        opts["subtitleslangs"] = ["all"]
        opts["embedsubtitles"] = True

    if cookies_browser:
        opts["cookiesfrombrowser"] = (cookies_browser,)

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        if "entries" in info:
            entries = [e for e in info["entries"] if e]
            print(f"\n✅ Playlist: {len(entries)} videos downloaded.")
            for e in entries:
                print(f"   - {e.get('title')}")
            return [ydl.prepare_filename(e) for e in entries]
        filename = ydl.prepare_filename(info)
        base, _ = os.path.splitext(filename)
        mp4 = base + ".mp4"
        if os.path.exists(mp4):
            filename = mp4
        mp3 = base + ".mp3"
        if audio_only and os.path.exists(mp3):
            filename = mp3
        print(f"\n✅ Downloaded: {filename}")
        print(f"   Title: {info.get('title')}")
        if info.get("duration"):
            print(f"   Duration: {info['duration']}s")
        return filename


def list_formats(url):
    opts = {"quiet": True, "no_warnings": True, "skip_download": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(f"Title: {info.get('title')}")
        print(f"Duration: {info.get('duration')}s\n")
        print("Available formats:")
        print(f"{'ID':<12} {'EXT':<6} {'RESOLUTION':<12} {'VCODEC':<12} {'ACODEC':<12}")
        print("-" * 60)
        for f in info.get("formats", []):
            print(f"{f.get('format_id',''):<12} {f.get('ext',''):<6} {str(f.get('resolution','')):<12} {str(f.get('vcodec',''))[:12]:<12} {str(f.get('acodec',''))[:12]:<12}")


def main():
    parser = argparse.ArgumentParser(
        description="Download online videos from 1000+ sites",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  %(prog)s "URL" --quality 720p
  %(prog)s "URL" --audio-only
  %(prog)s "URL" --subtitles
  %(prog)s "URL" --list-formats
  %(prog)s "URL" --playlist
        """,
    )
    parser.add_argument("url", nargs="?", help="Video URL")
    parser.add_argument("--output-dir", default=None, help="Output directory")
    parser.add_argument("--quality", default="best", choices=["best", "worst", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"], help="Video quality")
    parser.add_argument("--audio-only", action="store_true", help="Download audio only (MP3)")
    parser.add_argument("--subtitles", action="store_true", help="Download and embed subtitles")
    parser.add_argument("--playlist", action="store_true", help="Download entire playlist")
    parser.add_argument("--cookies-browser", metavar="BROWSER", help="Browser to extract cookies from (chrome, firefox, ...)")
    parser.add_argument("--list-formats", action="store_true", help="List available formats without downloading")
    parser.add_argument("--config", action="store_true", help="Show config file path")
    args = parser.parse_args()

    cfg = load_config()
    output_dir = args.output_dir or cfg.get("output_dir", DEFAULT_OUTPUT)

    if args.config:
        print(f"Config file: {CONFIG_PATH}")
        print(json.dumps(cfg, indent=2, ensure_ascii=False))
        return

    if not args.url:
        parser.print_help()
        return

    if args.list_formats:
        list_formats(args.url)
        return

    try:
        download(args.url, output_dir, args.quality, args.audio_only,
                args.subtitles, args.playlist, args.cookies_browser)
    except KeyboardInterrupt:
        print("\n⚠️  Cancelled by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()