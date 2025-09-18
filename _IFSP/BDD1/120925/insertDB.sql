-- 3 Usuario(s)
-- 3 Materia(s)
-- 7 Prova(s) -> 3 Questao(s)
-- 21 Questao(s) -> 4 Alternativa(s)


INSERT INTO Configuracao(
	ocultar_questoes_outros_usuario,
	exibe_material_inativa,
    exibe_alternativa
)VALUES
	(FALSE, TRUE, TRUE),
	(TRUE, TRUE, TRUE),
	(FALSE, FALSE, TRUE)
;

INSERT INTO Usuario(
	id_configuracao,
    email,
    nome_completo,
    senha,
    administrador
)VALUES
	(1, "artur@gmail.com", "Artur Regadas", "1234", TRUE),
	(2, "davi@gmail.com", "Davi Ribeiro", "2999", FALSE),
	(3, "gabriel@gmail.com", "Gabriel Nascimento", "9992",FALSE)
;


INSERT INTO Materia(
    nome,
    sigla,
    curso,
    inativa
) VALUES
    ("Banco de Dados", "BD", "Engenharia de Software", FALSE),
    ("Estruturas de Dados", "ED", "Ciência da Computação", FALSE),
    ("Algoritmos", "ALG", "Sistemas de Informação", FALSE)
;

INSERT INTO Prova(
    id_materia,
    id_usuario,
    descricao,
    tema,
    data_prova
) VALUES
    (1, 1, "Prova sobre normalização e SQL básico", "Modelagem Relacional", "2025-03-01"),
    (1, 1, "Avaliação de consultas SQL avançadas", "SQL Avançado", "2025-03-15"),
    (2, 1, "Prova sobre árvores e grafos", "Estruturas Não Lineares", "2025-04-05"),
    (2, 2, "Prova de listas, pilhas e filas", "Estruturas Lineares", "2025-04-20"),
    (3, 2, "Avaliação sobre recursão", "Recursividade", "2025-05-02"),
    (3, 2, "Prova de busca e ordenação", "Algoritmos de Ordenação", "2025-05-18"),
    (3, 3, "Grafos e seus algortimos", "Grafos", "2026-02-11")
;

INSERT INTO Questao(
    id_usuario,
    enunciado,
    verificada
) VALUES
    (1, "Explique a 1ª forma normal e dê um exemplo.", TRUE),
    (1, "Qual a diferença entre chave primária e chave estrangeira?", TRUE),
    (1, "O que significa integridade referencial?", TRUE),
    (1, "Explique o funcionamento de um JOIN em SQL.", TRUE),
    (2, "O que é uma subquery?", TRUE),
    (2, "Qual a diferença entre UNION e UNION ALL?", FALSE),
    (3, "Defina árvore binária e cite aplicações.", TRUE),
    (3, "Explique o que é um grafo dirigido.", TRUE),
    (3, "Qual a complexidade da busca em largura?", FALSE),
    (1, "Explique a diferença entre pilha e fila.", TRUE),
    (2, "Descreva a operação de inserção em uma lista encadeada.", TRUE),
    (3, "Qual a complexidade de acesso em vetor e lista encadeada?", FALSE),
    (1, "Explique o conceito de recursão com exemplo.", TRUE),
    (2, "O que é caso base em uma função recursiva?", TRUE),
    (2, "Dê um exemplo de recursão indireta.", FALSE),
    (3, "Explique o funcionamento do QuickSort.", TRUE),
    (3, "Qual a complexidade do MergeSort?", TRUE),
    (3, "Compare InsertionSort e SelectionSort.", FALSE),
    (1, "Para que serve o algortimo de Dijkstra", FALSE),
    (1, "Para que serve o algortimo de Kruskal", FALSE),
    (1, "Para que serve um DFS", FALSE)
;

INSERT INTO Alternativa(
    id_questao,
    texto,
    certa
) VALUES
    (1, "Organizar dados sem colunas multivaloradas ou repetidas", TRUE),
    (1, "Permitir colunas repetidas na tabela", FALSE),
    (1, "Eliminar todas as chaves estrangeiras", FALSE),
    (1, "Trasnformar as coisas", FALSE),

    (2, "Chave primária identifica unicamente um registro", TRUE),
    (2, "Chave estrangeira pode referenciar outra tabela", TRUE),
    (2, "Não existe diferença entre ambas", FALSE),
    (2, "Na verdade nao existem chaves primarias", FALSE),

    (3, "Assegura que os valores de chaves estrangeiras existam na tabela referida", TRUE),
    (3, "Permite qualquer valor em chave estrangeira", FALSE),
    (3, "É usada apenas para índices", FALSE),
    (3, "Uma chave para um banco de dados", FALSE),

    (4, "JOIN combina dados de duas ou mais tabelas com base em colunas relacionadas", TRUE),
    (4, "JOIN serve apenas para excluir registros", FALSE),
    (4, "JOIN substitui a chave primária da tabela", FALSE),
    (4, "Não existe join no SQL", FALSE),

    (5, "É uma consulta dentro de outra consulta SQL", TRUE),
    (5, "É uma tabela temporária criada pelo SGBD", FALSE),
    (5, "É um tipo especial de índice", FALSE),
    (5, "É uma query inexistente", FALSE),

    (6, "UNION remove duplicatas enquanto UNION ALL mantém todas as linhas", TRUE),
    (6, "UNION e UNION ALL são sempre equivalentes", FALSE),
    (6, "UNION ALL ordena automaticamente os resultados", FALSE),
    (6, "UNION ALL e UNION são pesquisas, uma retorna sem restrições e outra com", FALSE),

    (7, "Árvore binária é uma estrutura onde cada nó tem até dois filhos", TRUE),
    (7, "Árvore binária é sempre completamente balanceada", FALSE),
    (7, "Árvore binária só pode armazenar números inteiros", FALSE),
    (7, "Arvore binária pe uma estrutura que só pode ser representada por um array", FALSE),

    (8, "Um grafo dirigido possui arestas com orientação definida", TRUE),
    (8, "Um grafo dirigido não possui vértices", FALSE),
    (8, "Um grafo dirigido é sempre acíclico", FALSE),
    (8, "Um grafo dirigido nao possui arestas", FALSE),

    (9, "A busca em largura possui complexidade O(V + E)", TRUE),
    (9, "A busca em largura possui complexidade O(1)", FALSE),
    (9, "A busca em largura é mais lenta que O(V * E)", FALSE),
    (9, "A busca em largura possui complexidade O(N log N)", FALSE),

    (10, "Pilha segue LIFO e fila segue FIFO", TRUE),
    (10, "Pilha e fila funcionam exatamente da mesma forma", FALSE),
    (10, "Fila segue LIFO e pilha segue FIFO", FALSE),
    (10, "Pilha e fila seguem FIFO", FALSE),

    (11, "Inserção em lista encadeada exige criação de novo nó e ajuste de ponteiros", TRUE),
    (11, "Inserção em lista encadeada não é possível", FALSE),
    (11, "Inserção em lista encadeada não altera ponteiros", FALSE),
    (11, "Inserção não usa nodos", FALSE),

    (12, "Acesso em vetor é O(1) e em lista encadeada é O(n)", TRUE),
    (12, "Ambos possuem acesso O(1)", FALSE),
    (12, "Ambos possuem acesso O(n)", FALSE),
    (12, "Ambois possuem acesso em (log N)", FALSE),

    (13, "Recursão é quando uma função chama a si mesma", TRUE),
    (13, "Recursão é usar apenas laços for e while", FALSE),
    (13, "Recursão é aplicar herança em programação orientada a objetos", FALSE),
    (13, "Recursão é utilizar atributos de uma classe nessa mesma class", FALSE),

    (14, "Caso base é a condição que termina a recursão", TRUE),
    (14, "Caso base é a função principal do programa", FALSE),
    (14, "Caso base é a função que chama outra função recursiva", FALSE),
    (14, "Caso base é a primeira funcão ao ser chamada em um codigo", FALSE),

    (15, "Recursão indireta ocorre quando funções chamam umas às outras", TRUE),
    (15, "Recursão indireta é o mesmo que loop infinito", FALSE),
    (15, "Recursão indireta não existe em programação", FALSE),
    (15, "Recursão indireta é uma chamada de funcao referente ao caso base", FALSE),

    (16, "QuickSort usa divisão e conquista escolhendo um pivô", TRUE),
    (16, "QuickSort sempre ordena em tempo constante", FALSE),
    (16, "QuickSort só funciona com listas encadeadas", FALSE),
    (16, "QuickSort ordena pegando o menor do array, de forma que no final esteja ordenado", FALSE),

    (17, "MergeSort tem complexidade O(n log n)", TRUE),
    (17, "MergeSort tem complexidade O(1)", FALSE),
    (17, "MergeSort é mais lento que O(n²)", FALSE),
    (17, "MergeSort tem complexidade O(N)", FALSE),

    (18, "InsertionSort é eficiente para listas pequenas e SelectionSort seleciona mínimo em cada passo", TRUE),
    (18, "InsertionSort é sempre mais rápido que QuickSort", FALSE),
    (18, "SelectionSort possui complexidade O(1)", FALSE),
    (18, "SelectionSort possui complexidade linear", FALSE),

    (19, "Para Saber o menor caminho de um nodo a outro em um grafo com ponderado com pesos maiores que 0", TRUE),
    (19, "Para Saber a MST(Arvore Geradora Minima) de um grafo", FALSE),
    (19, "Caminhar em um grafo por uso de uma pilha", FALSE),
    (19, "Não tem utilidade", FALSE),

    (20, "Para Saber a MST(Arvore Geradora Minima) de um grafo", TRUE),
    (20, "Para Saber o menor caminho de um nodo a outro em um grafo com ponderado com pesos maiores que 0", FALSE),
    (20, "Caminhar em um grafo por uso de uma pilha", FALSE),
    (20, "Não tem utilidade", FALSE),

    (21, "Caminhar em um grafo por uso de uma pilha", TRUE),
    (21, "Para Saber a MST(Arvore Geradora Minima) de um grafo", FALSE),
    (21, "Para Saber o menor caminho de um nodo a outro em um grafo com ponderado com pesos maiores que 0", FALSE),
    (21, "Não tem utilidade", FALSE)
;

INSERT INTO ProvaQuestao(
    id_prova,
    id_questao
)VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 7), 
    (3, 8),
    (3, 9),
    (4, 10),
    (4, 11),
    (4, 12),
    (5, 13),
    (5, 14),
    (5, 15),
    (6, 16),
    (6, 17),
    (6, 18),
    (7, 19),
    (7, 20),
    (7, 21)
;