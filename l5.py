import string
def find_longest_word(words):
    return max(words,key=len,default="")
def categorize_words(sentence):
   vowels="AEIOUaeiou"
   vowel_words,consonant_words=[],[]
   for word in sentence.split():
     word=word.strip(string.punctuation)
     if word:
       (vowel_words if word[0] in vowels else consonant_words).append(word)
   return vowel_words,consonant_words
sentence=input("Enter a sentence:")
vowel_list,consonant_list=categorize_words(sentence)
print("vowel words:",vowel_list)
print("consonants words:",consonant_list)
print("Longest vowel word:",find_longest_word(vowel_list))
print("consonant vowel word:",find_longest_word(consonant_list))
