create 'students_pravin' ,'personal_details','contact_details','marks';

put 'students_pravin','01','personal_details:name','personal_details:Pravin';

scan 'students_pravin'

get  'students_pravin' ,'01'

describe 'students_pravin'

disable 'students_pravin'

drop 'students_pravin'

##########################################################################################################

scan "covid_hbase_pravin"

scan "covid_hbase_pravin",{'LIMIT' => 10}

get 'covid_hbase_pravin','Maharashtra_2020-06-04'


#Next time same record takes less time as it is present in block cache
get 'covid_hbase_pravin','Maharashtra_2020-06-04'

select * from COVID_HIVE_PRAVIN where STATE='Maharashtra' and TESTINGDATE='2020-06-04';


So hive takes more time to search the same record compared to hbase .
Conclusion:  HBase performs quick searches (takes very lesstime) as compared to Hive