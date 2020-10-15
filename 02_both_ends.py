"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""

# Solução #1: com uma linha

# def both_ends(s):
#     return '' if len(s) < 2 else ''.join([s[:2],s[-2:]])

# Solução #2: sem usar facilidades do Python, com while para contagem, deixando código expressivo

def both_ends(s):
    s_length = len(s)
    output = []
    if s_length > 1:
        counter = 0
        first_part, last_part = [], []
        while counter < s_length:
            if counter < 2:
                first_part.append(s[counter])
            if counter > (s_length - 3):
                last_part.append(s[counter])
            counter += 1
        output.extend([*first_part, *last_part])
    return ''.join(output)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'ha', 'haha') # Additional test with two distinct letters word
    test(both_ends, 'xyz', 'xyyz')
