
def anagram( listLetters ) :
    listAnagram = []
    if len(listLetters) == 1 :
        listAnagram.append(listLetters[0])
    else :
        for i in range(0, len(listLetters)) :
            underListLetters = []
            for j in range(len(listLetters)) :
                 if j != i :
                    underListLetters.append(listLetters[j])
            underListAnagram = anagram(underListLetters)
            for j in range (len(underListAnagram)) :
                listAnagram.append (listLetters[i] + underListAnagram[j])
    return listAnagram

word = input("Entrez une chaine de caractère : ")
listLetters = []
for i in range(0, len(word)) :
    listLetters.append(word[i])

listAnagrams = anagram(listLetters)
for i in range (len(listAnagrams)) :
    print (listAnagrams[i])
