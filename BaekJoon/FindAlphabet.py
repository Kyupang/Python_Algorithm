word = input()
Alphabet = ['a','b','c','d','e','f','g',
            'h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u',
            'v','w','x','y','z']
result =[-1 for i in range(len(Alphabet))]
for i in range(len(word)):
    for j in range(len(Alphabet)):
        if word[i] == Alphabet[j]:
            if result[j] == -1:
                result[j] = i
for i in range(len(result)):
    print(result[i], end=' ')
