import yt_dlp
import os
import whisper

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


def transcrever_audio(caminho_audio: str) -> str:
    """
    Transcreve o áudio usando Whisper e salva o resultado em um arquivo .txt.
    """
    print("\nTranscrevendo o áudio...")
    model = whisper.load_model("small")
    result = model.transcribe(caminho_audio, language="pt")
    texto = result["text"]

    print("\nTranscrição completa!\n")
    print(texto)

    # Salva em .txt no mesmo diretório do áudio
    txt_path = os.path.splitext(caminho_audio)[0] + ".txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"\nTranscrição salva em: {txt_path}")
    return texto


if __name__ == "__main__":
    url = input("Cole a URL do vídeo do YouTube: ").strip()
    caminho_mp3 = download_audio(url)
    transcrever_audio(caminho_mp3)
