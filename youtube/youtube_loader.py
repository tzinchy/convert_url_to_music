import yt_dlp

def download_audio_as_mp3(youtube_url, output_folder='cache'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
        'postprocessors': [],  # Без постпроцессоров, чтобы избежать использования ffmpeg
        'prefer_ffmpeg': False,  # Отключаем использование ffmpeg
        'keepvideo': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            title = info_dict.get('title', None)
            file_path = ydl.prepare_filename(info_dict)
            return file_path, title
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None, None

