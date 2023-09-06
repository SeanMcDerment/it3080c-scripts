# This Script Downloads Covid Data and Displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
HOSP=$(echo $DATA | jq '.[0].hospitalized')
HOSPCURRENT=$(echo $DATA | jq '.[0].hospitalizedCurrently')
ICUCURRENT=$(echo $DATA | jq '.[0].inIcuCurrently')
TOTALTESTRESULTS=$(echo $DATA | jq '.[0].totalTestResults')

TODAY=$(date)

echo "As of $TODAY,
There has been $TOTALTESTRESULTS total Covid test results,
There has been $POSITIVE positive cases,
There has been $NEGATIVE negative tests,
There has been $DEATH deaths, 
There has been $HOSP people hospitalized in total,
There are currently $HOSPCURRENT people in the hospital,
There are Currently $ICUCURRENT people in the ICU. "

