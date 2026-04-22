# Agente de IA para Reservas em Restauração

Este repositório contém o código e a documentação do projeto de um Agente de Inteligência Artificial desenhado para interagir com utilizadores em linguagem natural, oferecer recomendações de restaurantes em Portugal e gerir o processo de reserva de mesas.

---

## Objetivo do Projeto

Demonstrar a integração prática entre fluxos de orquestração de IA e bases de dados relacionais. O sistema processa pedidos complexos, consulta informações estruturadas de forma autónoma, devolve respostas humanizadas e gere o histórico de cada utilizador.

---

## Funcionalidades Principais

- **Pesquisa Inteligente:** Recomendação de restaurantes com filtros por localização (ex: Porto, Lisboa, Faro, Setúbal) e tipo de gastronomia.
- **Decisão Transparente:** O agente justifica as suas escolhas com base no preço e nas avaliações reais dos espaços.
- **Sistema de Autenticação:** Proteção de dados e personalização da experiência (Login).
- **Gestão de Reservas:** Simulação de novas marcações e consulta de histórico (reservas passadas e futuras) para utilizadores com sessão iniciada.
- **Tratamento de Exceções:** Respostas educadas e encaminhamento adequado perante a ausência de dados ou pedidos fora do contexto.

---

## Tecnologias e Ferramentas

A arquitetura do projeto divide-se em quatro pilares fundamentais:

1. **Extração de Dados (Web Scraping):** `Python` com recurso à biblioteca `BeautifulSoup4`.
2. **Armazenamento (Backend):** Base de dados relacional e local `SQLite` (`app_reservas.db`).
3. **Orquestração e IA:** `n8n` (Criação de _workflows_ e integração com o Modelo de Linguagem).
4. **Interface (Frontend):** `React` (Em fase de planeamento/desenvolvimento).

---

## Estrutura do Repositório

### Documentação Técnica (`/docs`)

- `REQUISITOS.md`: Histórias de Utilizador e requisitos do sistema.
- `DIAGRAMAS.md`: Arquitetura do sistema (Casos de Uso, Sequência e Modelo Lógico de Dados - ERD).
- `INTERFACE.md`: Mockups e design de interface (Figma).

### Scripts e Base de Dados

- `importar_dados.py`: Script original para extração e transformação dos dados do TheFork.
- `atualizar_db.py`: Script de migração para criação das tabelas de utilizadores e reservas.
- `app_reservas.db`: Base de dados pronta a utilizar pelo agente (Tabelas: `restaurantes`, `utilizadores`, `reservas`).

---

## Como Executar o Projeto

### Pré-requisitos

- Python instalado (versão 3.10 ou superior).
- Plataforma n8n instalada e configurada localmente.

### Passos de Instalação Local

1. Clona este repositório para a tua máquina:
   ```bash
   git clone https://github.com/filipegmt/Projeto-Integrador.git
   ```
