# 🧠 HashCrackr

Uma ferramenta simples e direta pra quebrar hashes usando força bruta.  
Feita com Python, sem firula, pra quem quer resultado.

---

## ⚙️ Como funciona?

Lê um arquivo com hashes (com ou sem salt) e tenta quebrar cada uma usando uma wordlist.

### Suporta:
- `md5`
- `sha1`
- `sha256`
- Formatos com:
  - `hash`
  - `salt$hash`
  - `salt:hash`

---

## 🚀 Como usar

### Pré-requisitos:
- Python 3.6+

### Comando:

```bash
python hashcrackr.py -f examples.txt -w rockyou.txt
