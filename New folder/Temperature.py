temp=input("Input you temperature: ")
temp=temp.lower()
print(temp)  # check if numbers did not lowered
templetter=temp.find("f")
templetter=temp.find("c")

letter=temp[templetter]

if letter == "f":
    temp = temp.replace('f', '')
    temp=int(temp)
    C=((5*temp)-160)/9  #temp in Celsius

    print(C)
else:
    temp = temp.replace('c', '')
    temp = int(temp)
    F = (9*temp+(32*5)) / 5  # temp in Celsius

    print(F)
