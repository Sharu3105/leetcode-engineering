WITH ConsecutiveGroups AS (
    SELECT *,
           id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
GroupCounts AS (
    SELECT *,
           COUNT(*) OVER (PARTITION BY grp) AS count_per_grp
    FROM ConsecutiveGroups
)
SELECT id, visit_date, people
FROM GroupCounts
WHERE count_per_grp >= 3
ORDER BY visit_date;
