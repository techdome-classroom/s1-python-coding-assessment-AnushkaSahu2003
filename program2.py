def decode_message(secret: str, key: str) -> bool:
    # Initialize pointers 
    i, j = 0, 0
    star_idx = -1  # Position of the last star 
    match_idx = 0  # Position in the secret message

    while i < len(secret):
        # If characters match or there is a ? continuee
        if j < len(key) and (key[j] == secret[i] or key[j] == '?'):
            i += 1
            j += 1
        
        elif j < len(key) and key[j] == '*':
            star_idx = j
            match_idx = i
            j += 1
       
        elif star_idx != -1:
            j = star_idx + 1
            i = match_idx + 1
            match_idx += 1
        else:
            return False

    # Check for any remaining charactersgit status

    while j < len(key) and key[j] == '*':
        j += 1

    return j == len(key)
