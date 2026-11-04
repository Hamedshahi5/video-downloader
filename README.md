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
---

## 🇮🇷 توضیحات فارسی

# 🐍 دانلودر ویدیو آنلاین

یک ابزار ساده، رایگان و قدرتمند برای دانلود ویدیو از **بیش از ۱۰۰۰ وب‌سایت** با استفاده از [yt-dlp](https://github.com/yt-dlp/yt-dlp).

پشتیبانی از YouTube، Instagram، Vimeo، TikTok، Twitter/X، Facebook، Reddit و بسیاری دیگر.

## ✨ ویژگی‌ها

- 🌍 پشتیبانی از ۱۰۰۰+ سایت (با yt-dlp)
- 🎚 انتخاب کیفیت: `best`، `worst`، `720p`، `1080p`
- 📦 ادغام خودکار ویدیو + صدا به MP4
- 🚫 بدون نیاز به نصب (فقط Python + yt-dlp)
- 💯 رایگان و متن‌باز

## 📥 نحوهٔ استفاده

```bash
python3 video_downloader.py "URL" --quality 720p
```

### گزینه‌ها

| گزینه | توضیح | پیش‌فرض |
|---|---|---|
| `URL` | آدرس ویدیو | (الزامی) |
| `--quality` | `best`، `worst`، `720p`، `1080p` | `best` |
| `--output-dir` | پوشهٔ خروجی | `~/hermes-work/downloads` |

### مثال‌ها

```bash
# دانلود بهترین کیفیت
python3 video_downloader.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# دانلود 720p
python3 video_downloader.py "https://www.instagram.com/reel/XXXX/" --quality 720p
```

## ⚠️ نکات

- YouTube ممکن است به دلیل bot detection نیاز به cookies داشته باشد. از `--cookies-from-browser` استفاده کنید.
- برای فایل‌های بزرگ، Telegram Bot API محدودیت ۵۰ MB دارد؛ با ffmpeg فشرده کنید.

## 📱 کانال تلگرام

به کانال تلگرام ما بپیوندید برای ابزارهای مفید بیشتر و به‌روزرسانی‌ها:

👉 **[@mytools47](https://t.me/mytools47)**

## 📄 مجوز

MIT License — آزاد برای استفاده، تغییر و توزیع.

## 🙏 اعتبار

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — موتور دانلود قدرتمند
- ساخته شده با ❤️ توسط [Hamed](https://github.com/Hamedshahi5)
