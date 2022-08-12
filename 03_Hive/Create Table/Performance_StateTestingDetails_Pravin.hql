Create external Table if not exists Performance_StateTestingDetails_Pravin
(
Seq Integer,
TestDate string,
TotalSamples Integer,
Negative Integer,
Positive Integer
)
partitioned by (State String)
clustered by (TestDate) into 4 buckets
STORED AS ORC
LOCATION'/user/itv001281/datalakestorage/Performance_StateTestingDetails_Pravin'
TBLPROPERTIES('orc.compress'='SNAPPY');

;