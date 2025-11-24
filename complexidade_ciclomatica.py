# complexidade_ciclomatica.py
import re

def remover_comentarios(code: str) -> str:
    # Remove comentários de bloco """ """ ou ''' '''
    code = re.sub(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', '', code)

    # Remove comentários de linha iniciados por #
    code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)

    return code


def calcular_complexidade_ciclomatica(code: str) -> int:
    if not isinstance(code, str):
        raise ValueError("O código deve ser uma string.")

    codigo_limpo = remover_comentarios(code)

    decision_patterns = [
        r'\bif\b',
        r'\belif\b',
        r'\bfor\b',
        r'\bwhile\b',
        r'\bexcept\b',
        r'\bwith\b',
        r'\bassert\b',
        r'\band\b',
        r'\bor\b',
        r'\?'
    ]

    complexidade = 1

    for pattern in decision_patterns:
        matches = re.findall(pattern, codigo_limpo)
        complexidade += len(matches)

    return complexidade


# Exemplo
exemplo = """
def test(x):
    # if x > 10 ignorado
    if x > 5:
        return 1
    elif x > 2:
        return 0
    return 2
"""

print("Complexidade ciclomática:", calcular_complexidade_ciclomatica(exemplo))
# Saída esperada: Complexidade ciclomática: 3