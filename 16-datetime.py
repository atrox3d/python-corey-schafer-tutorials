#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################


def hashline(width=160, char='#'):
    print(char * width)


def banner(text, height=3, width=160, char='#'):
    hashline(width, char)
    spacing = height // 2 + 1
    for spaceline in range(1, spacing):
        print(char)
    print(f'{char} {text}')
    for spaceline in range(1, spacing):
        print(char)
    hashline(width, char)
