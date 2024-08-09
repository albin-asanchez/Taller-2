CREATE OR REPLACE FUNCTION GetEmployees()
RETURNS JSON AS $$
DECLARE
    result JSON;
BEGIN
    SELECT json_agg(e) INTO result
    FROM Employees e;
    
    RETURN result;
END;
$$ LANGUAGE plpgsql;
