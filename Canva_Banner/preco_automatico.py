from PIL import Image, ImageDraw, ImageFont


SIZE_PRECO = 55
SIZE_SEGURADORA = 40
SIZE_ASSOCIADO = 45



class PrecoAutomatico:
    def __init__(self):
        self.basico_img = Image.open("Canva_Banner/Imagens/basico.png")
        self.completo = Image.open("Canva_Banner/Imagens/full.png")
        self.fonte_preco = ImageFont.truetype("Canva_Banner/Fonte/fonte.otf", size=SIZE_PRECO)
        self.fonte_seguradora = ImageFont.truetype("Canva_Banner/Fonte/fonte.otf", size=SIZE_SEGURADORA)
        self.fonte_associado = ImageFont.truetype("Canva_Banner/Fonte/fonte.otf", size=SIZE_ASSOCIADO)

    def financiado(self, entrada, mensalidade, a_vista, associado, seguradora):
        
        draw = ImageDraw.Draw(self.completo)
        seguradora = draw.text((800, 562), seguradora, font=self.fonte_seguradora, fill="white")
        entrada = draw.text((870, 1400), entrada, font=self.fonte_preco, fill="black")
        mensalidade = draw.text((885, 1545), mensalidade, font=self.fonte_associado, fill="black")
        a_vista = draw.text((850, 1695), a_vista, font=self.fonte_preco, fill="black")
        associado = draw.text((490, 1908), associado, font=self.fonte_associado, fill="white")
        self.completo.save("Canva_Banner/Imagens/financiado_feito.png")

    
    def quitado(self, entrada_basico, entrada_full, mensalidade_basico, mensalidade_full, a_vista_basico, a_vista_full, associado, seguradora):
        draw = ImageDraw.Draw(self.basico_img)
        seguradora_basico = draw.text((370, 543), seguradora, font=self.fonte_seguradora, fill="white")
        seguradora_full = draw.text((1030, 543), seguradora, font=self.fonte_seguradora, fill="white")

        entrada_basico = draw.text((440, 1375), entrada_basico, font=self.fonte_preco, fill="black")
        entrada_full = draw.text((1090, 1375), entrada_full, font=self.fonte_preco, fill="black")
   
        mensalidade_basico = draw.text((480, 1525), mensalidade_basico, font=self.fonte_associado, fill="black")
        mensalidade_full = draw.text((1130, 1525), mensalidade_full, font=self.fonte_associado, fill="black")
        
        a_vista_basico = draw.text((440, 1655), a_vista_basico, font=self.fonte_preco, fill="black")
        a_vista_full = draw.text((1090, 1655), a_vista_full, font=self.fonte_preco, fill="black")
        

        associado = draw.text((490, 1890), associado, font=self.fonte_associado, fill="white")

        self.basico_img.save("Canva_Banner/Imagens/quitado_feito.png")
