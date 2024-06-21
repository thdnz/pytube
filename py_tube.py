# Importa a classe YouTube da biblioteca pytube
from pytube import YouTube

# Define uma função chamada Download que aceita um link como argumento
def Download(link):
    # Cria um objeto YouTube usando o link fornecido
    youtubeObject = YouTube(link)
    # Obtém a stream de maior resolução disponível para o vídeo
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        # Tenta baixar o vídeo
        youtubeObject.download()
        # Se o download for bem-sucedido, imprime esta mensagem
        print("Download concluído")
    except:
        # Se ocorrer algum erro durante o download, imprime esta mensagem
        print("Erro, download não concluído")

# Solicita ao usuário que insira o URL do vídeo do YouTube
link = input("Digite o URL do vídeo do YouTube: ")
# Chama a função Download com o link fornecido pelo usuário
Download(link)