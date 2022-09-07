-- select * from analytics.trafic where type = ' Medium Vehicle'

select * from {{ source('analytics', 'trafic') }} where type = 'Medium Vehicle'
