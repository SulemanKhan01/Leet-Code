def anagramGroup(arr):
    ana_group = {}

    for word in arr:
        sorted_word = "".join(sorted(word))
        
        if sorted_word in ana_group:
            ana_group[sorted_word].append(word)

        else:
            ana_group[sorted_word] = [word]

    group = list(ana_group.values())

    return group

        



strs = ["act","pots","tops","cat","stop","hat"]
print(anagramGroup(strs))