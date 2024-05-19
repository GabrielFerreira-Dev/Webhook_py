import threading
import tkinter as tk
from flask import Flask, request, jsonify
import ssl

app = Flask(__name__)

# Variável global para armazenar a mensagem recebida
received_message = ""

@app.route('/webhook', methods=['POST'])
def webhook():
    global received_message
    data = request.json
    received_message = str(data)
    print(f"Dados recebidos: {data}")
    update_textarea(f"Dados recebidos: {data}")
    return jsonify({"message": "Dados recebidos com sucesso"}), 200

def run_server():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server_cert.pem", keyfile="server_key.pem")
    app.run(host="0.0.0.0", port=5000, ssl_context=context)

def start_server():
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

def update_textarea(message):
    text_area.insert(tk.END, message + "\n")
    text_area.see(tk.END)

# Interface Gráfica
root = tk.Tk()
root.title("Servidor Webhook Seguro")

frame = tk.Frame(root)
frame.pack(pady=10)

text_area = tk.Text(frame, height=20, width=50)
text_area.pack()

start_button = tk.Button(root, text="Iniciar Servidor", command=start_server)
start_button.pack(pady=10)

root.mainloop()
