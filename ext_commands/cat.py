if len(prompt) > 1:
    f = open(' '.join(prompt[1:]), 'r')
    print(f.read())
    f.close()
else:
    print('cat: usage: cat <filename>')
