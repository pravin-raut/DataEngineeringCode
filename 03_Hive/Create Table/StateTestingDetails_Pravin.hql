
Create external Table if not exists StateTestingDetails_Pravin
(
Seq Integer,
TestDate string,
State string,
TotalSamples Integer,
Negative Integer,
Positive Integer
)
row format delimited
fields terminated by ','
stored as textfile
location '/user/itv001281/datalakestorage/CoreStateTestingDetails_Pravin';