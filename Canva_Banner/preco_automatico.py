from PIL import Image, ImageDraw, ImageFont


SIZE_PRECO = 55
SIZE_SEGURADORA = 40
SIZE_ASSOCIADO = 45



class PrecoAutomatico:
    def __init__(self):
        self.basico = Image.open("Imagens/basico.png")
        self.completo = Image.open("Imagens/full.png")
        self.fonte_preco = ImageFont.truetype("Fonte/fonte.otf", size=SIZE_PRECO)
        self.fonte_seguradora = ImageFont.truetype("Fonte/fonte.otf", size=SIZE_SEGURADORA)
        self.fonte_associado = ImageFont.truetype("Fonte/fonte.otf", size=SIZE_ASSOCIADO)

    def escrever_preco_basico(self, entrada, mensalidade, a_vista, associado, seguradora):
        
        draw = ImageDraw.Draw(self.completo)
        seguradora = draw.text((800, 562), seguradora, font=self.fonte_seguradora, fill="white")
        entrada = draw.text((870, 1400), entrada, font=self.fonte_preco, fill="black")
        mensalidade = draw.text((885, 1545), mensalidade, font=self.fonte_associado, fill="black")
        a_vista = draw.text((850, 1695), a_vista, font=self.fonte_preco, fill="black")
        associado = draw.text((490, 1908), associado, font=self.fonte_associado, fill="white")
        self.completo.save("Imagens/completo_feito.png")
