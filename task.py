import os
from pydub import AudioSegment
import speech_recognition as sr

print('--- Sistema de transcrição de áudio para texto ---')

audioOrigem = 'audio.ogg'
audioWav = 'audio.wav'

try:
    print(f'Convertendo {audioOrigem} para .wav')
    audio = AudioSegment.from_file(audioOrigem, format='ogg')
    
    audio.export(audioWav, format='WAV')
    print('Formato WAV concluído')
    
    reconhecedor = sr.Recognizer()
    
    with sr.AudioFile(audioWav) as fonteAudio:
    
        dadosAudio = reconhecedor.record(fonteAudio)
        
        print('Iniciando transcrição via API Google')
        transcricao = reconhecedor.recognize_google(dadosAudio, language = 'PT-BR')

        print('Transcrição concluída')
        print(transcricao)
    
except sr.UnknownValueError:
    print('Ocorreu um erro, Google não entendeu o áudio')
except sr.RequestError as e:
    print(f'\nOcorreu um erro para ligar ao serviço Google: {e}')
except FileNotFoundError:
    print(f"\nERRO: Ficheiro não encontrado")
except Exception as e:
    print(f"\nERRO Inesperado: {e}")
    
finally:
    if os.path.exists(audioWav):
        os.remove(audioWav)
        print(f'Arquivo temporário {audioWav} apagado')