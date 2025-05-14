from app.util.data_funcoes import decodificar_vin, formatar_data, separar_nome, separar_documento, separar_endereco, veiculo_vin
def extrair_dados_formulario(cotacao_form):
    return {
        "genero": cotacao_form.genero.data,
        "nome": cotacao_form.nome.data,
        "documento": cotacao_form.documento.data,
        "endereco": cotacao_form.endereco.data,
        "financiado": cotacao_form.financiado.data,
        "tempo_de_seguro": cotacao_form.tempo_de_seguro.data,
        "vin": cotacao_form.vin.data,
        "data_nascimento": cotacao_form.data_nascimento.data,
        "tempo_com_veiculo": cotacao_form.tempo_com_veiculo.data,
        "tempo_no_endereco": cotacao_form.tempo_no_endereco.data,
    }

def processar_cotacao(primeiro):
    genero = primeiro.genero
    first_name, last_name = separar_nome(primeiro.nome)
    documento, estado_documento = separar_documento(primeiro.documento)
    rua, apt, cidade, zipcode = separar_endereco(primeiro.endereco)
    financiado = primeiro.financiado
    tempo_de_seguro = primeiro.tempo_de_seguro
    lista_vin = decodificar_vin(primeiro.vin)
    data_nascimento = formatar_data(primeiro.data_nascimento)
    tempo_com_veiculo = primeiro.tempo_com_veiculo
    tempo_no_endereco = primeiro.tempo_no_endereco
    return {
        "genero": genero,
        "first_name": first_name,
        "last_name": last_name,
        "estado_documento": estado_documento,
        "rua": rua,
        "apt": apt,
        "cidade": cidade,
        "zipcode": zipcode,
        "financiado": financiado,
        "tempo_de_seguro": tempo_de_seguro,
        "lista_vin": lista_vin,
        "data_nascimento": data_nascimento,
        "tempo_com_veiculo": tempo_com_veiculo,
        "tempo_no_endereco": tempo_no_endereco,
    }


def processar_preco_quitado(preco_form):
    entrada_basico = preco_form.entrada_basico.data
    mensal_basico = preco_form.mensal_basico.data
    valor_total_basico = preco_form.valor_total_basico.data
    entrada_completo = preco_form.entrada_completo.data
    mensal_completo = preco_form.mensal_completo.data
    valor_total_completo = preco_form.valor_total_completo.data
    nome = preco_form.nome.data
    seguradora = preco_form.seguradora.data
    return {
        "entrada_basico": entrada_basico,
        "mensal_basico": mensal_basico,
        "valor_total_basico": valor_total_basico,
        "entrada_completo": entrada_completo,
        "mensal_completo": mensal_completo,
        "valor_total_completo": valor_total_completo,
        "nome": nome,
        "seguradora": seguradora
    }

def processar_preco_financiado(preco_form):
    entrada_completo = preco_form.entrada_completo.data
    mensal_completo = preco_form.mensal_completo.data
    valor_total_completo = preco_form.valor_total_completo.data
    nome = preco_form.nome.data
    seguradora = preco_form.seguradora.data
    return {
        "entrada_completo": entrada_completo,
        "mensal_completo": mensal_completo,
        "valor_total_completo": valor_total_completo,
        "nome": nome,
        "seguradora": seguradora
    }