import customtkinter
from tkinter import *
import socket
import psutil
import telnetlib

def teste_telenet():
    end_ip = E_ip.get()
    Lips.delete(0, END)  # Limpar a lista antes de adicionar novos itens

    tentativas = 4
    for _ in range(tentativas):
        try:
            # Tenta estabelecer uma conexão usando telnet
            with telnetlib.Telnet(end_ip, 23, timeout=5) as tn:
                Lips.insert(END, f"Conexão Telenet bem-sucedida com {end_ip}")
                break  # Sai do loop se a conexão for bem-sucedida
        except Exception as e:
            Lips.insert(END, f"Falha na tentativa de conexão Telenet com {end_ip}: {str(e)}")

    else:
        # Este bloco é executado se todas as tentativas falharem
        Lips.insert(END, f"Não foi possível conectar com o endereço IP {end_ip}")



def teste_conexao():
    end_ip = E_ip.get()
    Lips.delete(0, END)  # Limpar a lista antes de adicionar novos itens

    try:
        # Tenta estabelecer uma conexão com o endereço IP
        socket.create_connection((end_ip, 80), timeout=5)
        Lips.insert(END, f"Conexão bem-sucedida com {end_ip}")
    except Exception as e:
        Lips.insert(END, f"Falha na conexão com {end_ip}: {str(e)}")

def listar_conexoes_ativas():
    Lips.delete(0, END)  # Limpar a lista antes de adicionar novos itens

    # Obtém a lista de conexões ativas usando psutil
    connections = psutil.net_connections(kind='inet')

    for conn in connections:
        Lips.insert(END, f"PID: {conn.pid}, Laddr: {conn.laddr}, Raddr: {conn.raddr}, Status: {conn.status}")

def reiniciar_conexoes():
    Lips.delete(0, END)  # Limpar a lista antes de adicionar novos itens

    # Obtém a lista de conexões ativas usando psutil
    connections = psutil.net_connections(kind='inet')

    for conn in connections:
        try:
            # Tenta encerrar o processo associado à conexão
            psutil.Process(conn.pid).terminate()
            Lips.insert(END, f"Conexão encerrada: PID {conn.pid}, Laddr: {conn.laddr}, Raddr: {conn.raddr}")
        except Exception as e:
            Lips.insert(END, f"Falha ao encerrar PID {conn.pid}: {str(e)}")


# defenir cores ----------------------------------------------------------------
co0 ='#0000FF' 
co1 = '#FFFFFF'

#-------------------------------------------------------------------------------

Janela = customtkinter.CTk()
Janela.geometry('780x600+100+100')
Janela.resizable(False, False)
Janela.title('Teste Ligação Dev Joel(com socket)')
Janela.config(bg=co0)
Janela.iconbitmap(r'C:\Users\HP\Desktop\Teste Ligação a Internet\Update ao Teste Ligação\icon2.ico')

E_ip = Entry(Janela, width=70, font=('arial 14'))
E_ip.place(x=135, y=20)

LIP = Label(Janela, text='Endereço IP:', font=('Arial 14'), bg=co0, fg=co1)
LIP.place(x=10, y=20)

Bteste = customtkinter.CTkButton(Janela, text='Teste Ligação', command=teste_conexao, bg_color=co0)
Bteste.place(x=90, y=60)

Blistar = customtkinter.CTkButton(Janela, text='Listar Conexões Ativas', command=listar_conexoes_ativas, bg_color=co0)
Blistar.place(x=240, y=60)

Breiniciar = customtkinter.CTkButton(Janela,  text='Reiniciar Conexões', command=reiniciar_conexoes, bg_color=co0)
Breiniciar.place(x=390, y=60)

BTesteTelenet = customtkinter.CTkButton(Janela,  text='Teste Telenet ',command=teste_telenet, bg_color=co0)
BTesteTelenet.place(x=540, y=60)

Lips = Listbox(Janela, width=100, height=29, font=('arial 13'))
Lips.place(x=20, y=150)

Janela.mainloop()
