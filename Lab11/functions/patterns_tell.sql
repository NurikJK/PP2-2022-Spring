CREATE OR REPLACE FUNCTION pattern_tell(p_pattern VARCHAR)
    RETURNS TABLE (
        account_username VARCHAR,
        account_tell VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        username,
        tell
    FROM
        accounts2
    WHERE
        tell LIKE p_pattern;
END; $$
LANGUAGE plpgsql;