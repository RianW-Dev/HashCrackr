# 🧠 HashCrackr

Ferramenta simples e direta pra quebrar hashes usando força bruta.  
Feita em Python.

## ⚙️ Como funciona?

Lê um arquivo com hashes (com ou sem salt) e tenta quebrar cada um usando uma wordlist.

Suporta:  
- md5  
- sha1  
- sha256  

Formatos aceitos:  
- hash  
- salt$hash  
- salt:hash  

## 🛠️ Como instalar

1. Clone o repositório:  
```bash
git clone https://github.com/RianW-Dev/HashCrackr.git
cd HashCrackr

(Opcional, mas recomendado) Crie e ative um ambiente virtual:
Linux/Mac:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

🚀 Como usar
Pré-requisitos:
Python 3.6+

Comando:
python hashcrackr.py -f examples.txt -w rockyou.txt
