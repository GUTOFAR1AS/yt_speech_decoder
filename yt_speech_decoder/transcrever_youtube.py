# SALVE COMO: TurboTranscriber_Pro.py
# ==============================================
# TURBO TRANSCRITOR PROFISSIONAL v2.0
# - Áudio .mp3 mantido
# - Logs 100% limpos
# - Texto completo em segundos
# ==============================================

import yt_dlp
import whisper
import os
import sys
from datetime import datetime
from pathlib import Path

# === CONFIGURAÇÕES PROFISSIONAIS ===
OUTPUT_DIR = Path("Transcrições")
OUTPUT_DIR.mkdir(exist_ok=True)

# Logger profissional
class Logger:
    def debug(self, msg): pass
    def info(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): print(f"[ERRO] {msg}")

# === INÍCIO ===
print("\n" + "═" * 60)
print("   TURBO TRANSCRITOR PROFISSIONAL v2.0")
print("   Extrai 100% do áudio em segundos")
print("   Áudio .mp3 salvo permanentemente")
print("═" * 60)

url = input("\nCole o link do vídeo: ").strip()
if not url:
    sys.exit("Link vazio!")

print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Iniciando download...")

# === DOWNLOAD SILENCIOSO E RÁPIDO ===
ydl_opts = {
    'format': '140/139/141',           # m4a 128kbps ou menor (ultra rápido)
    'outtmpl': 'audio_temp.m4a',
    'quiet': True,
    'no_warnings': True,
    'noplaylist': True,
    'logger': Logger(),
    'extractor_args': {'youtube': 'player_client=default'},
}

try:
    yt_dlp.YoutubeDL(ydl_opts).download([url])
except Exception as e:
    sys.exit(f"Erro no download: {e}")

# === CONVERTE PARA MP3 (salva permanentemente) ===
print(f"[{datetime.now().strftime('%H:%M:%S')}] Convertendo para MP3 (salvo na pasta)...")
os.system('ffmpeg -y -i audio_temp.m4a -vn -acodec libmp3lame -q:a 2 "áudio_original.mp3" >nul 2>&1')
os.remove("audio_temp.m4a")

if not os.path.exists("áudio_original.mp3"):
    sys.exit("Falha ao gerar MP3")

# === CARREGA MODELO TURBO (mais rápido do mundo) ===
print(f"[{datetime.now().strftime('%H:%M:%S')}] Carregando modelo Whisper TURBO...")
model = whisper.load_model("turbo", device="cpu")

# === TRANSCRIÇÃO ULTRA RÁPIDA ===
print(f"[{datetime.now().strftime('%H:%M:%S')}] Extraindo TODO o texto (aguarde segundos)...")
inicio = datetime.now()

result = model.transcribe(
    "áudio_original.mp3",
    language=None,
    verbose=False,
    temperature=0.0,
    compression_ratio_threshold=2.4,
    logprob_threshold=-1.0,
    no_speech_threshold=0.6,
    condition_on_previous_text=False,
    fp16=False
)

fim = datetime.now()
duracao = (fim - inicio).total_seconds()

texto = result["text"].strip()
idioma = result.get("language", "desconhecido").upper()

# === NOME DO ARQUIVO PROFISSIONAL ===
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nome_txt = OUTPUT_DIR / f"[{timestamp}]_{idioma}_Transcrição.txt"
nome_mp3 = "áudio_original.mp3"

# === SALVA TRANSCRIÇÃO ===
with open(nome_txt, "w", encoding="utf-8") as f:
    f.write(f"TRANSCRIÇÃO AUTOMÁTICA - TURBO v2.0\n")
    f.write(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    f.write(f"Link: {url}\n")
    f.write(f"Idioma detectado: {idioma}\n")
    f.write(f"Tempo de processamento: {duracao:.1f} segundos\n")
    f.write(f"Tamanho do texto: {len(texto):,} caracteres\n")
    f.write(f"Áudio salvo como: {nome_mp3}\n")
    f.write("="*70 + "\n\n")
    f.write(texto)

# === RESULTADO FINAL ===
print("\n" + "═" * 60)
print("   SUCESSO! TRANSCRIÇÃO COMPLETA")
print("═" * 60)
print(f"   Tempo total: {duracao:.1f} segundos")
print(f"   Idioma: {idioma}")
print(f"   Arquivo de texto: {nome_txt.name}")
print(f"   Áudio MP3 salvo: áudio_original.mp3")
print(f"   Pasta: {OUTPUT_DIR.resolve()}")
print("═" * 60)

# Abre automaticamente
try:
    os.startfile(nome_txt)
    os.startfile("áudio_original.mp3")
except:
    try:
        os.system(f"open '{nome_txt}'")
        os.system(f"open 'áudio_original.mp3'")
    except:
        pass

print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Finalizado com sucesso!")
input("\nPressione ENTER para fechar...")