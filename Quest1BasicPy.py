# Basic Python Quest
# When returning lists of values, order is not important unless specified

__STUDENT_ID__  = "47555408"     # replace with your 8 digit student id
__CODING_NAME__ = "tkyaagba"        # replace with your coding name -

#COMPLETE / PASSED
def isSorted(list):
    """ return boolean depending on if list sorted
    >>> isSorted([2,4,7,7,99,122]) -> True
    >>> isSorted(['a','b','c'])  -> True
    >>> isSorted(['a','z','b','c'])  -> False
    """
    return sorted(list) == list


#COMPLETE / PASSED
def isSortedAndUnique(list):
    """ return boolean depending on if list sorted
    >>> isSortedAndUnique([2,4,7,7,99,122]) -> False
    >>> isSortedAndUnique(['a','b','c'])  -> True
    >>> isSortedAndUnique(['a','z','b','b','c'])  -> False
    """
    return isSorted(list) and hasUniqueValues(list)

#COMPLETE / PASSED
def hasUniqueValues(list):
    """ return boolean depending on if list has unique values
    >>> hasUniqueValues([2,4,7,7,99,122]) -> False
    >>> hasUniqueValues(['a','b','c'])  -> True
    >>> hasUniqueValues(['a','z','b','b','c'])  -> False
    """
    return len(set(list)) == len (list)

#COMPLETE / PASSED
def genSortedArrayUniqueValues(my_list):
    """ return sorted version of list without duplicates
    >>> genSortedArrayUniqueValues([2,4,7,7,122,99]) -> [2,4,7,99,122]
    >>> genSortedArrayUniqueValues(['a','b','z','c', 'a'])  -> ['a','b','c','z']
    """
    # remove duplicate values, convert set to list, then sort and return
    return sorted(list(set(my_list)))

#COMPLETE / PASSED
def listToMapTwoByTwo(list):
    """ return a map based on the order of list elements.
    >>> listToMapTwoByTwo(['foo','bar'])     ->  {"foo":"bar"}
    >>> listToMapTwoByTwo(['a',2, 3,'foo'])  ->  {"a":2,3:'foo'}
    >>> listToMapTwoByTwo([])  -> {}
    """
    #create list of keys all items with an even index
    keys = [item for item in list if (list.index(item) % 2 == 0)]
    #create list of values --> all items with an odd index
    values = [item for item in list if (list.index(item) % 2 == 1)]
    return dict(zip(keys, values))

#COMPLETE / PASSED
def wordsInStringToDictWordCount(s):
    """ return a dict of words in string and count
    >>> wordsInStringToDictWordCount('foo bar   bar') -> {'foo':1, 'bar':2}
    >>> wordsInStringToDictWordCount('') -> {}
    """
    #create list of all items
    stringList = s.split()
    uniqueList = list(set(stringList))
    frequencyList = []
    
    #get list of item frequencies
    for item in uniqueList:
        counter = 0
        for word in stringList:
            if word == item:
                counter += 1
        frequencyList.append(counter)
        
    return dict(zip(uniqueList,frequencyList))

#COMPLETE / PASSED
def reverseWordsInString(string):
    """ return a string with words reversed with one space separators
    >>> reverseWordsInString('foo bar bar baz') -> 'baz bar bar foo'
    """
    #split string by spaces, reverse the resulting list, recombine list items into single string
    stringList = string.split(' ')
    reversedList = stringList[::-1]
    reversedString = ' '.join(reversedList)
    return reversedString


#COMPLETE / FAILED 1-OF-3: CODE FAILS TEST #2: assert [8,2,4,6] == [2,4,6,8]
#INSTRUCTIONS STATE THAT ORDER IS IRRELEVENT UNLESS SPECIFIED.
#INTENDED BEHAVIOR. WILL NOT FIX. MARKING AS CLOSED.
def genListOfOverlaps(list1, list2):
    """ return list of values appearing in both lists
    >>> genListOfOverlaps([2,4,6,8],[6,2,2,9,7]) -> [2,6]
    >>> genListOfOverlaps([2,4,6,8],[2,4,6,8]) -> [2,4,6,8]
    >>> genListOfOverlaps([2,4,6,8],[1,1,9,7]) -> []
    """
    return list(set(list1) & set(list2))

#COMPLETE / PASSED
def removeDupsNoSet(list):
    """ remove duplicates in the list without using Python Set
    >>> removeDupsNoSet([1,1,2,2,5,6]) -> [1,2,5,6]
    """
    dedupedList = list
    index = 0
    counter = index + 1
    finished = False
    
    if len(list) < 2:
        finished = True
        
    while not finished:
        #loop to remove duplicates by comparing dedupedList[index] to dedupedList[counter]
        while counter < len(dedupedList):
            if dedupedList[index] == dedupedList[counter]:
                del(dedupedList[counter:counter +1])
            counter += 1
        #increment index once end of list is reached then reset counter
        index += 1
        counter = index + 1
        
        #exit outer loop once last item in list is reached.
        if index == len(dedupedList) - 1:
            finished = True
    return dedupedList

#COMPLETE / PASSED
def removeDupsUseSet(mylist):
    """ remove duplicates in the list  using Python Set
    >>> removeDupsUseSet([1,1,2,2,5,6]) -> [1,2,5,6]
    """
    return list(set(mylist))

if __name__ == '__main__':
    #write your own test code here
    print ('ready to go')