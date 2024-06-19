# Projeto PyTube

Este projeto é uma ferramenta simples para baixar vídeos do YouTube. Ele usa a biblioteca `pytube` para fazer o download dos vídeos.

## Como usar

1. Clone este repositório para a sua máquina local usando `git clone https://github.com/thdnz/pytube.git`.
2. Navegue até o diretório do projeto com `cd pytube`.
3. Execute o script `projeto_pytube.py` com `python projeto_pytube.py`.
4. Quando solicitado, insira o URL do vídeo do YouTube que você deseja baixar.
5. O script tentará baixar o vídeo na resolução mais alta disponível.
6. Se o download for bem-sucedido, você verá a mensagem "Download concluído". Se ocorrer um erro, você verá a mensagem "Erro, download não concluído".

## Dependências

Este projeto depende da biblioteca `pytube`. Você pode instalá-la com o seguinte comando:

```bash
pip install pytube
