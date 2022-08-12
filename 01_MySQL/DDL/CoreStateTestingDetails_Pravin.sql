
Create Table IF NOT EXIST CoreStateTestingDetails_Pravin
(
Seq Integer,
Date varchar(10),
State varchar(10),
TotalSamples Integer,
Negative Integer,
Positive Integer,
primary key(Seq)
)