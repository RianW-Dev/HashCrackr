def detect_hash_type(hash_str):
    lenght = len(hash_str)
    if lenght == 32:
        return 'md5'
    elif lenght == 40:
        return 'sha1'
    elif lenght == 64:
        return 'sha256'
    else:
        return 'Desconhecido'