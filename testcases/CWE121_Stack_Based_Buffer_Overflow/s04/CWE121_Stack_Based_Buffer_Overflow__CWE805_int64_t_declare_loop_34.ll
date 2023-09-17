; ModuleID = 'CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34.c'
source_filename = "CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34.c"
target datalayout = "e-m:e-p:32:32-p10:8:8-p20:8:8-p160:32:32-i64:64-n32:64-S128-ni:1:10:20:160"
target triple = "wasm32-unknown-wasi"

%union.CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_unionType = type { i64* }

@.str = private unnamed_addr constant [18 x i8] c"Calling good()...\00", align 1
@.str.1 = private unnamed_addr constant [16 x i8] c"Finished good()\00", align 1
@.str.2 = private unnamed_addr constant [17 x i8] c"Calling bad()...\00", align 1
@.str.3 = private unnamed_addr constant [15 x i8] c"Finished bad()\00", align 1
@llvm.used = appending global [1 x i8*] [i8* bitcast (i32 ()* @__main_void to i8*)], section "llvm.metadata"

@__main_void = alias i32 (), i32 ()* @main

; Function Attrs: noinline nounwind optnone
define hidden void @CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_bad() #0 {
entry:
  %data = alloca i64*, align 4
  %myUnion = alloca %union.CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_unionType, align 4
  %dataBadBuffer = alloca [50 x i64], align 16
  %dataGoodBuffer = alloca [100 x i64], align 16
  %data1 = alloca i64*, align 4
  %source = alloca [100 x i64], align 16
  %i = alloca i32, align 4
  %arraydecay = getelementptr inbounds [50 x i64], [50 x i64]* %dataBadBuffer, i32 0, i32 0
  store i64* %arraydecay, i64** %data, align 4
  %0 = load i64*, i64** %data, align 4
  %unionFirst = bitcast %union.CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_unionType* %myUnion to i64**
  store i64* %0, i64** %unionFirst, align 4
  %unionSecond = bitcast %union.CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_unionType* %myUnion to i64**
  %1 = load i64*, i64** %unionSecond, align 4
  store i64* %1, i64** %data1, align 4
  %2 = bitcast [100 x i64]* %source to i8*
  call void @llvm.memset.p0i8.i32(i8* align 16 %2, i8 0, i32 800, i1 false)
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %3 = load i32, i32* %i, align 4
  %cmp = icmp ult i32 %3, 100
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %4 = load i32, i32* %i, align 4
  %arrayidx = getelementptr inbounds [100 x i64], [100 x i64]* %source, i32 0, i32 %4
  %5 = load i64, i64* %arrayidx, align 8
  %6 = load i64*, i64** %data1, align 4
  %7 = load i32, i32* %i, align 4
  %arrayidx2 = getelementptr inbounds i64, i64* %6, i32 %7
  store i64 %5, i64* %arrayidx2, align 8
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %8 = load i32, i32* %i, align 4
  %inc = add i32 %8, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond, !llvm.loop !2

for.end:                                          ; preds = %for.cond
  %9 = load i64*, i64** %data1, align 4
  %arrayidx3 = getelementptr inbounds i64, i64* %9, i32 0
  %10 = load i64, i64* %arrayidx3, align 8
  call void @printLongLongLine(i64 noundef %10) #3
  ret void
}

; Function Attrs: argmemonly nofree nounwind willreturn writeonly
declare void @llvm.memset.p0i8.i32(i8* nocapture writeonly, i8, i32, i1 immarg) #1

declare void @printLongLongLine(i64 noundef) #2

; Function Attrs: noinline nounwind optnone
define hidden void @CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_good() #0 {
entry:
  call void @goodG2B() #3
  ret void
}

; Function Attrs: noinline nounwind optnone
define hidden i32 @main() #0 {
entry:
  %call = call i64 @time(i64* noundef null) #3
  %conv = trunc i64 %call to i32
  call void @srand(i32 noundef %conv) #3
  call void @printLine(i8* noundef getelementptr inbounds ([18 x i8], [18 x i8]* @.str, i32 0, i32 0)) #3
  call void @CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_good() #3
  call void @printLine(i8* noundef getelementptr inbounds ([16 x i8], [16 x i8]* @.str.1, i32 0, i32 0)) #3
  call void @printLine(i8* noundef getelementptr inbounds ([17 x i8], [17 x i8]* @.str.2, i32 0, i32 0)) #3
  call void @CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_bad() #3
  call void @printLine(i8* noundef getelementptr inbounds ([15 x i8], [15 x i8]* @.str.3, i32 0, i32 0)) #3
  ret i32 0
}

declare void @srand(i32 noundef) #2

declare i64 @time(i64* noundef) #2

declare void @printLine(i8* noundef) #2

; Function Attrs: noinline nounwind optnone
define internal void @goodG2B() #0 {
entry:
  %data = alloca i64*, align 4
  %myUnion = alloca %union.CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_unionType, align 4
  %dataBadBuffer = alloca [50 x i64], align 16
  %dataGoodBuffer = alloca [100 x i64], align 16
  %data1 = alloca i64*, align 4
  %source = alloca [100 x i64], align 16
  %i = alloca i32, align 4
  %arraydecay = getelementptr inbounds [100 x i64], [100 x i64]* %dataGoodBuffer, i32 0, i32 0
  store i64* %arraydecay, i64** %data, align 4
  %0 = load i64*, i64** %data, align 4
  %unionFirst = bitcast %union.CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_unionType* %myUnion to i64**
  store i64* %0, i64** %unionFirst, align 4
  %unionSecond = bitcast %union.CWE121_Stack_Based_Buffer_Overflow__CWE805_int64_t_declare_loop_34_unionType* %myUnion to i64**
  %1 = load i64*, i64** %unionSecond, align 4
  store i64* %1, i64** %data1, align 4
  %2 = bitcast [100 x i64]* %source to i8*
  call void @llvm.memset.p0i8.i32(i8* align 16 %2, i8 0, i32 800, i1 false)
  store i32 0, i32* %i, align 4
  br label %for.cond

for.cond:                                         ; preds = %for.inc, %entry
  %3 = load i32, i32* %i, align 4
  %cmp = icmp ult i32 %3, 100
  br i1 %cmp, label %for.body, label %for.end

for.body:                                         ; preds = %for.cond
  %4 = load i32, i32* %i, align 4
  %arrayidx = getelementptr inbounds [100 x i64], [100 x i64]* %source, i32 0, i32 %4
  %5 = load i64, i64* %arrayidx, align 8
  %6 = load i64*, i64** %data1, align 4
  %7 = load i32, i32* %i, align 4
  %arrayidx2 = getelementptr inbounds i64, i64* %6, i32 %7
  store i64 %5, i64* %arrayidx2, align 8
  br label %for.inc

for.inc:                                          ; preds = %for.body
  %8 = load i32, i32* %i, align 4
  %inc = add i32 %8, 1
  store i32 %inc, i32* %i, align 4
  br label %for.cond, !llvm.loop !4

for.end:                                          ; preds = %for.cond
  %9 = load i64*, i64** %data1, align 4
  %arrayidx3 = getelementptr inbounds i64, i64* %9, i32 0
  %10 = load i64, i64* %arrayidx3, align 8
  call void @printLongLongLine(i64 noundef %10) #3
  ret void
}

attributes #0 = { noinline nounwind optnone "frame-pointer"="none" "min-legal-vector-width"="0" "no-builtins" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="generic" }
attributes #1 = { argmemonly nofree nounwind willreturn writeonly }
attributes #2 = { "frame-pointer"="none" "no-builtins" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="generic" }
attributes #3 = { nobuiltin "no-builtins" }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 14.0.5 (git@github.com:huangh-git/llvm-project.git be933079ef6aa62a00b606cd799aab91c68bbf8e)"}
!2 = distinct !{!2, !3}
!3 = !{!"llvm.loop.mustprogress"}
!4 = distinct !{!4, !3}
