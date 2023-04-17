# python3

def read_input():
    input_type = input()
    P, T = "", ""
    
    try:
        if(input_type == "I"):
            P = input()
            T = input()
    except: exit()
    
    try:
        if(input_type == "F"):
            with open(f"tests/{input()}") as file:
                data = file.readlines()
                P = data[0]
                T = data[1]
                file.close()
    except: exit()
    
    return (P.rstrip(), T.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_hash(pattern : str) -> int:
    Q, B = 256, 13

    pattern_length = len(pattern)
    pattern_hash = 0

    for i in range(pattern_length):
        unicode_value = get_unicode_pos(pattern[i])
        pattern_hash = (B * pattern_hash + unicode_value) % Q

    return pattern_hash

def get_unicode_pos(value):
    return ord(value)

def get_occurrences(pattern : str, text : str): 
    Q, B = 256, 13

    pattern_length = len(pattern)
    text_lenght = len(text)

    multiplayer = 1
    for i in range(1, pattern_length):
        multiplayer = (multiplayer * B) % Q

    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_length])

    positions = list()
    for symbol_index in range(text_lenght - pattern_length + 1):
        if(pattern_hash == text_hash):
            if(text[symbol_index: symbol_index + pattern_length] == pattern):
                positions.append(symbol_index)
        
        if(symbol_index < text_lenght - pattern_length):
            set_1 = get_unicode_pos(text[symbol_index])
            set_2 = get_unicode_pos(text[symbol_index + pattern_length])

            text_hash = ((text_hash - set_1 * multiplayer) * B + set_2) % Q

            if(text_hash < 0): text_hash += Q

    return positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

