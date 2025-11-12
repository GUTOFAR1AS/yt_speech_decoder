from yt_speech_decoder import download_audio, AudioTranscriber

def main():
    print("Baixar e transcrever áudio do YouTube")
    url = input("Cole o link do vídeo: ").strip()

    print("\nBaixando áudio...")
    audio_path = download_audio(url)

    print("\nIniciando transcrição...")
    transcriber = AudioTranscriber(model_name="base")
    text = transcriber.transcribe(audio_path)

    print("\nTranscrição completa:")
    print("=" * 60)
    print(text)
    print("=" * 60)

if __name__ == "__main__":
    main()
