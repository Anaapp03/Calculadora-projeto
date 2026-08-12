import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        n1 = float(entry_num1.get())
        n2 = float(entry_num2.get())
        op = var_operacao.get()
        
        if op == "+":
            res = n1 + n2
        elif op == "-":
            res = n1 - n2
        elif op == "*":
            res = n1 * n2
        elif op == "/":
            if n2 == 0:
                messagebox.showerror("Erro", "Não é possível dividir por 0!")
                return
            res = n1 / n2
            
        label_resultado.config(text=f"Resultado: {res}")
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos!")

janela = tk.Tk()
janela.title("Calculadora Python")
janela.geometry("300x300")

tk.Label(janela, text="Primeiro Número:").pack(pady=5)
entry_num1 = tk.Entry(janela)
entry_num1.pack()

tk.Label(janela, text="Segundo Número:").pack(pady=5)
entry_num2 = tk.Entry(janela)
entry_num2.pack()

var_operacao = tk.StringVar(value="+")
frame_ops = tk.Frame(janela)
frame_ops.pack(pady=10)

for op in ["+", "-", "*", "/"]:
    tk.Radiobutton(frame_ops, text=op, variable=var_operacao, value=op).pack(side=tk.LEFT, padx=5)

tk.Button(janela, text="Calcular", command=calcular, bg="green", fg="white").pack(pady=10)

label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.pack(pady=5)

janela.mainloop()
