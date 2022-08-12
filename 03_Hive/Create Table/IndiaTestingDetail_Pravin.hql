Create external Table if not exists  IndiaTestingDetail_Pravin
(
Sno Integer,
TestDate string,
State string,
Cured Integer,
Deaths Integer,
Confirmed Integer
)
row format delimited
fields terminated by ','
stored as textfile
location '/user/itv001281/datalakestorage/CoreIndiaTestingDetail_Pravin';