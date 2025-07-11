from PIL import Image, ImageDraw, ImageFont
from app.util.data_funcoes import formatar_com_virgula, parse_float_val


SIZE_PRECO = 55
SIZE_SEGURADORA = 40
SIZE_ASSOCIADO = 45


class PrecoAutomatico:
    def __init__(self, taxa_padrao=320.00):
        self.taxa_padrao = taxa_padrao
        self.fonte_preco = ImageFont.truetype("app/assets/fonts/fonte.otf", size=SIZE_PRECO)
        self.fonte_seguradora = ImageFont.truetype("app/assets/fonts/fonte.otf", size=SIZE_SEGURADORA)
        self.fonte_associado = ImageFont.truetype("app/assets/fonts/fonte.otf", size=SIZE_ASSOCIADO)

    def get_image_path(self, tipo, idioma):
        if tipo == 'basico':
            if idioma == 'en':
                return "app/assets/images/basico_en.png"
            
            elif idioma == 'es':
                return "app/assets/images/basico_es.png"
            
            else:
                return "app/assets/images/basico.png"
            
        elif tipo == 'full':
            if idioma == 'en':
                return "app/assets/images/full_en.png"
            
            elif idioma == 'es':
                return "app/assets/images/full_es.png"
            
            else:
                return "app/assets/images/full.png"
        return None

    def financiado(self, seguradora, idioma='pt', **kwargs):
        img_path = self.get_image_path('full', idioma)
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        draw.text((800, 562), seguradora, font=self.fonte_seguradora, fill="white")
        draw.text((870, 1400), kwargs.get("entrada_completo", ""), font=self.fonte_preco, fill="black")
        draw.text((885, 1545), kwargs.get("mensal_completo", ""), font=self.fonte_associado, fill="black")
        draw.text((850, 1695), kwargs.get("valor_total_completo", ""), font=self.fonte_preco, fill="black")
        draw.text((490, 1908), kwargs.get("nome", ""), font=self.fonte_associado, fill="white")
        caminho = "app/assets/images/financiado_feito.png"
        img.save(caminho)
        return caminho

    def quitado(self, seguradora, idioma='pt', **kwargs):
        img_path = self.get_image_path('basico', idioma)
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        draw.text((370, 543), seguradora, font=self.fonte_seguradora, fill="white")
        draw.text((1030, 543), seguradora, font=self.fonte_seguradora, fill="white")
        draw.text((440, 1375), kwargs.get("entrada_basico", ""), font=self.fonte_preco, fill="black")
        draw.text((1090, 1375), kwargs.get("entrada_completo", ""), font=self.fonte_preco, fill="black")
        draw.text((480, 1525), kwargs.get("mensal_basico", ""), font=self.fonte_associado, fill="black")
        draw.text((1130, 1525), kwargs.get("mensal_completo", ""), font=self.fonte_associado, fill="black")
        draw.text((440, 1655), kwargs.get("valor_total_basico", ""), font=self.fonte_preco, fill="black")
        draw.text((1090, 1655), kwargs.get("valor_total_completo", ""), font=self.fonte_preco, fill="black")
        draw.text((490, 1890), kwargs.get("nome", ""), font=self.fonte_associado, fill="white")
        caminho = "app/assets/images/quitado_feito.png"
        img.save(caminho)
        return caminho

    def processar_preco_quitado(self, preco_form, taxa=None):
        taxa = parse_float_val(taxa) if taxa is not None else self.taxa_padrao
        entrada_basico = parse_float_val(preco_form.entrada_basico.data) + taxa
        mensal_basico = preco_form.mensal_basico.data
        valor_total_basico = parse_float_val(preco_form.valor_total_basico.data) + taxa
        entrada_completo = parse_float_val(preco_form.entrada_completo.data) + taxa
        mensal_completo = preco_form.mensal_completo.data
        valor_total_completo = parse_float_val(preco_form.valor_total_completo.data) + taxa
        nome = preco_form.nome.data
        return {
            "entrada_basico": formatar_com_virgula(entrada_basico),
            "mensal_basico": mensal_basico,
            "valor_total_basico": formatar_com_virgula(valor_total_basico),
            "entrada_completo": formatar_com_virgula(entrada_completo),
            "mensal_completo": mensal_completo,
            "valor_total_completo": formatar_com_virgula(valor_total_completo),
            "nome": nome
        }

    def processar_preco_financiado(self, preco_form, taxa=None):
        taxa = parse_float_val(taxa) if taxa is not None else self.taxa_padrao
        entrada_completo = parse_float_val(preco_form.entrada_completo.data) + taxa
        mensal_completo = preco_form.mensal_completo.data
        valor_total_completo = parse_float_val(preco_form.valor_total_completo.data) + taxa
        nome = preco_form.nome.data
        return {
            "entrada_completo": formatar_com_virgula(entrada_completo),
            "mensal_completo": mensal_completo,
            "valor_total_completo": formatar_com_virgula(valor_total_completo),
            "nome": nome
        }