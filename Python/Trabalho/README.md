# Trabalho de Paradigmas de Programação em Python

## Objetivo

O objetivo do trabalho é exercitar o POO, criando uma classe produto e 

um menu interativo para poder adicionar produtos, adicionar preços, atualizar quantidades e listar produtos.

## Funcionalidades do menu

Adicionar produtos

Atualizar preços

Atualizar quantidades

Listar produtos

## Estrutura do projeto

O projeto está organizado da seguinte forma:

produto.py: Define a classe produto.

menu.py(arquivo principal): Contém a função menu() que fornece a interação para gerenciar os produtos.

## Classe Produto

### Atributos

nome:Implementa o nome do produto

preco:Indica o valor do produto.

quantidade: exibe a quantidade daquele produto.

### Métodos

São os comportamentos dos produtos.

__init__(nome,preco,quantidade): Inicializa um novo produto com nome,preco e quantidade.

Atualizar_quantidade: Atualiza a quantidade de produtos.

Atualizar_preco: Atualiza o preço do produto para um novo valor.

produtos.append(produto): Adiciona o produto.

### Estruturas utilizadas 

While: Estrutura de repetição para que o menu seja exibido até que o usuário escolha essa opção.

If: Estrutura de condição para tratamento de erros.

For: Estrutura de repetição para gerenciar os dados dentro da lista produtos.

