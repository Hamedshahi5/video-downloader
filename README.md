# 🐍 Online Video Downloader

A simple, free, and powerful Python tool to download videos from **1000+ websites** using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

Supports YouTube, Instagram, Vimeo, TikTok, Twitter/X, Facebook, Reddit, and many more.

## ✨ Features

- 🌍 Supports 1000+ sites (powered by yt-dlp)
- 🎚 Quality selection: `best`, `worst`, `720p`, `1080p`
- 📦 Auto-merge to MP4 (video + audio)
- 🚫 No installation required (just Python + yt-dlp)
- 💯 Free and open-source

## 📥 Usage

```bash
python3 video_downloader.py "URL" --quality 720p
```

### Options

| Option | Description | Default |
|---|---|---|
| `URL` | Video URL | (required) |
| `--quality` | `best`, `worst`, `720p`, `1080p` | `best` |
| `--output-dir` | Output directory | `~/hermes-work/downloads` |

### Examples

```bash
# Download best quality
python3 video_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download 720p
python3 video_downloader.py "https://www.instagram.com/reel/XXXX/" --quality 720p

# Custom output dir
python3 video_downloader.py "URL" --output-dir ./videos
```

## ⚠️ Notes

- YouTube may require cookies due to bot detection. Use `--cookies-from-browser` if needed.
- For large files, Telegram Bot API has a 50MB limit; use ffmpeg to compress if needed.

## 📱 Telegram Channel

Join our Telegram channel for more useful tools and updates:

👉 **[@mytools47](https://t.me/mytools47)**

## 📄 License

MIT License — free to use, modify, and distribute.

## 🙏 Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — the powerful download engine
- Built with ❤️ by [Hamed](https://github.com/Hamedshahi5)