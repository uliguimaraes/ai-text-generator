import requests

API_KEY = "SUA_CHAVE_AQUI"

def gerar_texto(prompt):
    prompt = prompt.lower()

    if "tênis" in prompt:
        return "Tênis esportivo leve e confortável, ideal para corridas e uso diário, com design moderno e alta durabilidade."

    elif "inteligência artificial" in prompt:
        return "A inteligência artificial é uma área da tecnologia que permite que máquinas aprendam e tomem decisões de forma automatizada."

    elif "resumo" in prompt:
        return "Resumo gerado automaticamente com base no conteúdo fornecido."

    else:
        return f"Texto gerado automaticamente sobre: {prompt}"

def main():
    print("=== GERADOR DE TEXTO ===")
    prompt = input("Digite o que você quer gerar: ")

    resultado = gerar_texto(prompt)
    print("\nResultado:\n")
    print(resultado)

if __name__ == "__main__":
    main()