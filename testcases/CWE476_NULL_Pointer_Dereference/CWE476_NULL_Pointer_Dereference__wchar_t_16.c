/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE476_NULL_Pointer_Dereference__wchar_t_16.c
Label Definition File: CWE476_NULL_Pointer_Dereference.label.xml
Template File: sources-sinks-16.tmpl.c
*/
/*
 * @description
 * CWE: 476 NULL Pointer Dereference
 * BadSource:  Set data to NULL
 * GoodSource: Initialize data
 * Sinks:
 *    GoodSink: Check for NULL before attempting to print data
 *    BadSink : Print data
 * Flow Variant: 16 Control flow: while(1)
 *
 * */

#include "std_testcase.h"

#include <wchar.h>

#ifndef OMITBAD

void CWE476_NULL_Pointer_Dereference__wchar_t_16_bad()
{
    wchar_t * data;
    while(1)
    {
        /* POTENTIAL FLAW: Set data to NULL */
        data = NULL;
        break;
    }
    while(1)
    {
        /* POTENTIAL FLAW: Attempt to use data, which may be NULL */
        /* printWLine() checks for NULL, so we cannot use it here */
        printWcharLine(data[0]);
        break;
    }
}

#endif /* OMITBAD */

#ifndef OMITGOOD

/* goodB2G() - use badsource and goodsink by changing the sinks in the second while statement */
static void goodB2G()
{
    wchar_t * data;
    while(1)
    {
        /* POTENTIAL FLAW: Set data to NULL */
        data = NULL;
        break;
    }
    while(1)
    {
        /* FIX: Check for NULL before attempting to print data */
        if (data != NULL)
        {
            /* printWLine() checks for NULL, so we cannot use it here */
            printWcharLine(data[0]);
        }
        else
        {
            printLine("data is NULL");
        }
        break;
    }
}

/* goodG2B() - use goodsource and badsink by changing the sources in the first while statement */
static void goodG2B()
{
    wchar_t * data;
    while(1)
    {
        /* FIX: Initialize data */
        data = L"Good";
        break;
    }
    while(1)
    {
        /* POTENTIAL FLAW: Attempt to use data, which may be NULL */
        /* printWLine() checks for NULL, so we cannot use it here */
        printWcharLine(data[0]);
        break;
    }
}

void CWE476_NULL_Pointer_Dereference__wchar_t_16_good()
{
    goodB2G();
    goodG2B();
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
    CWE476_NULL_Pointer_Dereference__wchar_t_16_good();
    printLine("Finished good()");
#endif /* OMITGOOD */
#ifndef OMITBAD
    printLine("Calling bad()...");
    CWE476_NULL_Pointer_Dereference__wchar_t_16_bad();
    printLine("Finished bad()");
#endif /* OMITBAD */
    return 0;
}

#endif
