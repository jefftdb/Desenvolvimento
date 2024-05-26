from model.entity.edicao import Edicao 
from model.entity.video_nugget import Video_nugget
from app import app
from flask import render_template,request,redirect


@app.route('/')
def index():
    return redirect('/cortar')

@app.route('/cortar', methods = ['GET' , 'POST'])
def cortar():
    if request.method == 'POST':
        
        link_YOUTUBE = request.form['link_youtube']
        palavra = request.form['palavra']
        
        video = Edicao(link_YOUTUBE,palavra)

        caminho_video = video.DownloadYouTube()
        tempos = video.identificaPalavraNoTempo()

        lista = []
        for t in tempos:
            cortes_de_video = Video_nugget(t[0],t[1],t[2]) # entra com o segundo, palavra e o texto encontrado
            cortes_de_video.cria_Video_nugget(caminho_video)
        
            lista.append(cortes_de_video)

        return render_template('lista_de_cortes.html',lista = lista)
    return render_template('index.html')

