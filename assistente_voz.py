import os
from dotenv import load_dotenv
import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from openai import OpenAI
from gtts import gTTS
from playsound import playsound
import tempfile

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not os.getenv("OPENAI_API_KEY"):
    print("❌ ERRO: Crie o arquivo .env com sua OPENAI_API_KEY")
    exit()

print("🔄 Carregando modelo Whisper (pode demorar na primeira vez)...")
model = whisper.load_model("small")

def record_audio(duration=8, fs=44100):
    print(f"\n🎤 Gravando por {duration} segundos... Fale agora!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    filename = "input_audio.wav"
    write(filename, fs, recording)
    return filename

def transcribe_audio(audio_file):
    result = model.transcribe(audio_file, fp16=False, language="pt")
    return result["text"].strip()

def get_chatgpt_response(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content.strip()

def speak_response(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text=text, lang="pt", slow=False)
        tts.save(fp.name)
        playsound(fp.name)
        os.unlink(fp.name)

print("\n🤖 Assistente de Voz Inteligente - DIO")
print("Pressione ENTER para gravar sua pergunta ou digite 'sair' para encerrar.\n")

while True:
    comando = input("▶️  Pressione ENTER para falar (ou 'sair'): ").strip().lower()
    if comando == "sair":
        print("👋 Até mais!")
        break

    audio_file = record_audio()
    print("📝 Transcrevendo...")
    transcription = transcribe_audio(audio_file)
    
    if not transcription:
        print("❓ Não entendi. Tente novamente.")
        continue

    print(f"Você disse: {transcription}\n")
    print("💭 Pensando na resposta...")
    response_text = get_chatgpt_response(transcription)
    print(f"ChatGPT: {response_text}\n")
    
    print("🔊 Falando a resposta...")
    speak_response(response_text)
    print("✅ Pronto! Pressione ENTER para nova conversa.\n")
