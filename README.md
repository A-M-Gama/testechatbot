# Furion - ChatBot da FURIA no Telegram

Este é um chatbot do Telegram chamado Furion, desenvolvido para fãs da FURIA (organização brasileira de esports), com foco principal em Counter-Strike (CS). Ele utiliza a API do Gemini da Google para gerar respostas contextuais e informativas, e também emprega a funcionalidade de busca do Google (via Gemini Tools) para fornecer informações atualizadas, com preferência pela Wikipédia como fonte.

## Funcionalidades

* **Apresentação:** Ao iniciar o bot com o comando `/start`, Furion se apresenta como um chatbot da FURIA dedicado aos fãs de CS.
* **Ajuda:** O comando `/help` exibe uma mensagem de ajuda básica.
* **Respostas Inteligentes:** Furion responde a mensagens de texto dos usuários sobre a FURIA, buscando informações relevantes utilizando a busca do Google (com foco na Wikipédia).
* **Personalidade Amigável:** As respostas são geradas de forma amigável, com a inclusão ocasional de emojis.
* **Indicação de Fonte:** Ao final de cada resposta, Furion tenta indicar uma das fontes utilizadas (prioritariamente a Wikipédia).

## Pré-requisitos

* **Python 3.6 ou superior**
* **Bibliotecas Python:**
    * `python-telegram-bot`
    * `python-dotenv`
    * `google-generativeai`
* **Chaves de API:**
    * **Google Gemini API Key:** Necessária para acessar os modelos Gemini e a funcionalidade de busca.
    * **Telegram Bot Token:** Fornecido pelo BotFather no Telegram para controlar seu bot.

## Configuração

1.  **Clone o repositório (se aplicável) ou crie um novo diretório para o projeto.**
2.  **Instale as bibliotecas necessárias:**
    ```bash
    pip install python-telegram-bot python-dotenv google-generativeai
    ```
3.  **Crie um arquivo `.env`** no mesmo diretório do seu script Python.
4.  **Adicione suas chaves de API ao arquivo `.env`:**
    ```dotenv
    GOOGLE_GEMINI_API_KEY="SUA_CHAVE_GEMINI"
    TELEGRAM_BOT_KEY="SEU_TOKEN_DO_BOT_TELEGRAM"
    ```
    **Importante:** Substitua `"SUA_CHAVE_GEMINI"` pela sua chave de API do Google Gemini e `"SEU_TOKEN_DO_BOT_TELEGRAM"` pelo token do seu bot do Telegram.
5.  **Salve o arquivo `.env`.**

## Como Executar o Bot

1.  **Abra o terminal ou prompt de comando.**
2.  **Navegue até o diretório do seu projeto.**
3.  **Execute o script Python:**
    ```bash
    python seu_script.py
    ```
    (Substitua `seu_script.py` pelo nome do seu arquivo Python).

4.  **Abra o Telegram e procure pelo seu bot.**
5.  **Inicie uma conversa com o bot e experimente os comandos `/start` e `/help`, ou simplesmente envie mensagens de texto sobre a FURIA.**

## Estrutura do Código

* **`logging`:** Utilizado para registrar informações e erros durante a execução do bot.
* **`os`:** Usado para acessar variáveis de ambiente.
* **`dotenv`:** Carrega variáveis de ambiente do arquivo `.env`.
* **`telegram` e `telegram.ext`:** Bibliotecas para interagir com a API do Telegram.
* **`google.generativeai`:** Biblioteca para acessar os modelos Gemini da Google.

## Funções Principais

* **`start(update: Update, context: ContextTypes.DEFAULT_TYPE)`:** Apresenta o bot ao usuário quando o comando `/start` é enviado.
* **`help_command(update: Update, context: ContextTypes.DEFAULT_TYPE)`:** Exibe uma mensagem de ajuda básica.
* **`generate_answer(update: Update, context: ContextTypes.DEFAULT_TYPE)`:** Recebe a mensagem do usuário, utiliza o modelo Gemini com a ferramenta de busca do Google (com foco na Wikipédia) para gerar uma resposta amigável sobre a FURIA, e tenta indicar a fonte utilizada.
* **`main()`:** Função principal que configura e inicia o bot do Telegram, definindo os handlers para comandos e mensagens.

## Notas

* Certifique-se de ter configurado corretamente as variáveis de ambiente no arquivo `.env`.
* A qualidade das respostas pode variar dependendo da informação disponível.
