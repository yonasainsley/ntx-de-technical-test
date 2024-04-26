--# Test Case 1
with countries as (
    sum(totalTransactionRevenue), country
    from ecommerce_session_bigquery
    group by country
    order by sum(totalTransactionRevenue) desc limit 5
)
select sum(totalTransactionRevenue), country, channelGrouping
from ecommerce_session_bigquery
where country in (select country from countries)
group by country, channelGrouping
;

--# Test Case 2
select fullVisitorId, timeOnSite, pageviews, sessionQualityDim
from ecommerce_session_bigquery
where timeOnsite > (select avg(cast(timeOnsite as int)) from ecommerce_session_bigquery)
and pageviews < (select avg(cast(pageviews as int)) from ecommerce_session_bigquery)
-- I noticed that the data type for the columns 'timeOnSite' and 'pageviews' are text, so i converted them into int
;

--# Test Case 3
select  sum(totalTransactionRevenue),
        sum(productQuantity),
        sum(productRefundAmount),
        sum(totalTransactionRevenue) - sum(productRefundAmount) as netRevenue
        v2ProductName,
        case
            when sum(productRefundAmount) > 0.1 * sum(totalTransactionRevenue)
            then 'Greater Than 10%'
            else 'Lower Than 10%'
        end as productRefundPercentage
from ecommerce_session_bigquery
group by v2ProductName
order by sum(totalTransactionRevenue) - sum(productRefundAmount)
;
