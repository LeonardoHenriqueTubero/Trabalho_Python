import customtkinter as ctk

from backend.repository.Repositorio import Repositorio

#aparencia
ctk.set_appearance_mode("Dark")

#Criando a janela
app = ctk.CTk()
app.title("Livraiaria")
app.geometry("500x500")
#instancia
repositorio = Repositorio.iniciar_repositorio()

#criando campos
label = ctk.CTkLabel(app, text='Bem vindo a Livraria')
label.pack(pady=20)

ctk.CTkButton(app, text='Carregue todos os dados antes de qualquer atividade', command=repositorio.carregar_tudo).pack(pady=10)
ctk.CTkButton(app, text='Consultar alunos', command=repositorio.dados_alunos.leitura_exaustiva).pack(pady=5)
ctk.CTkButton(app, text='Consultar autores', command=repositorio.dados_autores.leitura_exaustiva).pack(pady=5)
ctk.CTkButton(app, text='Incluir livros',).pack(pady=5)
ctk.CTkButton(app, text='Consultar livros', ).pack(pady=5)
ctk.CTkButton(app, text='Realizar empréstimo', ).pack(pady=5)
ctk.CTkButton(app, text='Consultar empréstimo', ).pack(pady=5)
ctk.CTkButton(app, text='Realizar devolução', ).pack(pady=5)
ctk.CTkButton(app, text='Consultar livros emprestados', ).pack(pady=5)
ctk.CTkButton(app, text='Empréstimo com devolução atrasada', ).pack(pady=5)
ctk.CTkButton(app, text='Qtde de livros emprestados por período', ).pack(pady=5)

#funcoes

#iniciando aplicaçao
app.mainloop()