import pandas as pd


cell_data = pd.read_csv('cell-count.csv')
processed_data = pd.DataFrame(columns=['sample', 'total_count', 'population', 'count', 'percentage'])
for index, row in cell_data.iterrows():
    total_count = sum(row[10:])
    sample = row['sample']
    for i in ['b_cell', 'cd8_t_cell', 'cd4_t_cell', 'nk_cell', 'monocyte']:
        population = i
        count = row[i]
        percentage = (count / total_count) * 100
        processed_data.loc[len(processed_data)] = [sample, total_count, population, count, percentage]
print(processed_data)