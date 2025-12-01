def isAnagram(s1,s2):

    if(len(s1)!=len(s2)):
        return False
    
    s1=s1.lower()
    s2=s2.lower()

    charCount={}

    for ch in s1:
        charCount[ch]=charCount.get(ch,0)+1
    for ch in s2:
        charCount[ch]=charCount.get(ch,0)-1

    for value in charCount.values():
        if value!=0:
            return False
    return True







if __name__=="__main__":
    s1=input("enter s1: ")
    s2=input("enter s2: ")
    if(isAnagram(s1,s2)):
        print("True")
    else:
        print("False")