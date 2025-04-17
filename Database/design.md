The initial data given has the following tags:

- **project**
- **subject**
- **condition**
- **age**
- **sex**
- **treatment**
- **response**
- **sample**
- **sample_type**
- **time_from_treatment_start**
- **b_cell**
- **cd8_t_cell**
- **cd4_t_cell**
- **nk_cell**
- **monocyte**

The best way to store this info this would be using a relational database such as MariaDB (MySQL).
The following schema would be an efficient way to store the data without too much repetition.

For storing subject data, there would be a **Subjects** table that stores information about a given subject.

| Column | Description |
| ------ | --- |
| subject_id |Unique ID for the subject (PRIMARY KEY) |
| project_id | Can reference a **Projects** table with more info on a given project if wanted |
| age |Age of the subject |
| sex | Biological sex of the subject |
| condition | The condition that the subject has |

For tracking what treatment is given to a certain subject, there should be a **Subject Treatment** table.

| Column | Description |
| ------ | ---------- |
| subject_id   | Foreign key to the **Subjects** table (PRIMARY KEY)      |
| treatment_id | Can reference a **Treatments** table with more info on the specific treatment if wanted (PRIMARY KEY) |
| response     |Treatment response ('y', 'n', or NULL) |

For keeping track of a given sample, a **Samples** table should be used.

| Column  | Description  |
| ---- | -------- |
| sample_id | Unique ID for the biological sample (PRIMARY KEY)  |
| subject_id | Foreign key to the **Subjects** table (PRIMARY KEY if sample_id is not guaranteed unique)  |
| sample_type  |  Type of sample  |
| time_from_start | Days from treatment start (NULL for untreated if needed) |

Now if all that is needed are the types of cells in the given cell-count.csv, it would likely be best to just add those to the **Samples** table and include the counts in there. However, if there is the potential to have other cells (or just a larger variety of cells) it would be best to have a separate **Cells** table that keeps track of the counts of a given type of cell attached to a certain sample.

| Column  | Description  |
| --- | ------ |
| sample_id  | Foreign key to the **Samples** table (PRIMARY KEY)  |
| cell_type  | Type of cell (PRIMARY KEY) |
| cell_count | Cell count |