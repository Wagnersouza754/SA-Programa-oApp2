
# Devolutiva formativa — Atividade 01 da SA

**Estudante:** Wagner  
**Turma:** Rio Negrinho — Tarde  
**Unidade Curricular:** Programação de Aplicativos  
**Projeto:** Aplicativo de Transporte  
**Códigos analisados:** `codigo/app.py` e `codigo/codigo_prova.py`  
**Referência:** Situação de Aprendizagem nº 1 — *Da Ideia ao Código*

## O que você já conseguiu desenvolver

Wagner, seu projeto apresenta uma aplicação de transporte que relaciona motoristas, passageiros e corridas. Você desenvolveu diferentes regras para cadastro, escolha de veículos, cálculo de preços e acompanhamento das solicitações.

Pontos positivos identificados:

- Criou as classes `Motorista`, `Passageiro` e `Corrida`, separando os principais elementos do sistema.
- Implementou cadastros e verificações para motoristas e passageiros.
- Utilizou **atributos e métodos** para representar informações e comportamentos dos objetos.
- Criou regras de cálculo de preço considerando a categoria do transporte e a distância informada.
- Implementou a seleção de motoristas disponíveis.
- Incluiu opções de forma de pagamento e confirmação de corrida.
- Desenvolveu uma consulta ao histórico das corridas registradas.
- Utilizou **condicionais, repetições, listas, funções e tratamento de erros numéricos**.
- Incluiu comentários detalhados, facilitando o acompanhamento do fluxo.

## O que precisa ser corrigido

### 1. Definir qual arquivo representa a versão principal do projeto

O repositório contém `app.py` e `codigo_prova.py`, com implementações diferentes do aplicativo.

O arquivo `codigo_prova.py` possui recursos e modalidades adicionais em relação ao `app.py`.

**Como melhorar:** identificar claramente no README qual arquivo deve ser executado e qual representa a versão atual. Se ambos forem mantidos, explicar a finalidade de cada um para evitar dúvidas.

### 2. Melhorar o controle de disponibilidade dos motoristas

Ao confirmar uma corrida, o programa define `motorista_encontrado.disponivel = False`.

Entretanto, na versão de `app.py`, não existe um fluxo correspondente para concluir a corrida e liberar novamente o motorista.

**Como melhorar:** implementar situações para a corrida, como solicitada, em andamento e concluída. Quando a corrida terminar, atualizar a disponibilidade do motorista de acordo com a regra definida.

### 3. Evitar duplicação de informações e regras

O projeto contém estruturas semelhantes em diferentes arquivos e funções extensas que concentram muitas etapas.

**Como melhorar:** separar as regras de cadastro, busca, cálculo e confirmação em funções menores. Manter uma versão principal do cálculo de preço para evitar diferenças entre implementações.

## Oportunidades de melhoria

### 4. Fortalecer a validação dos cadastros

O programa já verifica algumas informações, como idade e placa de veículo. Essas validações podem ser ampliadas para os demais campos.

**Como melhorar:** impedir informações obrigatórias vazias, padronizar telefones e placas e verificar a consistência dos dados utilizados para identificar passageiros e motoristas.

### 5. Melhorar a organização do código

As funções de cadastro e solicitação de corrida são extensas e realizam várias tarefas dentro do mesmo bloco.

**Como melhorar:** separar a coleta de dados, a validação, a busca de motoristas, o cálculo da tarifa e a confirmação do pedido.

### 6. Preparar a evolução do armazenamento

Os dados das corridas e dos cadastros são mantidos em listas durante a execução.

**Próximo passo:** planejar a persistência dessas informações na etapa correspondente da Situação de Aprendizagem. O banco de dados não era uma exigência da Atividade 01.

### 7. Completar a documentação

O código possui muitos comentários, mas o README ainda deve orientar a execução e explicar as diferenças entre os arquivos disponíveis.

**Como melhorar:** documentar a versão principal, as funcionalidades, as modalidades de transporte, as regras de tarifa e os testes realizados.

## Testes recomendados

1. Cadastrar motoristas e passageiros com dados válidos.
2. Tentar cadastrar veículos com placas repetidas.
3. Informar idade e distância inválidas.
4. Solicitar corrida em diferentes categorias.
5. Verificar os preços calculados.
6. Solicitar corrida sem motoristas disponíveis.
7. Confirmar e cancelar uma solicitação.
8. Concluir uma corrida e verificar se o motorista volta a ficar disponível.
9. Comparar os comportamentos de `app.py` e `codigo_prova.py`.

## Prioridades para a próxima versão

1. **Definir e documentar o arquivo principal da aplicação.**
2. **Implementar o encerramento das corridas e a atualização da disponibilidade dos motoristas.**
3. **Reduzir a duplicação de código.**
4. **Ampliar as validações dos cadastros.**
5. **Registrar testes dos cálculos e dos fluxos de corrida.**

## Mensagem final

Wagner, seu projeto demonstra compreensão de **orientação a objetos, funções, condições, repetição e construção de regras de negócio**. Você conseguiu relacionar diferentes entidades e implementar um fluxo de solicitação de transporte.

Continue aprimorando a organização das funcionalidades e a consistência das informações durante as corridas. **Documentar uma versão principal, testar cada etapa e concluir o ciclo das solicitações serão avanços importantes para tornar seu sistema mais confiável.**
