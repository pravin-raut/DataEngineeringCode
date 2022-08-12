set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;
set hive.enforce.bucketing=true;

insert overwrite table Performance_IndiaTestingDetail_Pravin
partition(state)
select Sno,from_unixtime(unix_timestamp(TestDate,'M/dd/yyyy'),'yyyy-MM-dd'),Cured,Deaths,Confirmed,State from IndiaTestingDetail_Pravin;