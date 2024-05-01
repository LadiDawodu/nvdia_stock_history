# Order date by date
select * 
from `historical_data`
order by date;


# Check avg Close
select round(AVG (close),2)
from historical_data;

# Calculate MAX / MIN close
select max(close) as max_close, min(close) as min_close
from historical_data;

# Calculate the total volume trend
select sum(volume)
from historical_data;