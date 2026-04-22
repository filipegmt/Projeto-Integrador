# Documentação de Requisitos - Agente de Inteligência Artificial para Reservas

## 1. Documento de Visão

O objetivo deste projeto é desenvolver um assistente virtual inteligente capaz de auxiliar utilizadores na escolha de restaurantes e na simulação de reservas em Portugal. O sistema utiliza dados reais extraídos da plataforma TheFork, armazenados de forma local (SQLite), e interage com o utilizador através de uma interface de chat fluida. O produto final visa demonstrar a integração prática entre bases de dados relacionais e agentes de Inteligência Artificial através da orquestração na plataforma n8n.

---

## 2. User Stories

### Pesquisa e Descoberta

- **US01:** Como utilizador, quero pedir recomendações de restaurantes numa cidade específica para encontrar um local perto de mim.
- **US02:** Como utilizador, quero especificar um tipo de gastronomia para filtrar os resultados de acordo com os meus gostos.
- **US03:** Como utilizador, quero saber o preço médio e a avaliação de um restaurante antes de decidir, para garantir uma boa relação qualidade/preço.

### Transparência e Confiança

- **US04:** Como utilizador, quero perceber o motivo da sugestão de certos restaurantes (ex: "Sugiro este porque tem nota 9.5 em comida italiana"), para confiar nas recomendações.
- **US05:** Como utilizador, quero receber respostas claras caso o agente não encontre restaurantes que correspondam aos meus critérios, para poder reformular o meu pedido.

### Processo de Reserva

- **US06:** Como utilizador, quero pedir ao agente para iniciar uma simulação de reserva para um número específico de pessoas numa determinada data.
- **US07:** Como utilizador, quero confirmar todos os detalhes (Nome, Data, Hora, Pessoas e Restaurante) através de um resumo antes da conclusão da reserva, para evitar erros.
- **US08:** Como utilizador, quero receber uma confirmação clara de sucesso após a efetivação da reserva simulada.

### Autenticação e Histórico de Reservas

- **US09:** Como utilizador, quero autenticar-me na plataforma para que as minhas preferências e reservas fiquem guardadas de forma segura.
- **US10:** Como utilizador, quero consultar a lista das minhas reservas efetuadas para gerir os meus planos gastronómicos.

---

## 3. Casos de Uso (Use Cases)

### UC01 - Consulta, Recomendação e Justificação

1. O utilizador envia uma mensagem natural com um pedido de recomendação.
2. O Agente de IA interpreta a intenção e os parâmetros (cidade, tipo de comida).
3. O sistema executa uma consulta SQL à base de dados `app_reservas.db`.
4. O sistema processa os dados e devolve as melhores opções, acompanhadas de uma breve justificação sobre o motivo da escolha.

### UC02 - Simulação Segura de Reserva

1. O utilizador solicita uma reserva após a escolha de um restaurante.
2. O Agente de IA verifica a existência de todos os dados necessários (Nome, Data, Hora, Número de Pessoas).
3. Se faltarem dados, o agente solicita as informações em falta ao utilizador.
4. Com os dados completos, o agente apresenta um resumo para validação final.
5. Após a aprovação do utilizador, o sistema emite uma mensagem de confirmação de sucesso.

### UC03 - Tratamento de Limitações de Dados

1. O utilizador pede um restaurante numa cidade que não consta na base de dados (ex: Coimbra).
2. O sistema consulta o ficheiro local e verifica a ausência de resultados.
3. O agente informa o utilizador de forma educada sobre a limitação geográfica atual do sistema e sugere as cidades disponíveis para pesquisa.

---

## 4. Requisitos do Sistema

### Requisitos Funcionais (RF)

- **RF01:** O sistema tem de interpretar linguagem natural através de um modelo de linguagem (LLM).
- **RF02:** O sistema tem de ler e extrair dados de uma base de dados SQLite local de forma autónoma.
- **RF03:** O sistema tem de devolver informações estruturadas (Nome, Morada, Preço, Avaliação e Cozinhas) ao utilizador.
- **RF04:** O sistema tem de solicitar uma confirmação explícita do utilizador antes de processar qualquer intenção de reserva.
- **RF05:** O sistema tem de manter o contexto da conversa para permitir pedidos de reserva sequenciais sem repetição de informações.
- **RF06:** O sistema deve validar as credenciais do utilizador antes de permitir o acesso ao histórico de reservas.
- **RF07:** O sistema deve associar automaticamente cada nova reserva ao ID do utilizador autenticado.

### Requisitos Não Funcionais (RNF)

- **RNF01 (Desempenho):** O tempo de resposta do agente não deve exceder os 10 segundos por interação.
- **RNF02 (Tecnologia):** A orquestração do fluxo de trabalho e a lógica de decisão têm de ocorrer na plataforma n8n.
- **RNF03 (Persistência):** A base de dados tem de suportar a adição de novas cidades sem requerer alterações à lógica principal do agente no n8n.
- **RNF04 (Resiliência):** O sistema deve responder de forma controlada a entradas de texto fora do contexto (ex: perguntas não relacionadas com restaurantes) para não bloquear a execução do fluxo.
