
str1 = "abcdefghijklmnopqrstuvwxyz" 
locationE = str1.find("e") 
print locationE 
 
str2 = "abcdfghijklmnopqrstuvwxyz" 
noLocationE = str2.find("e") 
print noLocationE

str1 = "abcdefghijklmnopqrstuvwxyz"
locationF = str1.find("f")
subString = str1[locationF:len(str1)]

#print subString


#print str1[locationF:len(str1) - 1]
#print str1[locationF + 1:len(str1)]
#print str1[locationF:locationF + 5]
#print str1[locationF:str1.find("h")]

## Advanced Exercise Example #1
## Find the answer -- "here"
str2 = "The answer you are looking for is: here"
strToFind = "is: "
findTheAnswer = str2.find(strToFind)

theAnswer = str2[findTheAnswer:len(str2)]
#print theAnswer

theRealAnswer = str2[findTheAnswer + len(strToFind):len(str2)]
#print theRealAnswer

## Advanced Exercise Example #2
## We want to find "defghijklmnopqrstuvwxyz"
str3 = "AabcAdefghijklmnopqrstuvwxyz"
letterToFind = "A"
firstA = str3.find(letterToFind)

#print str3[firstA + len(letterToFind):len(str3)]

secondA = str3.find(letterToFind, firstA + 1)
#print str3[secondA + len(letterToFind):len(str3)]

## Additional Exercises
exerciseOne = "BabcBdefBghijklmnopqrstuvwxyz"
exerciseOneLetter = "A"

## Can you write python code to parse out the string "defBghijklmnopqrstuvwxyz"?


## Can you write python code to parse out the string "ghijklmnopqrstuvwxyz"?


## Extra Challenge: Can you write python code to parse out the string "def"?


## HTML Exercise
exerciseTwo = "<body>This is body text</body>"
exerciseTwoParseFront = "<body>"
exerciseTwoParseBack = "</body>"

## Can you write python code to parse out the string "This is body text"?

