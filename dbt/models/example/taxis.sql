-- analytics.trafic_data
-- select * from analytics.trafic_data where type = 'Taxi'
select * from {{ source('analytics', 'trafic_data') }} where type = 'Taxi'
