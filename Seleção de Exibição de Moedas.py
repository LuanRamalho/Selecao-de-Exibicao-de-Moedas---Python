import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Links das imagens das moeda
links_moedas = {
    "1 Centavo": "https://images.tcdn.com.br/img/img_prod/1083822/1_centavo_1a_familia_1994_1997_337_1_0546992d03ccd73361c6ba5019fa3227.png",
    "5 Centavos": "https://images.tcdn.com.br/img/img_prod/1083822/5_centavos_2a_familia_fc_341_1_87fa023f132b787bc0efac76133757d8.png",
    "10 Centavos": "https://images.tcdn.com.br/img/img_prod/1083822/10_centavos_2a_familia_fc_343_1_433af046b48d50431a9a570beb1f567a.png",
    "25 Centavos": "https://images.tcdn.com.br/img/img_prod/1083822/25_centavos_2a_familia_fc_1669_1_0ed1170cc91ade41c29640ea60949051.png",
    "50 Centavos": "https://images.tcdn.com.br/img/img_prod/1083822/50_centavos_2a_familia_fc_1671_1_852b1f9b48db2fa5643e4463aac9ba8d.png",
    "1 Real": "https://numismaticacoan.com/wp-content/uploads/2017/07/2014-4.jpg"
}

# Função para carregar e exibir a imagem da moeda selecionada
def exibir_imagem(moeda):
    if moeda in links_moedas:
        url = links_moedas[moeda]
        try:
            response = requests.get(url, timeout=5)  # Define um tempo limite para a requisição
            response.raise_for_status()  # Verifica se houve algum erro na requisição
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image = image.resize((300, 250), Image.LANCZOS)  # Redimensiona a imagem
            photo = ImageTk.PhotoImage(image)
            imagem_label.config(image=photo)
            imagem_label.image = photo
            info_label.config(text=f"Você selecionou a moeda de {moeda}")
        except requests.RequestException:
            info_label.config(text="Erro ao carregar a imagem. Verifique o link.")
        except Exception as e:
            info_label.config(text=f"Erro inesperado: {e}")

# Configurações da janela principal
root = tk.Tk()
root.title("Seleção de Moedas de Dinheiro")
root.geometry("500x500")
root.configure(bg="#DFF0E8")

# Label de Instrução
instrucoes_label = tk.Label(root, text="Escolha uma moeda de dinheiro:", font=("Helvetica", 14), bg="#DFF0E8")
instrucoes_label.pack(pady=10)

# Menu de Seleção de Moedas
opcao_moeda = ttk.Combobox(root, values=list(links_moedas.keys()), font=("Helvetica", 12))
opcao_moeda.pack(pady=10)
opcao_moeda.set("Selecione uma Moeda")

# Botão para exibir a moeda selecionada
botao_exibir = tk.Button(root, text="Exibir Moeda", command=lambda: exibir_imagem(opcao_moeda.get()), bg="#68C3A3", fg="white", font=("Helvetica", 12))
botao_exibir.pack(pady=10)

# Label para exibir a imagem da moeda selecionada
imagem_label = tk.Label(root, bg="#DFF0E8")
imagem_label.pack(pady=10)

# Label para exibir informações sobre a moeda selecionada
info_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#DFF0E8")
info_label.pack(pady=5)

root.mainloop()
