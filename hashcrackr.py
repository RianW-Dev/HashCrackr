import argparse
from core.cracker import crack_hashes

print("Ta rodando")

def main():
    parser = argparse.ArgumentParser(description="HashCrackr - Uma simples ferramenta de quebra de hashes.")
    parser.add_argument('-f', '--file', help="Arquivo com hashs", required=True)
    parser.add_argument('-w', '--wordlist', help="Wordlist para o bruteforce", required=True)
    args = parser.parse_args()

    crack_hashes(args.file, args.wordlist)


if __name__ == "__main__":
    main()
