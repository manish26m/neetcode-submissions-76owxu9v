create table videos(
    id INT Primary key,
    name text not null,
    created_at Date,
    published BOOLEAN 
);






-- Do not modify below this line --
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_name = 'videos';
