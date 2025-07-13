# Projeto-gil

Objetivo: Desenvolver um sistema de gerenciamento de tarefas para uma startup de logística, utilizando a metodologia ágil (Kanban). O sistema ajudará a equipe a acompanhar as tarefas em tempo real, priorizar tarefas críticas e monitorar o desempenho.


Escopo: O sistema permitirá o acompanhamento das tarefas da equipe em tempo real, priorização de tarefas e monitoramento do desempenho. A aplicação foi construída com a metodologia ágil e utiliza uma interface gráfica simples com o Tkinter.


Metodologia: Será utilizada a metodologia Kanban para o gerenciamento das tarefas durante o desenvolvimento do projeto. As tarefas serão organizadas nas colunas A Fazer, Em Progresso, e Concluído.


**Tecnologias Usadas**

Linguagem: Python
Framework: Tkinter (para a interface gráfica)
Banco de Dados: SQLite (para persistência de tarefas)
Testes: PyTest


**Funcionalidades Implementadas**

Adicionar Tarefa: Permite adicionar tarefas com título, descrição e status (A Fazer, Em Progresso, Concluído).
Editar Tarefa: Permite editar as informações de uma tarefa existente.
Excluir Tarefa: Prmite excluir tarefas da lista.
Exibir Tarefas: A interface gráfica exibe as tarefas com seu respectivo status (A Fazer, Em Progresso, Concluído).
Persistência de Dados: As tarefas são salvas em um banco de dados SQLite, garantindo que os dados sejam preservados entre as execuções.


**Mudanças no Escopo**

Durante o desenvolvimento, a funcionalidade de priorização de tarefas foi adicionada, permitindo que o usuário defina a ordem de prioridade das tarefas, com base na criticidade das mesmas. Isso foi solicitado pelo cliente para melhorar o gerenciamento do fluxo de trabalho.


**Quadro Kanban**

Este projeto seguiu a metodologia Kanban, onde as tarefas foram organizadas nas seguintes colunas:

*A Fazer*
Criar funcionalidade de adicionar tarefas.
Implementar a visualização de tarefas na interface.

*Em Progresso*
Criar funcionalidade de edição de tarefas.
Adicionar a funcionalidade de remover tarefas.

*Concluído*
Teste de funcionalidade do CRUD (Create, Read, Update, Delete).
Testar a persistência das tarefas no banco de dados.
