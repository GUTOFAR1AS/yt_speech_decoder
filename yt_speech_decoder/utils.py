import re

def clean_filename(name: str) -> str:
    """
    Remove caracteres inválidos do nome do arquivo.
    """
    return re.sub(r'[\\/*?:"<>|]', "", name)
