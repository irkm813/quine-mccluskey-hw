#Átalakít egy bináris számot decimális formába. A bináris számot string-ként adja vissza
def decimal_to_binary(decNum,bit):

    binNum = ""
    while decNum != 0:


        if decNum%2:

            binNum = "1"+binNum
            decNum = (decNum-1)/2

        else:

            binNum = "0"+binNum
            decNum = decNum/2

        if decNum < 0:
            print("decimal_to_binary function error")



    if len(binNum) != bit:
        additionalZeroes = bit - len(binNum)
        binNum = (additionalZeroes * "0") + binNum

    return binNum

#Összeolvaszt két minterm számot vagy sorozatot, ha szomszédosak.
def merge_bins(bin1,bin2):

    temporaryList = []

    if is_minterm_neighbor(bin1,bin2):
        if type(bin1) == str:
            return (bin1,bin2)

        else:
            for item in bin1:
                temporaryList.append(item)

            for item in bin2:
                temporaryList.append(item)

            return tuple(temporaryList)

#A függvény bemenete összevont mintermek, kimenete pedig ezeknek a különbségei.
def binary_difference(binNum):

    if type(binNum) == str:
        return [0]

    groupNumber = int(len(binNum))

    if groupNumber == 2:
        returnValue = []

        binNum = binary_to_decimal(binNum)
        returnValue.append(binNum[1]-binNum[0])

        return tuple(returnValue)

    else:
        binNum = binary_to_decimal(binNum)
        searchRange = max(binNum)
        powerOfTwo = []
        powNum = 0
        returnVaule = []

        while True:

            powerOfTwo.append(pow(2,powNum))
            powNum += 1
            if pow(2,powNum) > searchRange:
                break

        isFirstNum = True

        for i2 in range(1,len(binNum)):
            if (binNum[i2]-binNum[0]) in powerOfTwo:
                returnVaule.append(binNum[i2]-binNum[0])

        return tuple(returnVaule)

#Átalakít egy decimális számit bináris formába. A decimális számot int-ként adja vissza
def binary_to_decimal(binNum):


    binList = []
    binList += binNum[::-1]
    decNum = 0

    if type(binNum) == str:
        for item in range(len(binList)):
            decNum += int(binList[item])*(2**item)

        return decNum

    else:
        listOfNumbers = []

        for i1 in binNum:
            binList = []
            binList += i1[::-1]
            decNum = 0

            for item in range(len(binList)):
                decNum += int(binList[item]) * (2 ** item)

            listOfNumbers.append(decNum)
        return tuple(listOfNumbers)

#A kapott számokat átalakítja binárissá, majd csinál egy dictionary-t, amiben a különböző minterm súlyszámokhoz hozzárendeli ezeket az értékeket
def minterm_weight(numOfVars,numList):

    numbersAndWeights = {}

    #Leellenorzi, hogy jo adatok vannak-e megadva.
    largestMinterm = (2 ** numOfVars)

    for number in numList:
        if number >= largestMinterm or number < 0:
            print("A megadott mintermek nem megfelelőek")
            return 1

    # Átalakítja a mintermeket bináris formába és megszámolja a súlyszámukat. Ezeket hozzáadja egy dictionary-hez.
    for number in numList:

        binNum = decimal_to_binary(number,numOfVars)

        if len(binNum) != numOfVars:
            additionalZeroes = numOfVars-len(binNum)
            binNum = (additionalZeroes*"0")+binNum


        weight = binNum.count("1")

        try:
            numbersAndWeights[weight].append(binNum)
        except:
            templist = []
            templist.append(binNum)
            numbersAndWeights[weight] = templist

    return dict(sorted(numbersAndWeights.items()))

#Összehasonlít két bináris számot és visszaadja, hogy szomszédosak-e (Csak egy eltérő helyi érték van közöttük)
def is_binary_neighbor(bin1,bin2):

    bin1List,bin2List = [],[]
    bin1List += bin1
    bin2List += bin2
    if len(bin1List[0]) == 1:

        differenceCounter = 0

        for item in range(len(bin1List)):
            if bin1List[item] != bin2List[item]:
                differenceCounter += 1
        if differenceCounter == 1:
            return True

        return False

#Összehasonlít két mintermet, vagy mintermsorozatot és megállapítja, hogy összevonhatók-e
def is_minterm_neighbor(m1,m2):

    m1List, m2List = [], []
    m1List += m1
    m2List += m2

    # Ha két string a bemenet, ez az ág fut le
    if len(m1List[0]) == 1:
        return is_binary_neighbor(m1,m2)

    # Ha két touple a függvény bemenete, akkor ez az ág fut le
    else:

        for i1 in range(len(m1List)):
            tempNum1 = m1List[i1]
            tempNum2 = m2List[i1]
            if max(binary_to_decimal(m1List)) >= min(binary_to_decimal(m2List)):
                return False
            if not is_binary_neighbor(tempNum1,tempNum2):
                return False

        return True

#A kész teljes minterm listából kiszűri azokat az elemeket, amik nem voltak felhasználva további elemekhez
def unused_minterms(numberList):

    allMinterms = []
    usedMinterms = []

    for i1 in numberList:
        for i2 in i1:
            for i3 in i1[i2]:
                allMinterms.append(i3)

    allMinterms.reverse()

    for i1 in range(len(allMinterms)):
        for i2 in range(len(allMinterms)):
            if len(allMinterms[i1]) != len(allMinterms[i2]) and type(allMinterms[i1]) == type(allMinterms[i2]):

                if set(allMinterms[i2]).issubset(allMinterms[i1]):
                    usedMinterms.append(allMinterms[i2])

            if len(allMinterms[i1]) != len(allMinterms[i2]) and type(allMinterms[i2]) == str:
                if allMinterms[i2] in allMinterms[i1]:
                    usedMinterms.append(allMinterms[i2])

    newList = []

    for item in allMinterms:
        if item in usedMinterms:
            pass
        else:
            newList.append(item)

    newList.reverse()

    return newList

#Maga a csoda
def minterm_grouping(numOfVars,numList):

    numsByWeight = minterm_weight(numOfVars,numList)
    columns = [numsByWeight]
    tempDict = {}
    tempList = []
    tempCounter = 1
    usedMintermsList = []


    cont = True
    kere = 0

    groupNumber = []

    while cont:

        groupNumber = list(columns[-1].keys())

        if len(groupNumber) <= 1:
            cont = False
            break

        maxGroup = max(groupNumber)

        for i1 in range(len(groupNumber)):
            if groupNumber[i1] < maxGroup:
                mintermGroup1 = (columns[-1][groupNumber[i1]])
                mintermGroup2 = (columns[-1][groupNumber[i1+1]])

                for numbers1 in mintermGroup1:
                    for numbers2 in mintermGroup2:

                        if (merge_bins(numbers1,numbers2)) != None:
                            tempList.append(merge_bins(numbers1,numbers2))

                tempDict[tempCounter] = tempList
                tempCounter += 1
                tempList = []

        columns.append(tempDict)
        tempCounter = 1
        tempDict = {}


    return(columns)

#segédszámítások a prím implikáns táblázathoz
def vars_by_nums_finalization(numsByVars,varsByNums,allNums):

    varsByNumsFinal = {}
    allNumsWithRepetition = []
    absolutelynecVars = []
    unnecVars = []
    tempList = []
    variables = list(numsByVars.keys())

    for i in numsByVars:
        if type(numsByVars[i]) == str:
            allNumsWithRepetition.append(numsByVars[i])
        else:
            for i2 in numsByVars[i]:
                allNumsWithRepetition.append(i2)



    for i2 in variables:
        tempList = allNumsWithRepetition[:]

        for i3 in numsByVars[i2]:
            tempList.remove(i3)

        if all(item in tempList for item in allNums):
            unnecVars.append(i2)


    tempstring = ""
    cont = True



    while cont:

        for item in varsByNums:
            varsByNumsFinal[item] = ""

            if len(varsByNums[item]) > 1:
                for i2 in range(len(varsByNums[item])):
                    if varsByNums[item][i2] in unnecVars:
                        pass
                    else:
                        varsByNumsFinal[item] += varsByNums[item][i2]
            else:
                varsByNumsFinal[item] += varsByNums[item]

        try:
            print(list(varsByNumsFinal.values()).index(""))
        except:
            cont = False
            break

        print(unnecVars)
        unnecVars = variable_magic(varsByNumsFinal,varsByNums,unnecVars)
        print(unnecVars)


    return varsByNumsFinal

def variable_magic(varsByNumsFinal,varsByNums,unnecVars):

    tempList = []

    for i1 in varsByNumsFinal:
        if varsByNumsFinal[i1] == '':
            for l1 in varsByNums[i1]:
                tempList.append(l1)

    removableVariable = max(set(tempList), key=tempList.count)
    unnecVars.remove(removableVariable)

    return unnecVars

#A prím impikánsok a függvény bemenetei, a kimenete pedig a prím implikáns táblázat
def prime_implicant_table(primeImplicants):

    numbers = []
    differences = []
    numbersByVars = {}
    varsByNumbers = {}
    varsByNumbersFinal = {}
    letters = []
    tempCounter = 1
    largestGroup = 0
    abc = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n',
     14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}


    for i1 in primeImplicants:
        if type(i1) == str:
            if i1 not in numbers:
                numbers.append(i1)
        else:
            for i2 in i1:
                if i2 not in numbers:
                    numbers.append(i2)

    numbers = ((sorted(binary_to_decimal(numbers))))

    for item in range(len(numbers)):
        numbers[item] = decimal_to_binary(numbers[item],len(primeImplicants[-1][0]))

    for i1 in range(len(primeImplicants)):
        numbersByVars[abc[i1]] = primeImplicants[i1]

    for i1 in numbersByVars:
        if len(numbersByVars[i1]) > largestGroup:
            largestGroup = len(numbersByVars[i1])


    for i1 in numbersByVars:
        for i2 in numbers:
            if i2 in numbersByVars[i1]:
                try:
                    varsByNumbers[binary_to_decimal(i2)] += i1
                except:
                    varsByNumbers[binary_to_decimal(i2)] = i1

                if i1 not in letters:
                    letters.append(i1)

    varsByNumbers = dict(sorted(varsByNumbers.items()))

    varsByNumbers = vars_by_nums_finalization(numbersByVars,varsByNumbers,numbers)

    return letters, varsByNumbers

#A minterm összevonások táblázatának kiiratása
def firstTableData(mintermColumns):

    tempList = []
    rowNum = 0
    colNum = 0

    for i1 in mintermColumns:
        for i2 in i1:
            tempList.append(i2)
            for i3 in i1[i2]:
                tempList.append(i3)
    return tempList

#Eredmények kiiratását segítő függvények
def final_form(primeImplicant):


    whereToDelete = []
    upperABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
     "X", "Y", "Z"]

    if type(primeImplicant) != str:

        for i3 in binary_difference(primeImplicant):
            currentNumber = (decimal_to_binary(i3,len(primeImplicant[0])))
            whereToDelete.append(currentNumber.index('1'))


        mintermFinalForm = ""

        for i4 in range(len(primeImplicant[0])):
            if i4 not in whereToDelete:
                if primeImplicant[0][i4] == "0":
                    mintermFinalForm += "¬"+upperABC[i4]
                else:
                    mintermFinalForm += upperABC[i4]

                if i4 < len(primeImplicant[0])-1:
                    mintermFinalForm += "*"
    else:
        mintermFinalForm = ""

        for i4 in range(len(primeImplicant)):
            if i4 not in whereToDelete:
                if primeImplicant[i4] == "0":
                    mintermFinalForm += "¬" + upperABC[i4]
                else:
                    mintermFinalForm += upperABC[i4]

                if i4 < len(primeImplicant) - 1:
                    mintermFinalForm += "*"

    return mintermFinalForm

def final_outcome(primeImplicants):

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

    vegeredmeny = "Prim implikansok:\n"

    for i1 in range(len(primeImplicants)):
        vegeredmeny += str(abc[i1])+": "
        vegeredmeny += str(binary_to_decimal(primeImplicants[i1]))+" "
        vegeredmeny += str(binary_difference(primeImplicants[i1]))+"\n"

    vegeredmeny += "\n"
    vegeredmeny += "Alak az osszes prim implikans alapjan:\n"

    for i2 in range(len(primeImplicants)):
        vegeredmeny += final_form(primeImplicants[i2])
        if i2 < len(primeImplicants)-1:
            vegeredmeny += " + "

    vegeredmeny += "\n\n"
    vegeredmeny += "Legegyszerubb alak:\n"

    olk,allPrimeImps = prime_implicant_table(primeImplicants)

    finalImplicants = []

    for i3 in allPrimeImps:
        if len(allPrimeImps[i3])==1 and allPrimeImps[i3] not in finalImplicants:
            finalImplicants.append(allPrimeImps[i3])

    finalImplicants = sorted(finalImplicants)

    for i5 in range(len(finalImplicants)):
        vegeredmeny += finalImplicants[i5]
        if i5 < len(finalImplicants)-1:
            vegeredmeny += "+"

    vegeredmeny += "\n\n"

    for i4 in range(len(primeImplicants)):
        if abc[i4] in finalImplicants:
            vegeredmeny += final_form(primeImplicants[i4])
            if i4 < len(primeImplicants):
                vegeredmeny += " + "

    if vegeredmeny[-1] == " ":
        vegeredmeny = vegeredmeny[0:-3]

    return vegeredmeny


if __name__ == "__main__":

    variableInput = 5
    mintermInput2 = [0,2,3,4]
    mintermInput = (0,1,4,5,9,10,13,14,16,17,20,21,25,26,27,29)
    ka = ['a', 'b', 'c']
    ke = {0: 'ab', 2: 'ac', 4: 'b', 3: 'c'}

    mintermColumns = minterm_grouping(variableInput, mintermInput)


    primeImplicants = unused_minterms(mintermColumns)

    primeImpTableSide, primeImpTable = prime_implicant_table(primeImplicants)

    print("-------------")


