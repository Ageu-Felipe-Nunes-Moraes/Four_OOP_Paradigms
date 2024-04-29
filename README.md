# Programação Orientada a Objetos: Conceitos Fundamentais

Neste código, exploro os princípios essenciais da Programação Orientada a Objetos (POO) através da implementação de classes em Python. Vamos examinar cada um desses conceitos e como estão aplicados no código fornecido:

## Abstração

Abstração é o processo de destacar informações importantes enquanto oculta detalhes desnecessários. No código, vemos que as classes e métodos são projetados para focar nas funcionalidades essenciais de cada objeto, como fazer um som específico, sem se preocupar com a implementação interna.

## Encapsulamento

O encapsulamento organiza o código de forma a proteger seus componentes internos, permitindo alterações futuras com menor impacto em outras partes do sistema. No código, as propriedades das classes são definidas como privadas (`_nome`) para controlar o acesso externo, seguindo o princípio do encapsulamento.

## Polimorfismo

O polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme, possibilitando que métodos com o mesmo nome se comportem de maneira diferente em cada classe. No exemplo, cada animal tem um método `fazer_som()`, que é polimórfico, produzindo sons distintos para cada tipo de animal.

## Herança

A herança permite que uma classe filha herde atributos e métodos de uma classe pai, promovendo reutilização de código e facilitando a organização hierárquica de objetos. No código, vemos a hierarquia de classes onde `AnimalSilvestre` e `AnimalDomestico` herdam de `Animal`, e `Cobra`, `Cachorro` e `Gato` herdam de `AnimalSilvestre` e `AnimalDomestico`, respectivamente.

## Requisitos de Instalação

- Python 3.x

## Como Executar

1. Certifique-se de ter Python instalado em seu sistema.
2. Clone ou baixe o repositório deste código.
3. Execute o arquivo principal.

## Contribuições

Se deseja contribuir para o desenvolvimento deste código:

1. Fork o repositório.
2. Faça suas modificações e melhorias no código.
3. Teste suas alterações para garantir o funcionamento correto.
4. Envie um pull request descrevendo as alterações feitas e suas justificativas.

## Autor

Este jogo foi desenvolvido por Ageu Felipe Nunes Moraes(eu) com o propósito de sintetizar ao máximo um dos conteúdos de POO, como parte de um projeto pessoal dedicado ao fortalecimento e amadurecimento da codificação. Para quaisquer dúvidas ou sugestões, por favor, entre em contato pelo e-mail [ageumoraes67@gmail.com].

## Aviso Legal

Este é um projeto de software desenvolvido por um indivíduo. Inspirado por atividade acadêmica passada durante aula.
