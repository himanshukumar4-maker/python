#Write a function to calculate the unique elements in both the  list.
# a1=[1,2,3,4]
# a2=[2,3,5,6]

# def unique(a1,a2):
#     print(set(a1)^set(a2)) 
# unique(a1,a2)

#Write a python function to print the count of unique words in the given sentence.
S='The cat and the hat' 
def count_unique_words(S):
    return len(set(S.lower().split()))
print(count_unique_words(S))

    
 