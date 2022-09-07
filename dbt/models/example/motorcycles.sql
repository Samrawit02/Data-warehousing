-- select * from analytics.trafic where type = ' Motorcycle'
select * from {{ source('analytics', 'trafic') }} where type = 'Motorcycle'
