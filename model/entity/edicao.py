import os
from pytube import YouTube
import moviepy.editor as mp
from pydub import AudioSegment

from vosk import Model, KaldiRecognizer,SetLogLevel
import wave
import json
import os
from model.entity.utilitarios import Utilitarios

class Edicao():
    def __init__(self,link_You_tube,palavra_chave) -> None:
        self.link_YouTube = link_You_tube
        self.caminho_salvar = os.path.abspath("view/static")
        self.palavra_chave = palavra_chave
        self.caminho_do_video = self.DownloadYouTube()
        self.lista_de_palavras_deste_video = None

    #Baixa o Vídeo do YouTube, informe o link do vídeo e o local a ser salvo.
    def DownloadYouTube(self):
        yt = YouTube(self.link_YouTube)
        yt.streams.first().download(self.caminho_salvar)
        

        return yt.streams.first().url
    
    def identificaPalavraNoTempo(self):

        SetLogLevel(-1)

        model = Model('vosk-model-small-pt-0.3')
        nomeArquivo = Utilitarios().criaNome()
        saida = nomeArquivo + '.wav'
        
        mp.AudioFileClip(self.caminho_do_video).write_audiofile(self.caminho_salvar + saida) #cria o arquivo de audio        
        audio = AudioSegment.from_wav(self.caminho_salvar + saida)
        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)
        audio.export(saida,format='wav')

        wf = wave.open(saida,'rb')
        rec = KaldiRecognizer(model,wf.getframerate())
        rec.SetWords(True)
    
        results = []
        momentos = []
        

        while True:
            data = wf.readframes(1600)

            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()        
                results.append(result)
                dados = json.loads(result)
                
                if dados['text'] != "":
                    for i in range(len(dados["result"])):
                        print(result)
                        
                    
                        if(dados["result"][i]["word"] == self.palavra_chave): #Está comparando a palavra do dados com a palavra chave
                            momentos.append([dados["result"][i]["start"],dados["result"][i]["word"],dados['text']])

                
                
        return momentos
    
    def identificaTodasPalavas(self):

        SetLogLevel(-1)

        model = Model('vosk-model-small-pt-0.3')
        nomeArquivo = Utilitarios().criaNome()
        saida = nomeArquivo + '.wav'
        
        mp.AudioFileClip(self.caminho_do_video).write_audiofile(self.caminho_salvar + saida) #cria o arquivo de audio        
        audio = AudioSegment.from_wav(self.caminho_salvar + saida)
        audio = audio.set_channels(1)
        audio = audio.set_frame_rate(16000)
        audio.export(saida,format='wav')

        wf = wave.open(saida,'rb')
        rec = KaldiRecognizer(model,wf.getframerate())
        rec.SetWords(True)
    
        results = []
        lista_de_palavras_deste_vídeo = []

        while True:
            data = wf.readframes(1600)

            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()        
                results.append(result)
                dados = json.loads(result)
                
                if dados['text'] != "":
                    for i in range(len(dados["result"])):
                        lista_de_palavras_deste_vídeo.append(dados["result"][i]["word"]) #capita todas as palavras do vídeo para uma lista
                        self.lista_de_palavras_deste_video = lista_de_palavras_deste_vídeo