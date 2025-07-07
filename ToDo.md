# ToDo - Ordem de Prioridade

## 2. Funcionalidades Essenciais e Experiência do Usuário
- Implementar validações mais robustas nos formulários (PrecoForm_quitado, PrecoForm_financiado, etc.).
- Adicionar feedback visual para ações do usuário (ex.: carregamento, sucesso ou erro).
- Adicionar placeholders e tooltips nos campos dos formulários para melhorar a experiência do usuário.
- Melhorar o design do formulário preco.html para torná-lo mais responsivo e intuitivo.
- Adicionar uma barra de progresso para indicar o status do preenchimento da cotação.

## 3. Banco de Dados e Performance
- Adicionar migrações de banco de dados usando Flask-Migrate para facilitar alterações no esquema.
- Implementar validações e restrições no modelo Cotacao para evitar dados inconsistentes.
- Criar índices no banco de dados para melhorar a performance de consultas.
- Gerar e aplicar migration Alembic para garantir que o banco ML esteja sempre sincronizado com o modelo Python.
- Revisar e otimizar queries para evitar N+1 e melhorar performance em listas grandes.
- Adicionar campos de auditoria (criado_em, atualizado_em, usuário) nas tabelas principais.

## 4. Integrações e Automação
- Adicionar integração com WhatsApp ou Telegram para atendimento automatizado (menu de opções para clientes).
- Permitir envio de notificações automáticas para clientes (ex: status da cotação, documentos pendentes).
- Melhorar a integração com o Trello, exibindo status, comentários e anexos no sistema.
- Adicionar suporte para envio de e-mails automáticos com os resultados das cotações.
- Integrar com APIs de terceiros para validação de dados (ex.: validação de VIN ou CEP).
- Implementar cache para evitar chamadas repetidas a APIs externas (ex.: decodificação de VIN).
- Adicionar logs detalhados para monitorar o comportamento do sistema em produção.
- Automatizar exportação de dados para CSV periodicamente.
- Exibir anexos e comentários do Trello diretamente no sistema.

## 5. Testes e Qualidade
- Escrever testes unitários para todas as funções e métodos principais.
- Implementar testes de integração para verificar o fluxo completo de cotações.
- Adicionar testes para garantir que as imagens geradas (PrecoAutomatico) estão corretas.
- Configurar um pipeline de CI/CD para rodar os testes automaticamente.
- Criar testes automatizados para o fluxo de ML e integração.
- Adicionar testes para uploads de arquivos e validação de anexos.
- Testar o fluxo de múltiplos veículos/pessoas na edição e criação de cotações.
- Adicionar testes para rotas protegidas e autenticação.

## 6. Organização e Estrutura do Código
- Refatorar o código para garantir modularidade e reutilização.
- Revisar e organizar os arquivos em pastas apropriadas (ex.: services, routes, forms, models, etc.).
- Adicionar docstrings em todas as funções e classes para melhorar a documentação do código.
- Garantir que todos os métodos utilizem **kwargs onde aplicável para maior flexibilidade.
- Mover arquivos estáticos (fonts, imagens, templates PDF) para uma pasta assets ou static.

## 10. Automação de preenchimento de campos via imagem (OCR)
- Adicionar botão "Preencher automático" nos campos do condutor principal (e outros relevantes).
- Ao clicar, permitir que o usuário envie uma foto/documento (ex: Driver License).
- Utilizar OCR (ex: Tesseract, Google Vision API) para extrair dados da imagem e preencher automaticamente campos como nome, data de nascimento, número da CNH/DL, etc.
- Exibir preview dos dados extraídos para o usuário revisar/editar antes de salvar.
- Permitir anexar a imagem ao formulário junto com os dados extraídos.
- Garantir fallback manual caso o OCR não consiga extrair algum campo.

## 7. Documentação
- Criar um README detalhado com instruções de instalação, configuração e uso do projeto.
- Adicionar exemplos de uso para cada funcionalidade principal.
- Documentar as dependências no requirements.txt e garantir que ele esteja atualizado.
- Documentar e padronizar variáveis de ambiente (ex: .env para segredos e configs sensíveis).
- Adicionar um guia rápido para desenvolvedores contribuírem com o projeto.
- Documentar o fluxo de atendimento automatizado (chatbot/menu de opções).

## 8. Funcionalidades Futuras e Expansão
- Implementar uma API REST para permitir integração com outros sistemas.
- Criar um painel administrativo para gerenciar cotações, usuários e configurações.
- Dashboard de cotações e preços em tempo real.
- Notificações por e-mail ou no sistema para eventos importantes (nova cotação, cotação precificada, erro de integração).
- Upload e visualização de documentos adicionais (ex: CNH, comprovante de residência) vinculados à cotação.
- Relatórios em PDF/Excel das cotações e preços.
- Controle de acesso por perfil (admin, operador, gestor).
- Visualização dos anexos e comentários do Trello diretamente no sistema.
- Exportação de dados para análise externa.
- Histórico detalhado e auditoria de alterações em cotações e preços.
- Adicionar suporte a múltiplas empresas/filiais no sistema.
- Permitir customização de templates de e-mail e PDF por usuário ou empresa.

## 9. Tarefas Concluídas
- Permitir duplicar uma cotação existente para facilitar novos orçamentos.
- Suporte a múltiplas pessoas e veículos no formulário de cotação e edição.
- Separação de pessoas e veículos no banco de dados principal (Cotacao).
- Criação do modelo CotacaoPrecoML para ML.
- Scripts de ML: preprocessamento, treino, exportação, endpoint de predição.
- Integração do pipeline de ML com o app (previsão de preço).
- Checkbox "Somente prever preço (ML)" nos formulários de preço.
- Validação visual de seguradora obrigatória no preco.html (alerta no topo).
- Correção do fluxo de múltiplos veículos na automação Progressive.
- Correção de bugs e restauração de arquivos apagados do pipeline ML.
- Orientação sobre migrations para corrigir erros de schema no banco ML.
- Refino de legibilidade e remoção de redundâncias em vários arquivos de rotas e serviços.
- Integração do pré-processamento de features entre treino e predição ML.
- Edição de cotações com campos dinâmicos funcionando corretamente.
- Tema escuro/claro persistente via localStorage.
- Implementar um tema escuro/claro persistente usando cookies ou local storage.
- Permitir adicionar/remover veículos e pessoas na edição da cotação.
- Permitir upload de documentos e imagens diretamente na cotação (ex: CNH, comprovante de residência).
- Implementar confirmação antes de excluir veículos, pessoas ou cotações.
- Adicionar suporte a múltiplos idiomas (ex.: português e inglês) para mensagens e labels.