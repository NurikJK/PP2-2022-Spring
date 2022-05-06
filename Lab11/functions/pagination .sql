CREATE OR REPLACE FUNCTION pagination(lim INTEGER, off INTEGER)
    RETURNS TABLE(
    account_username VARCHAR,
    account_tell VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        *
    FROM
        accounts2
    LIMIT lim OFFSET off;
END; $$
LANGUAGE plpgsql;