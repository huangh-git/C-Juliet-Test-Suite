/* TEMPLATE GENERATED TESTCASE FILE
Filename: CWE126_Buffer_Overread__CWE129_fscanf_67a.c
Label Definition File: CWE126_Buffer_Overread__CWE129.label.xml
Template File: sources-sinks-67a.tmpl.c
*/
/*
 * @description
 * CWE: 126 Buffer Overread
 * BadSource: fscanf Read data from the console using fscanf()
 * GoodSource: Larger than zero but less than 10
 * Sinks:
 *    GoodSink: Ensure the array index is valid
 *    BadSink : Improperly check the array index by not checking the upper bound
 * Flow Variant: 67 Data flow: data passed in a struct from one function to another in different source files
 *
 * */

#include "std_testcase.h"

typedef struct _CWE126_Buffer_Overread__CWE129_fscanf_67_structType
{
    int structFirst;
} CWE126_Buffer_Overread__CWE129_fscanf_67_structType;

#ifndef OMITBAD

/* bad function declaration */
void CWE126_Buffer_Overread__CWE129_fscanf_67b_badSink(CWE126_Buffer_Overread__CWE129_fscanf_67_structType myStruct);

void CWE126_Buffer_Overread__CWE129_fscanf_67_bad()
{
    int data;
    CWE126_Buffer_Overread__CWE129_fscanf_67_structType myStruct;
    /* Initialize data */
    data = -1;
    /* POTENTIAL FLAW: Read data from the console using fscanf() */
    fscanf(stdin, "%d", &data);
    myStruct.structFirst = data;
    CWE126_Buffer_Overread__CWE129_fscanf_67b_badSink(myStruct);
}

#endif /* OMITBAD */

#ifndef OMITGOOD

/* goodG2B uses the GoodSource with the BadSink */
void CWE126_Buffer_Overread__CWE129_fscanf_67b_goodG2BSink(CWE126_Buffer_Overread__CWE129_fscanf_67_structType myStruct);

static void goodG2B()
{
    int data;
    CWE126_Buffer_Overread__CWE129_fscanf_67_structType myStruct;
    /* Initialize data */
    data = -1;
    /* FIX: Use a value greater than 0, but less than 10 to avoid attempting to
     * access an index of the array in the sink that is out-of-bounds */
    data = 7;
    myStruct.structFirst = data;
    CWE126_Buffer_Overread__CWE129_fscanf_67b_goodG2BSink(myStruct);
}

/* goodB2G uses the BadSource with the GoodSink */
void CWE126_Buffer_Overread__CWE129_fscanf_67b_goodB2GSink(CWE126_Buffer_Overread__CWE129_fscanf_67_structType myStruct);

static void goodB2G()
{
    int data;
    CWE126_Buffer_Overread__CWE129_fscanf_67_structType myStruct;
    /* Initialize data */
    data = -1;
    /* POTENTIAL FLAW: Read data from the console using fscanf() */
    fscanf(stdin, "%d", &data);
    myStruct.structFirst = data;
    CWE126_Buffer_Overread__CWE129_fscanf_67b_goodB2GSink(myStruct);
}

void CWE126_Buffer_Overread__CWE129_fscanf_67_good()
{
    goodG2B();
    goodB2G();
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
    CWE126_Buffer_Overread__CWE129_fscanf_67_good();
    printLine("Finished good()");
#endif /* OMITGOOD */
#ifndef OMITBAD
    printLine("Calling bad()...");
    CWE126_Buffer_Overread__CWE129_fscanf_67_bad();
    printLine("Finished bad()");
#endif /* OMITBAD */
    return 0;
}

#endif
