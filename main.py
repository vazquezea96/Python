def correct(s):
    character_recong = {5: 'S', 0: 'O', 1: 'I'}
    for old, new in character_recong.items():
        s = s.replace(str(old), new)
    return s

print(correct("L0ND0N"))