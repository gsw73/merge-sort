def merge_sort( el ):

    # break array into two pieces
    lenA = len( el ) // 2
    lenB = len( el ) // 2 + len( el ) % 2
    unsortedA = el[ :lenA ]
    unsortedB = el[ lenA: ]

    # sort list A
    if lenA == 1:
        sortedA = list( unsortedA )
    else:
        sortedA = merge_sort( unsortedA )

    # sort list B
    if lenB == 1:
        sortedB = list( unsortedB )
    else:
        sortedB = merge_sort( unsortedB )

    # a list for the final sorted elements
    sorted_el = []
    doneA = 0
    doneB = 0
    usedA = 0
    usedB = 0

    # get iterators for each sub list
    iterA = iter( sortedA )
    iterB = iter( sortedB )

    # get the first items
    itemA = next( iterA )
    itemB = next( iterB )

    # the sorted list must be as long as the original
    for i in range( len( el ) ):
        if not doneA and not doneB:
            if itemA < itemB:
                sorted_el.append( itemA )
                usedA += 1
                doneA = usedA == lenA
                if not doneA:
                    itemA = next( iterA )

            else:
                sorted_el.append( itemB )
                usedB += 1
                doneB = usedB == lenB
                if not doneB:
                    itemB = next( iterB )

        elif doneA and not doneB:
            sorted_el.append( itemB )
            usedB += 1
            doneB = usedB == lenB
            if not doneB:
                itemB = next( iterB )

        elif not doneA and doneB:
            sorted_el.append( itemA )
            usedA += 1
            doneA = usedA == lenA
            if not doneA:
                itemA = next( iterA )

    return sorted_el

def main():
    elementsA = [ 87, 16, 2, 0, 12, 25, 26, 27, 63, 75, 28, 50, 2, 5, 41, 39 ]
    sortedA = merge_sort( elementsA )

    print( elementsA )
    print( sortedA )

    elementsB = [ 98, 97, 96, 90, 73, 72, 71, 70, 43, 42, 41, 40, 25, 24, 23, 22 ]
    sortedB = merge_sort( elementsB )

    print( elementsB )
    print( sortedB )

    elementsC = [ 5, 4, 3, 2, 1 ]
    sortedC = merge_sort( elementsC )

    print( elementsC )
    print( sortedC )

    elementsD = [ 23, 27, 82, 69, 1, 4, 2, 100, 1023, 1000, 83, 41, 14, 19, 37, 18, 8 ]
    sortedD = merge_sort( elementsD )

    print( elementsD )
    print( sortedD )

if __name__ == '__main__':
    main()
