import sys
import re

inversions = 0

def merge_sort( el ):
    global inversions

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

    # get iterators for each sub list
    iterA = iter( sortedA )
    iterB = iter( sortedB )

    # get the first items
    itemA = next( iterA )
    itemB = next( iterB )

    # track inversions by seeding...
    itemsRemainingInA = lenA

    # the sorted list must be as long as the original
    for i in range( len( el ) ):
        if ( not doneA and itemA < itemB ) or doneB:
            sorted_el.append( itemA )
            itemsRemainingInA -= 1
            try:
                itemA = next( iterA )
            except StopIteration:
                doneA = 1
        else:
            sorted_el.append( itemB )
            inversions += itemsRemainingInA
            try:
                itemB = next( iterB )
            except StopIteration:
                doneB = 1

    return sorted_el

def main():
    global inversions
    inversions = 0
    genTestFile = False
    genFileName = ''
    elements = []

    if len( sys.argv ) > 1:
        if re.match( '-h', sys.argv[ 1 ] ):
            print( 'Usage -- with or without commas:' )
            print( 'my_prompt>  python3 merge_sort.py 1 6 3 2 4 5' )
            print( 'my_prompt>  python3 merge_sort.py 1, 6, 3, 2, 4, 5' )
            print( 'The next example writes the input values from the command line to a file, one per line.' )
            print( 'my_prompt>  python3 merge_sort.py -g outputfile.txt 1, 6, 3, 2, 4, 5' )
            print( 'The next examples expects input values, one per line, in the associated file' )
            print( 'my_prompt>  python3 merge_sort.py -f inputfile.txt' )
            return

        # generates output files for test
        if re.match( '-g', sys.argv[ 1 ] ):
            genTestFile = True
            genFileName = sys.argv[ 2 ]
            del sys.argv[ 1:3 ]

        # gets values from file
        if re.match( '-f', sys.argv[ 1 ] ):
            inputFileName = sys.argv[ 2 ]
            with open( inputFileName, 'rt' ) as fin:
                while True:
                    line = fin.readline()
                    if not line:
                        break
                    elements.append( int( line ) )
        else:
            # getting values from command line
            elements = [ int( re.sub( ',', '', x ) ) for x in sys.argv[ 1: ] ]

        # call the sort function
        sorted_elements = merge_sort( elements )

        print( elements )
        print( sorted_elements )
        print( 'number of inversions:  {:,d}'.format( inversions ) )

        if genTestFile:
            with open( genFileName, 'wt' ) as fout:
                for num in elements:
                    print( num, file = fout )

        return

    # if no command line arguments
    inversions = 0
    elementsA = [ 87, 16, 2, 0, 12, 25, 26, 27, 63, 75, 28, 50, 2, 5, 41, 39 ]
    sortedA = merge_sort( elementsA )

    print( elementsA )
    print( sortedA )
    print( 'number of inversions:  {:d}'.format( inversions ) )

    inversions = 0
    elementsB = [ 98, 97, 96, 90, 73, 72, 71, 70, 43, 42, 41, 40, 25, 24, 23, 22 ]
    sortedB = merge_sort( elementsB )

    print( elementsB )
    print( sortedB )
    print( 'number of inversions:  {:d}'.format( inversions ) )

    inversions = 0
    elementsC = [ 5, 4, 3, 2, 1 ]
    sortedC = merge_sort( elementsC )

    print( elementsC )
    print( sortedC )
    print( 'number of inversions:  {:d}'.format( inversions ) )

    inversions = 0
    elementsD = [ 23, 27, 82, 69, 1, 4, 2, 100, 1023, 1000, 83, 41, 14, 19, 37, 18, 8 ]
    sortedD = merge_sort( elementsD )

    print( elementsD )
    print( sortedD )
    print( 'number of inversions:  {:d}'.format( inversions ) )

if __name__ == '__main__':
    main()
