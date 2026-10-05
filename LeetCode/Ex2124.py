# A implementação verifica se todos os caracteres `'a'` aparecem antes dos caracteres `'b'`. Para isso, utiliza `rfind("a")` para encontrar a posição do último `'a'` e `find("b")` para encontrar a posição do primeiro `'b'`, garantindo que o último `'a'` esteja antes do primeiro `'b'`. Caso a string contenha apenas `'a'` ou apenas `'b'`, retorna `True`, pois nesses casos a condição já é válida.


def checkString(self, s: str) -> bool:
    # return list(s) == sorted(s)
    return s.rfind("a") < s.find("b") if "a" in s and "b" in s else True


s = "aaabbb"
print(checkString(None, s))
