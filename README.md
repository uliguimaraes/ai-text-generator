# ai-text-generator

> Um pequeno laboratório em **Python** para transformar prompts simples em respostas automáticas, funcionando como uma primeira ponte entre lógica condicional, entrada do usuário e geração de texto.

## Visão geral

O **ai-text-generator** é um projeto de console que simula um gerador de textos orientado por palavras-chave. A aplicação lê um prompt digitado pelo usuário, normaliza o texto para letras minúsculas e retorna uma resposta pronta quando reconhece temas como tênis, inteligência artificial ou resumo. Quando o tema não está cadastrado, o programa devolve uma resposta genérica baseada no próprio prompt.

| Aspecto | Descrição |
|---|---|
| Linguagem | **Python** |
| Arquivo principal | `main.py` |
| Interface | Terminal |
| Ideia central | Receber uma solicitação textual e produzir uma resposta automática |
| Conceitos praticados | Funções, condicionais, entrada de dados, saída formatada e organização de fluxo |

## Como funciona

A função `gerar_texto(prompt)` concentra a lógica do projeto. Ela interpreta o texto digitado pelo usuário e decide qual resposta será exibida. Esse desenho torna o código fácil de expandir: basta criar novas condições para novos temas ou substituir as respostas fixas por chamadas a uma API de IA no futuro.

```text
Usuário digita um prompt
        ↓
Programa normaliza o texto
        ↓
Condições procuram palavras-chave
        ↓
Resposta personalizada é exibida no terminal
```

## Como executar

Certifique-se de ter o **Python** instalado em sua máquina. A linguagem é amplamente usada para automação, scripts e aplicações de dados, e pode ser executada diretamente pelo terminal.[1]

```bash
git clone https://github.com/uliguimaraes/ai-text-generator.git
cd ai-text-generator
python main.py
```

Em algumas instalações, o comando pode ser:

```bash
python3 main.py
```

## Possíveis evoluções

Este projeto pode crescer para um gerador real conectado a uma API externa, com histórico de prompts, categorias de resposta, interface gráfica ou integração com modelos de linguagem. Uma melhoria imediata seria remover a variável `API_KEY` quando ela não estiver em uso ou carregar chaves sensíveis por variáveis de ambiente.

## Referências

[1]: https://docs.python.org/3/ "Python 3 Documentation"
