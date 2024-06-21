import instaloader
import os

ig = instaloader.Instaloader()

# URL do post do vídeo
url = input("Entre com o URL do post do vídeo")

# Obtém o post do vídeo
post = instaloader.Post.from_shortcode(ig.context, url.split("/")[-2])

# Caminho para o diretório atual
current_directory = os.getcwd()

# Baixa o vídeo para o diretório atual
ig.download_post(post, target=current_directory)
