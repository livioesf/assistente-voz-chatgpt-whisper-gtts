# 🤖 Assistente de Voz Inteligente com Whisper + ChatGPT + gTTS

Projeto desenvolvido como solução do desafio **"Conversando Por Voz Com o ChatGPT Utilizando Whisper (OpenAI) e Python"** da **Digital Innovation One (DIO)**.

## 🎯 O que o projeto faz

Este assistente permite uma conversa **completa por voz**:
- Grava sua voz pelo microfone
- Transcreve o áudio usando **Whisper** (OpenAI)
- Envia a transcrição para o **ChatGPT** e recebe uma resposta inteligente
- Converte a resposta em áudio usando **gTTS** (Google Text-to-Speech)
- Reproduz automaticamente a resposta em voz

Tudo funcionando em **português (pt-BR)**.

## 🛠️ Tecnologias utilizadas

- **Python**
- **Whisper** (OpenAI) — Reconhecimento de fala (Speech-to-Text)
- **OpenAI API** — ChatGPT (gpt-3.5-turbo)
- **gTTS** — Síntese de voz (Text-to-Speech)
- **sounddevice + scipy** — Gravação de áudio
- **python-dotenv** — Gerenciamento seguro da API key

## 🚀 Como executar o projeto

### 1. Pré-requisitos
- Instale o **FFmpeg** (necessário para o Whisper):
  - Windows: Baixe em https://www.gyan.dev/ffmpeg/builds/
  - Linux: `sudo apt install ffmpeg`
  - Mac: `brew install ffmpeg`

### 2. Clone o repositório
pip install -r requirements.txtgit clone https://github.com/SEU_USUARIO/assistente-voz-chatgpt-whisper-gtts.git
cd assistente-voz-chatgpt-whisper-gtts
