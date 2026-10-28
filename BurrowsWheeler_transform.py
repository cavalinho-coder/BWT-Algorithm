startString = input("write something, it will be then processed with the BWT algorithm\nwrite here: ")    #example: banana

print(f"\nyour string: {startString}")

startString += "$"  #the algorithm starts adding a dollar at the end of the string      example: banana$

print(f"\nwe start by adding the dollar at the end of your sentence: {startString}\n")

stringSteps = []    #we initialize the list were all the steps the string takes will be recorded

stringSteps.append(startString)     #taking record of the first step

print("then we start taking the first char and putting it at the end of your string\ntill it's all behind the dollar:\n")

while startString[0] != "$":
    firstChar = startString[0]  #save the first char of the startString: b

    startString = startString[1:]   #remove it from the startString: anana$

    startString += firstChar    #add the char we saved at the end of the string:  anana$b

    stringSteps.append(startString)     #recording the step in the list

for i in range(len(startString)):
    print(f"{i+1} {stringSteps[i]}")

sortedFlag = False

for i in range (len(stringSteps)):
    for j in range (len(stringSteps)):
        if ord(stringSteps[i][0].lower()) < ord(stringSteps[j][0].lower()):
            stringSteps[i] , stringSteps[j] = stringSteps[j] , stringSteps[i]