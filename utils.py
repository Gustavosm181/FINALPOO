import json
from typing import Any

def salvar_json(caminho: str, dados: Any):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_json(caminho: str) -> Any:
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
