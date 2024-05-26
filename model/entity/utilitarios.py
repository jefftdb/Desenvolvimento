from datetime import datetime

class Utilitarios():
    def __init__(self) -> None:
       pass
    
    #Converte o tempo para segundos
    def ConverteTempoEmSegundos(self,time):
        splitted_time = time.split(':')

        horas = int(splitted_time[0])
        minutos = int(splitted_time[1])
        segundos = int(splitted_time[2])

        total_de_segundos =(horas * 3600) + (minutos * 60) + segundos

        return total_de_segundos
    
    def criaNome(self):
        t = datetime.now()
        nome = "/ORIGEM-" + t.strftime('%y-%m-%d-%H%M%S%f')
        return nome