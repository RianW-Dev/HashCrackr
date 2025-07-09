import hashlib
from core.hashtypes import detect_hash_type

def crack_hashes(hash_file, wordlist_file): 
    with open(hash_file, 'r') as hf:
        hashes = [line.strip() for line in hf.readlines()]

    with open(wordlist_file, 'r', encoding='latin-1') as wf:
        wordlist = [word.strip() for word in wf.readlines()]

    for line in hashes:  
        line = line.strip()
        if not line:
            continue  

        if '$' in line or ':' in line:
            salt, hash_value = split_salt_hash(line)
        else:
            salt, hash_value = '', line

        hash_type = detect_hash_type(hash_value)
        print(f"Tentando quebrar a hash: {hash_value} (tipo: {hash_type})")

        for word in wordlist:
            attempt = word if not salt else salt + word

            if hash_type == 'md5':
                hashed = hashlib.md5(attempt.encode()).hexdigest()
            elif hash_type == 'sha1':
                hashed = hashlib.sha1(attempt.encode()).hexdigest()
            elif hash_type == 'sha256':
                hashed = hashlib.sha256(attempt.encode()).hexdigest()
            else:
                continue

                print(f"Tentando com: {attempt} => {hashed}")  

            if hashed == hash_value:
                print(f"[+] A Hash foi quebrada! Valor: {word}")
                break
        else:
            print("[-] Nenhuma correspondência encontrada.")

def split_salt_hash(line):
    if '$' in line:
        parts = line.strip().split('$', 1)
        if len(parts) == 2:
            return parts[0], parts[1]
        else:
            return '', line  
    elif ':' in line:
        return line.strip().split(':', 1)
    return '', line
