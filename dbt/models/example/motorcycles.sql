-- select * from analytics.trafic_data where type = 'Motorcycle'
select * from {{ source('analytics', 'trafic_data') }} where type = 'Motorcycle'
