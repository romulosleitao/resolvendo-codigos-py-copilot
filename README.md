# 🐍 Resolução de Desafios em Python com Gemini

Repositório criado para a entrega do desafio prático de Python, focado em manipulação de dados, estruturas básicas e boas práticas de programação, utilizando Inteligência Artificial como suporte de desenvolvimento.

## 🎯 Objetivos de Aprendizagem Alcançados
* **Reprodução e Melhoria:** Compreensão e implementação de scripts em Python baseados em problemas práticos iniciais.
* **Aplicação Prática:** Uso de conceitos fundamentais como manipulação de strings, conversão de tipos de dados, operações aritméticas e entrada de dados via terminal (`input`).
* **Documentação Técnica:** Registro claro do raciocínio e das decisões de código tomadas no projeto.
* **Versionamento com Git/GitHub:** Organização e hospedagem do código-fonte em um repositório público na nuvem.

---

## 🛠️ Metodologia e Ferramentas Utilizadas

Para a resolução dos códigos deste repositório, utilizou-se o **Google Gemini** como um assistente de desenvolvimento (*Copilot de Estudos*), simulando o fluxo de trabalho com ferramentas de IA generativa para otimização, estruturação e explicação lógica dos algoritmos.

* **Linguagem:** Python 3
* **Assistente de IA:** Google Gemini
* **Ambiente de Versionamento:** Git & GitHub

---

## 💻 Explicação das Resoluções

O projeto é composto por três scripts principais que solucionam problemas fundamentais de lógica de programação:

### 1. Concatenando Dados (`concat_dados.py`)
* **O que faz:** Recebe dois valores distintos inseridos pelo usuário e os une em uma única string formatada.
* **Decisão técnica:** Utilizou-se a tipagem padrão de inputs do Python combinada com o operador de adição (`+`) e espaços controlados para garantir que os dados fossem exibidos de forma legível.

### 2. Repetindo Textos (`repet_txt.py`)
* **O que faz:** Solicita uma string e um número inteiro, retornando a repetição dessa string conforme o valor informado.
* **Decisão técnica:** Realizou-se a conversão explícita da entrada numérica utilizando `int(input())` para permitir a multiplicação de strings em Python (`texto * vezes`), tratando a repetição de forma direta e eficiente.

### 3. Operações Matemáticas Simples (`ope_mat.py`)
* **O que faz:** Captura dois números informados pelo usuário e executa uma operação matemática básica (soma).
* **Decisão técnica:** Utilizou-se a conversão para `float` para abranger tanto números inteiros quanto decimais, aplicando f-strings (`f"{...}"`) na exibição do resultado para manter o código limpo, moderno e de fácil leitura.

---

## 📁 Estrutura do Repositório

```text
├── concat_dados.py   # Script de concatenação de strings
├── repet_txt.py      # Script de repetição de textos com inteiros
├── ope_mat.py        # Script de operações matemáticas básicas
└── README.md         # Documentação detalhada do projeto
