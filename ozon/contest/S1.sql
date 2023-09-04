
 SELECT 
    f.id as fulfilment_id,
    f.name as fulfilment_name,
    p.id as package_id,
    p.name as package_name,
    
    # to_char(arrival_time(1444646136079 / 1000), 'yyyy-mm-dd HH24:MI:SS') as cahr_2,
    #arrival_time as time_in,
    TO_CHAR(arrival_time::date, 'yyyy-mm-dd HH:MI:SS') as time_in,
    #time_out,
    TO_CHAR(time_out::date, 'yyyy-mm-dd HH:MI:SS') as time_out,
    #EXTRACT(EPOCH FROM (time_out - arrival_time))/60/60/24 as storage_time,
    #TO_CHAR(AGE(time_out, arrival_time),'DD "days"') as storage_time,
    #extract(day from AGE(time_out,å arrival_time)) as storage_time,
    #AGE(time_out, arrival_time) as storage_time2,
     CASE
        WHEN extract(days from age(time_out, arrival_time)) = 1 THEN
            extract(days from age(time_out, arrival_time)) || ' day'
        ELSE
            extract(days from age(time_out, arrival_time)) || ' days'
    END as storage_time
    
FROM (
    SELECT 
        t1.package_id,
        t1.destination_id,
        t1.arrival_time,
        t2.departure_time as time_out
    FROM transportations t1
    LEFT JOIN transportations t2 ON t1.package_id = t2.package_id 
                                 AND t1.destination_id = t2.source_id
) as t_out
JOIN packages p ON t_out.package_id = p.id
JOIN fulfilments f ON t_out.destination_id = f.id
WHERE t_out.time_out IS NOT NULL
ORDER BY storage_time DESC, time_in, fulfilment_id, package_id;