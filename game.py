print("welcome to guess the sentence game!!!")
print("\nIt is based on yourgeneral knowledge on monuments and different places in India")
print("\n Rules:")
print("\n1. total 3  levels")
print("\n2.you can enter maximum three numbers from 1-5 or 1-6 or 1-7 which will be mentioned")
print("\n3. these 3 numbers will give the 3 hidden words from the actual answer")
print("\n4. all the letter of the word will be in lower case")
print("\n5. All sentences are made up of 5-7 word, it will be specified before each level ")

print("\nLET'S START!!!")
print("LEVEL-1: IT IS A SENTECE OF 5 WORDS ")
actual_sentence="taj mahal is situated in agra"
for x in range(1,4):
    x=int(input("\nenter the number of your choice:"))
    if x==1:
        print("taj mahal")
        continue
    if x==2:
        print("is")
        continue
    if x==3:
        print("situated")
        continue
    if x==4:
        print("in")
        continue
    if x==5:
        print("agra")
        continue
your_answer1=input("enter your answer for level 1:")
if actual_sentence==your_answer1:
    print("\n\nYOU WON LEVEL 1")
elif actual_sentence!=your_answer1:   
    print("you lost") 
        
    

print("LEVEL-2:IT IS A SENTENCE OF 6 WORDS")
actual_sentence="udaipur is a district in rajasthan"
for x in range(1,4):
    x=int(input("\nenter the number of your choice:"))
    if x==1:
        print("udaipur")
        continue
    if x==2:
        print("is")
        continue
    if x==3:
        print("a")
        continue
    if x==4:
        print("district")
        continue
    if x==5:
        print("in")
        continue
    if x==6:
        print("rajasthan")
your_answer1=input("enter your answer for level 1:")
if actual_sentence==your_answer1:
    print("\n\nYOU WON LEVEL 2")
print("LEVEL-3:IT IS A SENTENCE OF 7 WORDS")
actual_sentence="india pakistan border is known as radcliffe"
for x in range(1,4):
    x=int(input("\nenter the number of your choice:"))
    if x==1:
        print("taj mahal")
        continue
    if x==2:
        print("is")
        continue
    if x==3:
        print("situated")
        continue
    if x==4:
        print("in")
        continue
    if x==5:
        print("agra")
        continue
your_answer1=input("enter your answer for level 3:")
if actual_sentence==your_answer1:
    print("\n\nYOU WON LEVEL 3")
    