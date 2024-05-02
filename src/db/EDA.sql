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

# Calculate change in closing prices Day to Day
select date, close, 
(close - LAG(close) OVER (ORDER BY date desc)) / LAG(close) OVER (ORDER BY date desc) AS price_perc
from historical_data;

# Identify unusual trading volume using SUBQUERY
/*
multiplying by 2 is to set a threshold for volume that is higher than twice the 
average 
volume. 
This helps identify records with exceptionally high volume
*/

select date, volume
from historical_data
where volume > ( SELECT AVG(VOLUME) * 2 from historical_data);

# Daily price range

SELECT date, high, low, (high - low) AS price_range
FROM historical_data
where (high - low) > 10
ORDER BY price_range DESC;



# Number of days where the closing was higher than the opening:

select open, close, count(close > open) as all_count
from historical_data
group by open, close
order by count(close > open) desc;



# Large price changes:
select date, high, low, (high - low) as price_range
from historical_data
where abs(high - low) > (
select AVG(high - low) * 1.5 
from historical_data
)
having price_range > 10
order by price_range desc;


# Rolling AVG closing price:
select date, close,
AVG(close) OVER (ORDER BY date ROWS BETWEEN 30 PRECEDING AND CURRENT ROW) as rolling_AVG
from historical_data;


# Bulish & Bearish
select date, close,
	case
		when close > LAG(close) OVER (ORDER BY date) then 'Bullish'
        when close < LAG(close) OVER (ORDER BY date) then 'Bearish'
        else 'Stable'
	end as trend_analysis
    from historical_data

    order by trend_analysis;
    
    
# Daily ROI    
select date, close,
	(close - LAG(close) OVER (ORDER BY date desc)) / LAG(close) OVER ( ORDER BY date desc) as daily_roi
    from historical_data;


