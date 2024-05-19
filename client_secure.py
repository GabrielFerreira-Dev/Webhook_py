import tkinter as tk
import requests
import json

# Função para enviar mensagem ao servidor
def send_message():
    server_url = "https://localhost:5000/webhook"  # Substitua pelo IP do servidor se necessário
    data = {
        "nome": "Cliente",
        "mensagem": message_entry.get()
    }
    response = requests.post(server_url, json=data, verify=False)
    response_text.set(f"Status Code: {response.status_code}\nResposta do Servidor: {response.json()}")

# Interface Gráfica
root = tk.Tk()
root.title("Cliente Webhook Seguro")

frame = tk.Frame(root)
frame.pack(pady=10)

message_label = tk.Label(frame, text="Mensagem:")
message_label.grid(row=0, column=0, padx=5, pady=5)

message_entry = tk.Entry(frame, width=40)
message_entry.grid(row=0, column=1, padx=5, pady=5)

send_button = tk.Button(root, text="Enviar Mensagem", command=send_message)
send_button.pack(pady=10)

response_text = tk.StringVar()
response_label = tk.Label(root, textvariable=response_text, justify=tk.LEFT)
response_label.pack(pady=10)

root.mainloop()
