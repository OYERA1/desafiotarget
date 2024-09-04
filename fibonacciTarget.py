def fibonacci(target: int) -> (bool, str):
    f, s = 0, 1

    if target < 0:
        return (False, 'Não está na sequencia')
    
    while f <= target:
        if f == target:
            return (True, 'Está na sequencia')
        f, s = s, f + s
    return (False, 'Não está na sequencia')

fibonacci(610)