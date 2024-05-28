import sys
sys.setrecursionlimit(1500000)

T = int(input())

def next_piastrelle(inst, idx, config):
    if idx == len(inst):
        return False

    if inst[idx] == 1:
        # La nostra soluzione inizia per inst[idx]
        valid_length = len(config)
        config.append(inst[idx])
        exists = next_piastrelle(inst, idx + 1, config)
        if exists:
            return True
        else:
            del config[valid_length:]
            len_bagno = sum(inst[idx:])
            if len_bagno < 2:
                return False
            config.append(2)
            for _ in range(len_bagno - 2):
                config.append(1)
            return True
    elif inst[idx] == 2:
        config.append(inst[idx])
        exists = next_piastrelle(inst, idx + 1, config)
        return exists

    # Qua la configurazione non e' valida
    return False

def prev_piastrelle(inst, idx, config):
    if idx == len(inst):
        return False
    if inst[idx] == 1:
        config.append(inst[idx])
        exists = prev_piastrelle(inst, idx + 1, config)
        return exists
    elif inst[idx] == 2:
        valid_length = len(config)
        config.append(2)
        exists = prev_piastrelle(inst, idx + 1, config)
        if exists:
            return True
        else:
            del config[valid_length:]
            len_bagno = sum(inst[idx:]) - 1
            config.append(1)
            
            while len_bagno >= 2:
                config.append(2)
                len_bagno -= 2

            if len_bagno == 1:
                config.append(1)

            return True
        
def gen_smallest_p(n):
    return ['()'] * (n // 2)

def gen_largest_p(n):
    return ['('] * (n//2) + [')'] * (n//2)

def next_parentesi(parentesi, config):
    if len(parentesi) == 0:
        return False

    assert(parentesi[0] == '(')
    counter = 1
    pos = 1
    while counter > 0:
        if parentesi[pos] == '(':
            counter += 1
        else:
            counter -= 1
        pos += 1

    part1 = parentesi[:pos] 
    part1_f = parentesi[1:pos - 1] 
    part2 = parentesi[pos:]

    valid_length = len(config)
    config += part1

    exists = next_parentesi(part2, config)
    if exists:
        return True
    
    del config[valid_length:]

    config.append('(')
    exists = next_parentesi(part1_f, config)
    config.append(')')
    if exists:
        config += gen_smallest_p(len(part2))
        return True
    
    if len(part2) == 0:
        return False

    del config[valid_length:]

    next_len_part1_f = len(part1_f) + 2
    next_len_part2 = len(part2) - 2

    config.append('(')
    config += gen_smallest_p(next_len_part1_f)
    config.append(')')
    config += gen_smallest_p(next_len_part2)
    return True

def prev_parentesi(parentesi, config):
    if len(parentesi) == 0:
        return False

    assert(parentesi[0] == '(')
    counter = 1
    pos = 1
    while counter > 0:
        if parentesi[pos] == '(':
            counter += 1
        else:
            counter -= 1
        pos += 1

    part1 = parentesi[:pos] 
    part1_f = parentesi[1:pos - 1] 
    part2 = parentesi[pos:]

    valid_length = len(config)
    config += part1

    exists = prev_parentesi(part2, config)
    if exists:
        return True
    
    del config[valid_length:]

    config.append('(')
    exists = prev_parentesi(part1_f, config)
    config.append(')')
    if exists:
        config += gen_largest_p(len(part2))
        return True
    
    if len(part1_f) == 0:
        return False

    del config[valid_length:]

    prev_len_part1_f = len(part1_f) - 2
    prev_len_part2 = len(part2) + 2

    config.append('(')
    config += gen_largest_p(prev_len_part1_f)
    config.append(')')
    config += gen_largest_p(prev_len_part2)

    return True

for t in range(T):
    inst = input()

    if inst[0] == '[':
        # Piastrelle
        piastrelle = []

        pos = 0
        while pos < len(inst):
            if inst[pos + 1] == ']':
                pos += 2
                piastrelle.append(1)
            else:
                pos += 4
                piastrelle.append(2)

        next_config = []
        next_exists = next_piastrelle(piastrelle, 0, next_config)
        prev_config = []
        prev_exists = prev_piastrelle(piastrelle, 0, prev_config)

        if not prev_exists:
            print()
        else:
            print("".join(['[]' if x == 1 else '[--]' for x in prev_config]))

        if not next_exists:
            print()
        else:
            print("".join(['[]' if x == 1 else '[--]' for x in next_config]))


        pass
    elif inst[0] == '(':
        # Parentesi
        prev_config = []
        prev_exists = prev_parentesi(inst, prev_config)
        if prev_exists:
            print("".join(prev_config))
        else:
            print()

        next_config = []
        next_exists = next_parentesi(inst, next_config)
        if next_exists:
            print("".join(next_config))
        else:
            print()

    else:
        # Numero
        numbers = [int(x) for x in inst.split()]
        base = max(numbers) + 1

        numbers_prev = [x for x in numbers]

        # 3 2 4 0 5
        # 3 2 4 0 4
        
        # 3 2 4 0
        # 3 2 3 4

        pos = len(numbers) - 1
        while pos >= 0 and numbers_prev[pos] == 0:
            numbers_prev[pos] = base - 1
            pos -= 1

        if pos < 0:
            print()
        else:
            numbers_prev[pos] -= 1
            print(" ".join([str(x) for x in numbers_prev]))

        numbers_next = [x for x in numbers]

        # 3 2 4 0 5
        # 3 2 4 1 0
        
        # 3 2 4 0
        # 3 2 4 1

        pos = len(numbers) - 1
        while pos >= 0 and numbers_next[pos] == (base - 1):
            numbers_next[pos] = 0
            pos -= 1

        if pos < 0:
            print()
        else:
            numbers_next[pos] += 1
            print(" ".join([str(x) for x in numbers_next]))
