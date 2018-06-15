# Testfile for Quest1BasicPy.py
import pytest
import Quest1BasicPy 


# TESTS   

def test_isSorted1():
    assert Quest1BasicPy.isSorted([2, 4, 7, 7, 99, 122]) == True


def test_isSorted2():
    assert Quest1BasicPy.isSorted(['a', 'b', 'c']) == True


def test_isSorted3():
    assert Quest1BasicPy.isSorted(['a', 'z', 'b', 'c']) == False


def test_isSortedAndUnique1():
    assert Quest1BasicPy.isSortedAndUnique([2, 4, 7, 7, 99, 122]) == False


def test_isSortedAndUnique2():
    assert Quest1BasicPy.isSortedAndUnique(['a', 'b', 'c']) == True


def test_isSortedAndUnique3():
    assert Quest1BasicPy.isSortedAndUnique(['a', 'z', 'b', 'b', 'c']) == False


def test_hasUniqueValues1():
    assert Quest1BasicPy.hasUniqueValues([2, 4, 7, 7, 99, 122]) == False


def test_hasUniqueValues2():
    assert Quest1BasicPy.hasUniqueValues(['a', 'b', 'c']) == True


def test_hasUniqueValues3():
    assert Quest1BasicPy.hasUniqueValues(['a', 'z', 'b', 'b', 'c']) == False

def test_genSortedArrayUniqueValues1():
    assert Quest1BasicPy.genSortedArrayUniqueValues(['a','b','z','c', 'a']) ==  ['a','b','c','z']

def test_genSortedArrayUniqueValues2():
    assert Quest1BasicPy.genSortedArrayUniqueValues([2,4,7,7,122,99]) ==  [2,4,7,99,122]

def test_listToMapTwoByTwo1():
    assert Quest1BasicPy.listToMapTwoByTwo(['foo', 'bar']) == {'foo': 'bar'}


def test_listToMapTwoByTwo2():
    assert Quest1BasicPy.listToMapTwoByTwo(['a', 2, 3, 'foo']) == {'a': 2, 3: 'foo'}


def test_listToMapTwoByTwo3():
    assert Quest1BasicPy.listToMapTwoByTwo([]) == {}


def test_wordsInStringToDictWordCount1():
    assert Quest1BasicPy.wordsInStringToDictWordCount('foo bar   bar') == {'foo': 1, 'bar': 2}


def test_wordsInStringToDictWordCount2():
    assert Quest1BasicPy.wordsInStringToDictWordCount('') == {}


def test_reverseWordsInString1():
    assert Quest1BasicPy.reverseWordsInString('foo bar bar baz') == 'baz bar bar foo'


def test_genListOfOverlaps1():
    assert Quest1BasicPy.genListOfOverlaps([2, 4, 6, 8], [6, 2, 2, 9, 7]) == [2, 6]


def test_genListOfOverlaps2():
    assert Quest1BasicPy.genListOfOverlaps([2, 4, 6, 8], [2, 4, 6, 8]) == [2, 4, 6, 8]


def test_genListOfOverlaps3():
    assert Quest1BasicPy.genListOfOverlaps([2, 4, 6, 8], [1, 1, 9, 7]) == []


def test_removeDupsNoSet1():
    assert Quest1BasicPy.removeDupsNoSet([1, 1, 2, 2, 5, 6]) == [1, 2, 5, 6]


def test_removeDupsUseSet1():
    assert Quest1BasicPy.removeDupsUseSet([1, 1, 2, 2, 5, 6]) == [1, 2, 5, 6]



if __name__ == '__main__':
    print("running main ")
    pytest.main()
    

