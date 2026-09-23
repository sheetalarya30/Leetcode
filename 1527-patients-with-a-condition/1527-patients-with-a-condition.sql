SELECT *
FROM patients
where conditions like 'DIAB1%' OR
conditions LIKE '% DIAB1%';