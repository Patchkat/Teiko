import pandas as pd

# Read the data and make the processed data DataFrame
cell_data = pd.read_csv('cell-count.csv')
processed_data = pd.DataFrame(columns=['sample', 'total_count', 'population', 'count', 'percentage'])

# Loop through each row of the data
for index, row in cell_data.iterrows():
    # Grab the total count and sample name
    total_count = sum(row[10:])
    sample = row['sample']
    # Loop through each cell type and calculate the percentage
    for i in ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']:
        population = i
        count = row[i]
        percentage = (count / total_count) * 100
        processed_data.loc[len(processed_data)] = [sample, total_count, population, count, percentage]
# Output the processed data to a CSV file
processed_data.to_csv('processed_cell_count.csv', index=False)