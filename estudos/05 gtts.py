# Criando audio a partir de arquivo txt e executando
from gtts import gTTS
from playsound import playsound
_path = "C:/Users/Armando/Documents/python/AssistentePessoal/estudos"
def cria_audio(mensagem):
	tts = gTTS(mensagem, lang = 'pt-br')
	tts.save(_path+'/hello.mp3')
	playsound(_path+'/hello.mp3')

arquivo = open(_path+"/frase.txt", "r", encoding = "utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)
arquivo.close()