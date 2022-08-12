Create external Table if not exists  Performance_IndiaTestingDetail_Pravin
(
Sno Integer,
TestDate string,
Cured Integer,
Deaths Integer,
Confirmed Integer
)
partitioned by (State String)
clustered by (TestDate) into 4 buckets
STORED AS ORC
LOCATION'/user/itv001281/datalakestorage/Performance_IndiaTestingDetail_Pravin'
TBLPROPERTIES('orc.compress'='SNAPPY');
;