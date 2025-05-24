# Auto Quotes

Bem-vindo ao Auto Quotes! Este é um sistema web para automação de cotações de seguros de veículos, com integração a múltiplas seguradoras e ao Trello para organização do fluxo de trabalho.

## O que o projeto faz?
- Permite cadastrar cotações de seguro de veículos de forma simples e rápida.
- Integra com as seguradoras Progressive, Geico e Allstate para automação de cotações.
- Gera banners automáticos de preço.
- Salva e gerencia cotações em banco de dados.
- Permite anexar imagens e informações diretamente em cartões do Trello.
- Interface web moderna, responsiva e com tema claro/escuro.

## Como rodar o projeto

1. **Clone o repositório:**
   ```powershell
   git clone <url-do-repositorio>
   cd Auto_Quotes
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
     ```env
     FLASK_APP=main.py
     FLASK_ENV=development
     SECRET_KEY=sua_chave_secreta
     URL_TRELLO=https://api.trello.com/1/cards
     TRELLO_KEY=seu_trello_key
     TRELLO_TOKEN=seu_trello_token
     TRELLO_ID_LIST=seu_id_da_lista
     ```

5. **Execute as migrações do banco de dados:**
   ```powershell
   flask db upgrade
   ```

6. **Rode o servidor Flask:**
   ```powershell
   flask run
   ```
   O app estará disponível em [http://localhost:5000](http://localhost:5000)

## Estrutura das principais pastas
- `app/` — Código principal da aplicação
  - `routes/` — Rotas Flask (cada arquivo representa um fluxo)
  - `services/` — Integrações externas e regras de negócio
  - `forms/` — Formulários WTForms
  - `models/` — Modelos do banco de dados
  - `util/` — Funções utilitárias
  - `templates/` — Templates HTML (Jinja2)
  - `static/` — CSS, JS e imagens
- `instance/` — Banco de dados SQLite
- `migrations/` — Controle de versões do banco

## Principais funcionalidades
- Cadastro, edição e exclusão de cotações
- Integração com Trello (criação de cartões e anexos)
- Geração automática de banners de preço
- Suporte a múltiplas seguradoras
- Interface amigável e responsiva

## Contribuindo
Pull requests são bem-vindos! Se quiser sugerir melhorias, abrir issues ou contribuir com código, fique à vontade.

## Roadmap e ideias futuras
Veja o arquivo `ToDo.md` para uma lista de melhorias e funcionalidades planejadas.

---

Se tiver dúvidas, sugestões ou encontrar bugs, abra uma issue ou entre em contato!
