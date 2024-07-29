import requests
from deep_translator import GoogleTranslator
from typing import Tuple


class Colors:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"

def get_random_quote() -> dict:

    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise SystemExit(f"{Colors.RED}Erro ao obter citação: {e}{Colors.RESET}")

def translate_text(text: str, target_language: str = 'pt') -> str:

    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        return translator.translate(text)
    except Exception as e:
        raise SystemExit(f"{Colors.RED}Erro ao traduzir o texto: {e}{Colors.RESET}")

def print_translated_quote(author: str, translated_content: str) -> None:

    print(f"\n\n{Colors.GREEN}{author}{Colors.RESET}: \"{Colors.BLUE}{translated_content}{Colors.RESET}\" \n\n")

def main() -> None:

    print(f"{Colors.YELLOW}Bem-vindo ao Gerador de Frases.{Colors.RESET}")
    print(f"{Colors.YELLOW}Este aplicativo gera citações aleatórias.{Colors.RESET}\n")

    while True:
        user_input = input("Pressione Enter para gerar uma nova frase ou digite 'sair' para encerrar: ").strip().lower()
        
        if user_input == 'sair':
            print(f"{Colors.RED}Saindo...{Colors.RESET}")
            break

        try:
            quote = get_random_quote()
            quote_content = quote['content']
            quote_author = quote['author']
            translated_content = translate_text(quote_content, 'pt')

            print_translated_quote(quote_author, translated_content)
        
        except SystemExit as e:
            print(e)

if __name__ == "__main__":
    main()
