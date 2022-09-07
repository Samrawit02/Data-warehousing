
select * from {{ source('analytics', 'trafic') }} where type = 'Taxi'
