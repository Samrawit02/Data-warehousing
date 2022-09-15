-- select * from analytics.trafic_data where type = 'Medium Vehicle'

select * from {{ source('analytics', 'trafic_data') }} where type = 'Medium Vehicle'
