str1 = "how are you"
num = 23
str2 = "Hello!"

#part1

    #print the thrird element in str
print(str1[2])

    #add "!" to the end of str
str1=str1+"!"
print(str1)

    #set str to eqaul a concatination of str2 and str with a space in between
str1=str1+"\n"+str2
print(str1)

    #print str

    #print the length of str
print(len(str1))

#part 2

    #cast num to a string
num=str(num)

    #set str2 to equal the concat of str and num
str2=str1+num
    #print num
print(num)
    #set num eqaul to itself plus "1"
num=num+"1"
print(num)
    #cast num to an integer
num=int(num)
    #print num
print(num)
    #add 1 to num
num=num+1
    #print num
print(num)