/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE126_Buffer_Overread__CWE170_char_loop_05.c
Label Definition File: CWE126_Buffer_Overread__CWE170.label.xml
Template File: point-flaw-05.tmpl.c
*/
/*
 * @description
 * CWE: 126 Buffer Overread
 * Sinks: loop
 *    GoodSink: Copy a string using a loop with explicit null termination
 *    BadSink : Copy a string using a loop without explicit null termination
 * Flow Variant: 05 Control flow: if(staticTrue) and if(staticFalse)
 *
 * */

#include "std_testcase.h"

#include <wchar.h>

/* The two variables below are not defined as "const", but are never
   assigned any other value, so a tool should be able to identify that
   reads of these will always return their initialized values. */
static int staticTrue = 1; /* true */
static int staticFalse = 0; /* false */

#ifndef OMITBAD

void CWE126_Buffer_Overread__CWE170_char_loop_05_bad()
{
    if(staticTrue)
    {
        {
            char src[150], dest[100];
            int i;
            /* Initialize src */
            memset(src, 'A', 149);
            src[149] = '\0';
            for(i=0; i < 99; i++)
            {
                dest[i] = src[i];
            }
            /* FLAW: do not explicitly null terminate dest after the loop */
            printLine(dest);
        }
    }
}

#endif /* OMITBAD */

#ifndef OMITGOOD

/* good1() uses if(staticFalse) instead of if(staticTrue) */
static void good1()
{
    if(staticFalse)
    {
        /* INCIDENTAL: CWE 561 Dead Code, the code below will never run */
        printLine("Benign, fixed string");
    }
    else
    {
        {
            char src[150], dest[100];
            int i;
            /* Initialize src */
            memset(src, 'A', 149);
            src[149] = '\0';
            for(i=0; i < 99; i++)
            {
                dest[i] = src[i];
            }
            dest[99] = '\0'; /* FIX: null terminate dest */
            printLine(dest);
        }
    }
}

/* good2() reverses the bodies in the if statement */
static void good2()
{
    if(staticTrue)
    {
        {
            char src[150], dest[100];
            int i;
            /* Initialize src */
            memset(src, 'A', 149);
            src[149] = '\0';
            for(i=0; i < 99; i++)
            {
                dest[i] = src[i];
            }
            dest[99] = '\0'; /* FIX: null terminate dest */
            printLine(dest);
        }
    }
}

void CWE126_Buffer_Overread__CWE170_char_loop_05_good()
{
    good1();
    good2();
}

#endif /* OMITGOOD */

/* Below is the main(). It is only used when building this testcase on
   its own for testing or for building a binary to use in testing binary
   analysis tools. It is not used when compiling all the testcases as one
   application, which is how source code analysis tools are tested. */

#ifdef INCLUDEMAIN

int main()
{
    /* seed randomness */
    srand( (unsigned)time(NULL) );
#ifndef OMITGOOD
    printLine("Calling good()...");
    CWE126_Buffer_Overread__CWE170_char_loop_05_good();
    printLine("Finished good()");
#endif /* OMITGOOD */
#ifndef OMITBAD
    printLine("Calling bad()...");
    CWE126_Buffer_Overread__CWE170_char_loop_05_bad();
    printLine("Finished bad()");
#endif /* OMITBAD */
    return 0;
}

#endif
