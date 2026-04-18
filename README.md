# 🤖 Assistente de Voz Inteligente - DIO Challenge

Projeto desenvolvido como **solução própria** do desafio **"Conversando por Voz com o ChatGPT utilizando Whisper (OpenAI) e Python"** da Digital Innovation One.

### ✨ O que o projeto faz
- Grava sua voz pelo microfone do computador
- Transcreve com **Whisper** (OpenAI)
- Envia a pergunta para o **ChatGPT** (gpt-3.5-turbo)
- Converte a resposta em voz com **gTTS** e reproduz automaticamente
- Totalmente em português (pt-BR)

### 🛠️ Tecnologias usadas
- Whisper (OpenAI)
- OpenAI API (ChatGPT)
- gTTS (Google Text-to-Speech)
- sounddevice + scipy (gravação de áudio)

### 🚀 Como executar
1. Instale o **ffmpeg** (obrigatório)
2. `pip install -r requirements.txt`
3. Renomeie `.env.example` para `.env` e coloque sua chave da OpenAI
4. `python assistente_voz.py`

Pressione **ENTER** para gravar e falar com o assistente.

**Projeto feito para destacar no portfólio!** 🚀
