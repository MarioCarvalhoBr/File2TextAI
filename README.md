# File2TextAI

File2TextAI é um projeto em Python que combina o poder da Inteligência Artificial para extrair texto de arquivos de diversos formatos, como PDFs, imagens, entre outros. O projeto oferece uma interface simples em linha de comando para processar um ou vários arquivos de uma só vez, com a opção de salvar as saídas em uma pasta definida pelo usuário.

## Sumário
- [File2TextAI](#file2textai)
  - [Sumário](#sumário)
  - [Pré-requisitos](#pré-requisitos)
  - [Configuração](#configuração)
    - [1. Criação e Ativação de Ambiente Virtual (Venv)](#1-criação-e-ativação-de-ambiente-virtual-venv)
    - [2. Instalação dos Requerimentos](#2-instalação-dos-requerimentos)
      - [Opção 1: Instalar via `requirements.txt`](#opção-1-instalar-via-requirementstxt)
      - [Opção 2: Instalar individualmente](#opção-2-instalar-individualmente)
  - [Como Usar](#como-usar)
    - [Executar em múltiplos arquivos](#executar-em-múltiplos-arquivos)
    - [Executar em um único arquivo](#executar-em-um-único-arquivo)
    - [Salvar em Pasta de Saída](#salvar-em-pasta-de-saída)
  - [Estrutura de Pastas](#estrutura-de-pastas)
  - [Contribuindo](#contribuindo)
  - [Requisitos](#requisitos)
  - [Licença](#licença)

---

## Pré-requisitos

- Python 3.x instalado (recomendado Python 3.12 ou superior).
- [pip](https://pip.pypa.io/en/stable/installing/) instalado.
- Acesso à internet para instalar e utilizar algumas bibliotecas, como a [OpenAI](https://pypi.org/project/openai/) e outras dependências.

---

## Configuração

### 1. Criação e Ativação de Ambiente Virtual (Venv)

É fortemente recomendado criar e ativar um ambiente virtual para evitar conflitos de dependências com outros projetos. No terminal ou prompt de comando, execute:

```bash
# Crie o ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual (Linux/macOS)
source venv/bin/activate

# Ative o ambiente virtual (Windows)
venv\Scripts\activate
```

### 2. Instalação dos Requerimentos

#### Opção 1: Instalar via `requirements.txt`
Se preferir instalar todos os pacotes de uma vez, utilize:
```bash
pip install -r requirements.txt
```

#### Opção 2: Instalar individualmente
Para instalar cada biblioteca de forma manual, execute no terminal (já com o ambiente virtual ativado):

```bash
pip install openai==1.59.6
pip install PyYAML==6.0.2

# Desinstala quaisquer versões pré-instaladas de torch, torchvision e torchaudio
pip3 uninstall torch torchvision torchaudio -y

# Instala as versões CPU de torch, torchvision e torchaudio
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Instala o docling (com extra index url para pacotes CPU)
pip install docling --extra-index-url https://download.pytorch.org/whl/cpu

# Instala o easyocr
pip install easyocr
```

---

## Como Usar

Depois de configurar e ativar seu ambiente, você pode executar o `main.py` para extrair texto de arquivos.

### Executar em múltiplos arquivos

Use `--input_folder` para processar **N arquivos** de uma só vez. É possível usar o glob `*` para buscar todos os arquivos dentro de pastas e subpastas:

```bash
python3 main.py --input_folder="pasta/arquivos/*"
```

### Executar em um único arquivo

Use `--input_file` para processar **apenas um arquivo**:

```bash
python3 main.py --input_file="arquivo.pdf"
```

### Salvar em Pasta de Saída

Opcionalmente, utilize `--output_folder` para indicar onde os arquivos de texto extraídos devem ser salvos:

```bash
python3 main.py --input_folder="pasta/arquivos/*" --output_folder="saida_texto/"
```

Caso não seja especificado um `--output_folder`, os arquivos de texto serão salvos em um local padrão definido no script `main.py`.

---

## Estrutura de Pastas

A estrutura típica do projeto é:

```
File2TextAI/
├── main.py
├── requirements.txt
├── README.md
└── venv/ (criado após executar o comando de criação do ambiente virtual)
```

---

## Contribuindo

Contribuições são bem-vindas! Para propor melhorias, correções ou novas funcionalidades:

1. Faça um fork deste repositório.
2. Crie uma nova branch: `git checkout -b minha-nova-feature`.
3. Faça commit das suas alterações: `git commit -m 'Adicionando nova feature'`.
4. Faça push para a branch: `git push origin minha-nova-feature`.
5. Abra um Pull Request descrevendo suas alterações.

---

## Requisitos

- Python 3.x
- openai==1.59.6
- PyYAML==6.0.2
- torch (versão compatível com CPU)
- torchvision (versão compatível com CPU)
- torchaudio (versão compatível com CPU)
- docling
- easyocr


## Licença

Este projeto é distribuído sob a licença [MIT](https://opensource.org/licenses/MIT). Sinta-se livre para usar, modificar e distribuir conforme definido na licença.