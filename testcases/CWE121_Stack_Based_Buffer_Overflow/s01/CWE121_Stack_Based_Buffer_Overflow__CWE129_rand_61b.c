/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_61b.c
Label Definition File: CWE121_Stack_Based_Buffer_Overflow__CWE129.label.xml
Template File: sources-sinks-61b.tmpl.c
*/
/*
 * @description
 * CWE: 121 Stack Based Buffer Overflow
 * BadSource: rand Set data to result of rand(), which may be zero
 * GoodSource: Larger than zero but less than 10
 * Sinks:
 *    GoodSink: Ensure the array index is valid
 *    BadSink : Improperly check the array index by not checking the upper bound
 * Flow Variant: 61 Data flow: data returned from one function to another in different source files
 *
 * */

#include "std_testcase.h"

#ifndef OMITBAD

int CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_61b_badSource(int data)
{
    /* POTENTIAL FLAW: Set data to a random value */
    data = 10;
    return data;
}

#endif /* OMITBAD */

#ifndef OMITGOOD

/* goodG2B() uses the GoodSource with the BadSink */
int CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_61b_goodG2BSource(int data)
{
    /* FIX: Use a value greater than 0, but less than 10 to avoid attempting to
     * access an index of the array in the sink that is out-of-bounds */
    data = 7;
    return data;
}

/* goodB2G() uses the BadSource with the GoodSink */
int CWE121_Stack_Based_Buffer_Overflow__CWE129_rand_61b_goodB2GSource(int data)
{
    /* POTENTIAL FLAW: Set data to a random value */
    data = 10;
    return data;
}

#endif /* OMITGOOD */
