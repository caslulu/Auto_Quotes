from customtkinter import *
from Canva_Banner.preco_automatico import PrecoAutomatico


class Preco:
    def tela(self, fin_ou_qui, opcao, delete):
        self.fin_ou_qui = fin_ou_qui
        self.opcao = opcao
        self.delete = delete
        window = CTk()
        window.geometry("660x400")
        set_appearance_mode("dark")
        window.config(padx=30, pady=30)

        main_frame = CTkFrame(window, border_color="white", border_width=2, corner_radius=20)
        main_frame.pack(fill=BOTH, expand=True)
        self.associado_entry = CTkEntry(main_frame, placeholder_text="Associado")

        if self.fin_ou_qui == "Quitado":
            basico_frame = CTkFrame(main_frame)
            basico_frame.pack(side = LEFT, padx=30)

            self.entrada_basico_entry = CTkEntry(basico_frame, placeholder_text="Preço Básico")
            self.mensalidade_basico_entry = CTkEntry(basico_frame, placeholder_text="Mensalidade Básico")
            self.a_vista_basico_entry = CTkEntry(basico_frame, placeholder_text="À vista Básico")


            self.entrada_basico_entry.pack(pady=10)
            self.mensalidade_basico_entry.pack(pady=10)
            self.a_vista_basico_entry.pack(pady=10)  


            full_frame = CTkFrame(main_frame)
            full_frame.pack(side = RIGHT,  padx=30)

            self.entrada_full_entry = CTkEntry(full_frame, placeholder_text="Preço Full")
            self.mensalidade_full_entry = CTkEntry(full_frame, placeholder_text="Mensalidade Full")
            self.a_vista_full_entry = CTkEntry(full_frame, placeholder_text="À vista Full")

            self.entrada_full_entry.pack(pady=10)
            self.mensalidade_full_entry.pack(pady=10)
            self.a_vista_full_entry.pack(pady=10)

            enviar_botao = CTkButton(main_frame, text="Enviar", command=self.cotar)

            enviar_botao.pack(side = BOTTOM, pady=10)
            self.associado_entry.pack(side = BOTTOM, pady=10)




        else:   
            self.entrada_entry = CTkEntry(main_frame, placeholder_text="Entrada")
            self.mensalidade_entry = CTkEntry(main_frame, placeholder_text="Mensalidade")
            self.a_vista_entry = CTkEntry(main_frame, placeholder_text="À vista")


            self.entrada_entry.pack(pady=10)
            self.mensalidade_entry.pack(pady=10)
            self.a_vista_entry.pack(pady=10)  



            enviar_botao = CTkButton(main_frame, text="Enviar", command=self.cotar)

            enviar_botao.pack(side = BOTTOM, pady=10)
            self.associado_entry.pack(side = BOTTOM, pady=10)


        window.mainloop()



    def cotar(self):
        if self.opcao == "progressive":
            seguradora = "Progressive"
        elif self.opcao == "geico":
            seguradora = "Geico"
        p = PrecoAutomatico()
        associado = self.associado_entry.get()

        if self.fin_ou_qui == "Financiado":
            entrada = self.entrada_entry.get()
            mensalidade = self.mensalidade_entry.get()
            a_vista = self.a_vista_entry.get()

            p.financiado(seguradora=seguradora, entrada=entrada, mensalidade=mensalidade, a_vista=a_vista, associado=associado)

        else:
            entrada_basico = self.entrada_basico_entry.get()
            mensalidade_basico = self.mensalidade_basico_entry.get()
            a_vista_basico = self.a_vista_basico_entry.get()

            entrada_full = self.entrada_full_entry.get()
            mensalidade_full = self.mensalidade_full_entry.get()
            a_vista_full = self.a_vista_full_entry.get()
            p.quitado(seguradora=seguradora, entrada_basico=entrada_basico, entrada_full=entrada_full, mensalidade_basico=mensalidade_basico, mensalidade_full=mensalidade_full,
                                    a_vista_basico=a_vista_basico, a_vista_full=a_vista_full, associado=associado)
            
        self.delete()
        
