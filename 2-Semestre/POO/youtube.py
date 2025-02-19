from pytube import YouTube

def baixar_video(link):
    try:
        # Inicializa o objeto YouTube
        yt = YouTube(link)
        
        # Exibe informações do vídeo
        print(f"Baixando: {yt.title}")
        print(f"Autor: {yt.author}")
        print(f"Duração: {yt.length // 60} minutos e {yt.length % 60} segundos")
        
        # Seleciona a melhor stream de vídeo
        stream = yt.streams.get_highest_resolution()
        
        # Faz o download do vídeo
        stream.download()
        print("Download concluído!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    link = input("Digite o link do vídeo do YouTube: ")
    baixar_video(link)
