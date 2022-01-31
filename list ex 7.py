#palindrome
s=input("Enter a string:")
if s==s[::-1]:
  print(s,"is a palindrome.")
else:
  print(s,"is not a palindrome.")

#searching substring
s=input("Enter a string:")
b=int(input("Enter starting index for substring:"))
e=int(input("Enter ending index for substring:"))
print(s[b:e+1],"is the substring.")

#anagram
def anagram(s1,s2):
    str1=sorted(s1)
    str2=sorted(s2)
    if (str1==str2):
        print("Anagram")
    else:
        print("Not an anagram")
if __name__=="__main__":
    s1=input("Enter the 1st string: ")
    s2=input("Enter the 2nd string: ")
anagram(s1,s2)

#number of substrings
def substring(str1):
    sub_list=[]
    count=0
    for i in range(len(str1)):
        for j in range(i+1,len(str1)+1):
          sub_str=str1[i:j]
          sub_list.append(sub_str)
          count+=1
    print("Total number of substrings = ",count)
    print("Substrings = ",sub_list)
if __name__=="__main__":
    str1=input("Enter the string: ")
substring(str1)