# Create a groupAnagram Checker
# output = [["eat", "ate", "tea"],["nat", "bat"]]
input = ["eat", "tea", "nat", "bat", "ate"]

def group_anagram(input):
    
    base_text = "".join(sorted(input[0]))
    print("BASE:", base_text)
    
    anagram = []
    not_anagram = []
    
    for i in input:
        current = list(i)
        current.sort()
        current = "".join(current)
        
        if current == base_text:
            anagram.append(i)
        else:
            not_anagram.append(i)
    
    return [anagram, not_anagram]
    
    
print(group_anagram(input))
