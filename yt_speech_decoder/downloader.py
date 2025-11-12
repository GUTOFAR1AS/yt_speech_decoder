import yt_dlp
import os

def download_audio(url: str) -> str:
    """
    Faz o download do áudio de um vídeo do YouTube e retorna o caminho do arquivo MP3.
    """
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Caminho correto do FFmpeg instalado via Chocolatey
        'ffmpeg_location': r'C:\ProgramData\chocolatey\lib\ffmpeg\tools\ffmpeg\bin',
        'quiet': False,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("\nBaixando áudio...")
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        mp3_path = os.path.splitext(filename)[0] + ".mp3"
        print(f"\nÁudio salvo em: {mp3_path}")
        return mp3_path
