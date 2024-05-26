from model.entity.utilitarios import Utilitarios
import moviepy.editor as mp
import os

class Video_nugget():
    def __init__(self,segundo,palavra,texto) -> None:
        self.palavra = palavra
        self.segundo = segundo
        self.texto = texto
        self.caminho_salvar = os.path.abspath("view/static")
        self.nome = None

    def cria_Video_nugget(self,caminho_video):

        video = mp.VideoFileClip(caminho_video)
        inicio_corte = self.segundo - 60
        final_corte = self.segundo + 60

        if inicio_corte < 0:
            inicio_corte = 0

        if final_corte > video.duration:
            final_corte = video.duration

        self.nome = Utilitarios().criaNome() + '.mp4'
    
        trimed_video = video.subclip(inicio_corte,final_corte)
        self.caminho = self.caminho_salvar + self.nome
        trimed_video.write_videofile( self.caminho , codec = 'libx264')