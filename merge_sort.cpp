#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>

using namespace std;

// scrambled array as input; returns sorted array
unsigned int *merge_sort( unsigned int *el, unsigned int numberOfElements ) {
    
    // pointers come back from recursion in sorted order; new array created
    // at point of sorting
    unsigned int *sortedA_p;
    unsigned int *sortedB_p;

    // sorted array goes here
    unsigned int *sorted_p = new unsigned int [ numberOfElements ];

    // two halves; 2nd half gets extra element if total len not even
    unsigned int lenA = numberOfElements / 2;
    unsigned int lenB = numberOfElements / 2 + numberOfElements % 2;

    // use original array for each half
    unsigned int startA_offset = 0;
    unsigned int startB_offset = lenA;

    unsigned int *startA_p = el;
    unsigned int *startB_p = el + startB_offset;

    if ( lenA == 1 ) {
        sortedA_p = new unsigned int [ 1 ];
        *sortedA_p = *startA_p;
    } else {
        sortedA_p = merge_sort( startA_p, lenA );
    }

    if ( lenB == 1 ) {
        sortedB_p = new unsigned int [ 1 ];
        *sortedB_p = *startB_p;
    } else {
        sortedB_p = merge_sort( startB_p, lenB );
    }

    // merge
    unsigned int *tmpA_p = sortedA_p;
    unsigned int *tmpB_p = sortedB_p;
    unsigned int tmpAUsed = 0;
    unsigned int tmpBUsed = 0;
    unsigned int doneA = 0;
    unsigned int doneB = 0;

    for ( unsigned int i = 0; i < numberOfElements; i++ ) {
        if ( ( !doneA && *tmpA_p < *tmpB_p ) || doneB ) {
            sorted_p[ i ] = *tmpA_p++;
            tmpAUsed++;
            if ( tmpAUsed == lenA ) doneA = 1;
        } else {
            sorted_p[ i ] = *tmpB_p++;
            tmpBUsed++;
            if ( tmpBUsed == lenB ) doneB = 1;
        }
    }

    delete [] sortedA_p;
    delete [] sortedB_p;
    
    return( sorted_p );
}

void arrayPrint( unsigned int* array_p, unsigned int len ) {
    for ( unsigned int i = 0; i < len; i++ ) {
        printf( "%d ", array_p[ i ] );
    }

    printf( "\n" );
    return;
}

int main() {
    unsigned int elements[ 16 ] = { 87, 16, 2, 0, 12, 25, 26, 27, 63, 75, 28, 50, 2, 5, 41, 39 };
    unsigned int *sorted_p = merge_sort( elements, 16 );

    arrayPrint( elements, 16 );
    arrayPrint( sorted_p, 16 );
    
    unsigned int elementsB[ 16 ] = { 98, 97, 96, 90, 73, 72, 71, 70, 43, 42, 41, 40, 25, 24, 23, 22 };
    sorted_p = merge_sort( elementsB, 16 );

    arrayPrint( elementsB, 16 );
    arrayPrint( sorted_p, 16 );
    
    unsigned int elementsC[ 5 ] = { 5, 4, 3, 2, 1 };
    sorted_p = merge_sort( elementsC, 5 );
    
    arrayPrint( elementsC, 5 );
    arrayPrint( sorted_p, 5 );

    unsigned int elementsD[] = { 23, 27, 82, 69, 1, 4, 2, 100, 1023, 1000, 83, 41, 14, 19, 37, 18, 8 };
    unsigned int elementsInD = sizeof( elementsD ) / sizeof( unsigned int );
    sorted_p = merge_sort( elementsD, elementsInD );
    arrayPrint( elementsD, elementsInD );
    arrayPrint( sorted_p, elementsInD );
    
    return( 0 );
}








