## Advantages of Using a Database

One main advantage of capturing all this information inside a database is the efficiency provided by modern relational databases, both in terms of memory usage and query performance. Additionally, instead of writing extensive code to handle processing CSV files and the like, you can simply write a few SQL queries to retrieve the desired information from the database. It also reduces the need to manage multiple files once the data is stored in the database.

Another benefit is the general simplicity of SQL queries. This makes it easier for non-programmer team members to access the information they need without having to wait for someone else to get the data and send it to them. As a result, this can significantly improve office efficiency, especially in teams with many non-programmers.

The database also allows for data constraints to be enforced (such as all necessary fields being non-null), and often have fairly good security options to limit access to certain pieces of data. The scalability of the database also cannot be understated as an important advantage. If all of the data is being stored in CSVs, as the amount of data increases so does the number of CSV files in the network. This can lead to issues with finding the correct data or accidentally deleting certain pieces of data when trying to clear things out.

## Queries

### Number of Subjects in Each Condition
```sql
SELECT condition, COUNT(*) AS subject_count
FROM Subjects
GROUP BY condition;
```

### All Melanoma PBMC samples at tfts = 0

```sql
SELECT s.sample_id, s.sample_type, s.time_from_start
FROM Samples s
JOIN Subjects sub ON s.subject_id = sub.subject_id
JOIN Subject_Treatments st ON sub.subject_id = st.subject_id
WHERE sub.condition = 'melanoma'
  AND s.sample_type = 'PBMC'
  AND s.time_from_start = 0
  AND st.treatment_id = 'tr1';

```

### Samples From Each Project
```sql
SELECT sub.project_id, COUNT(*) AS sample_count
FROM Samples s
JOIN Subjects sub ON s.subject_id = sub.subject_id
JOIN Subject_Treatments st ON sub.subject_id = st.subject_id
WHERE sub.condition = 'melanoma'
  AND s.sample_type = 'PBMC'
  AND s.time_from_start = 0
  AND st.treatment_id = 'tr1'
GROUP BY sub.project_id;

```
### # Responders/Non-Responders
```sql
SELECT st.response, COUNT(*) AS count
FROM Samples s
JOIN Subjects sub ON s.subject_id = sub.subject_id
JOIN Subject_Treatments st ON sub.subject_id = st.subject_id
WHERE sub.condition = 'melanoma'
  AND s.sample_type = 'PBMC'
  AND s.time_from_start = 0 -- As this check is specific, it should ignore entries where there is no time_from_start given (which may or may not be wanted in this case)
  AND st.treatment_id = 'tr1'
  AND st.response IS NOT NULL -- This prevents null from showing up as a third response category, could be removed if that is a value that should be checked
GROUP BY st.response;

```

### # Males/Females
```sql
SELECT sub.sex, COUNT(*) AS count
FROM Samples s
JOIN Subjects sub ON s.subject_id = sub.subject_id
JOIN Subject_Treatments st ON sub.subject_id = st.subject_id
WHERE sub.condition = 'melanoma'
  AND s.sample_type = 'PBMC'
  AND s.time_from_start = 0
  AND st.treatment_id = 'tr1'
GROUP BY sub.sex;

```