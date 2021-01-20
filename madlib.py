#string concatenation
#madlibs
print('Hello! Thank you trying out this madlibs game! Please enter each noun, adjective, or verb when prompted and enjoy!\n')
#below we will remove some nouns adjectives and verbs throughout the quote and allow the user to input the data based on the prompt. I need to figure out a way to disallow int or floats in the so it only allows strings.
noun1 = input('noun: ')
adj1 = input('adjective: ')
noun2 = input('another noun: ')
adj2 = input('another adjective: ')
noun3 = input('next noun: ')
verb1 = input('verb: ')
verb2 = input('another verb: ')
verb3 = input('next verb: ')
verb4 = input('another another verb: ')
verb5 = input('final verb?: ')

#below is a quote from the 2008 movie Taken  I thought it would be fun to replace some of the words and see what kind of wacky things will be turned out with it. 
madlibs = (f"I don't know who you are. I don't know what you want. If you are looking for a/an {noun1} I can tell you I don't have a {noun1}, but what I do have are a very {adj1} set of {noun2}s. {noun2}s I have acquired over a very {adj2} career. {noun2.title()}s that make me a nightmare for people like you. If you let my daughter go now that'll be the end of it. I will not {verb1} for you, I will not {verb2} you, but if you don't, I will {verb3} for you, I will {verb4} you and I will {verb5} you.")

print(madlibs)
