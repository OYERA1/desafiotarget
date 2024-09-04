def checkString(strs: str) -> str:
    acc = {"A": 0, 'a': 0}
    
    for i in strs:
        if i == "A":
            if i in acc:
                acc['A'] += 1
        elif i == 'a':
            if i in acc:
                acc['a'] += 1
    
    if acc["A"] > 0 or acc["a"] > 0:
        return f'Existe A com uma ocorrencia de {acc["A"]} vez(es) e a com uma ocorrencia de {acc["a"]} vez(es).'
    
    if acc["A"] > 0:
        return f'Existe apenas A com uma ocorrencia de {acc["A"]} vez(es).'
    elif acc["a"] > 1:
        return f'Existe apenas a com uma ocorrencia de {acc["a"]} vez(es).'
    
    return 'Não existe nenhum A ou a'    


string = 'Amo A Charli XCX'
print(checkString(string))