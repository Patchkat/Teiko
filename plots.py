import pandas as pd

# Read the data
cell_data = pd.read_csv('cell-count.csv')
processed_data = pd.read_csv('processed_cell_count.csv')


full_data = pd.merge(
    processed_data, 
    cell_data[['sample', 'subject', 'condition', 'treatment', 'response']], 
    on='sample', 
    how='inner'
)

full_data.to_csv('full_cell_count.csv', index=False)