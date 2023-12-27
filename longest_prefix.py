

# ["flee","flow","fly"]
def longest_prefix(words):
    words.sort(key=lambda x: len(x))
    length=len(words)
    prefix=""
    for i in range(len(words[0])):
        count=0
        char = words[0][i]
        for j in range(1,length):
            if char == words[j][i]:
                count+=1
        if count == length-1:
            prefix += char
        else:
             return prefix


print(longest_prefix(["flee", "flow", "fly"]))
