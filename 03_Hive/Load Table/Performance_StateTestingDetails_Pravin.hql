set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;
set hive.enforce.bucketing=true;

insert overwrite table Performance_StateTestingDetails_Pravin
partition(state)
select Seq,from_unixtime(unix_timestamp(TestDate,'M/dd/yyyy'),'yyyy-MM-dd'),TotalSamples,Negative,Positive,state from StateTestingDetails_Pravin;