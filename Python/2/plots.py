import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cell_data = pd.read_csv('cell-count.csv')
processed_data = pd.read_csv('processed-cell-count.csv')

# Merge the processed data with the necessary info from cell_data
full_data = pd.merge(
    processed_data,
    cell_data[['sample', 'subject', 'condition', 'treatment', 'response']], 
    on='sample',
    how='inner'
)

# Create a mask for the conditions
mask_treatment = full_data['treatment'] == 'tr1'
mask_condition = full_data['condition'] == 'melanoma'

# Filter the data 
filtered_data = full_data[mask_treatment & mask_condition]
tr1_patients = filtered_data['subject'].unique()

# Split the data into responders and non-responders
# If a patient has no response value, they are ignored
responders = filtered_data[filtered_data['response'] == 'y'][['population', 'percentage', 'response']]
non_responders = filtered_data[filtered_data['response'] == 'n'][['population', 'percentage', 'response']]

# Create the boxplot
plt.figure()
sns.boxplot(
    x='population',
    y='percentage',
    hue='response',
    data=pd.concat([responders, non_responders]),
    palette={'y': 'skyblue', 'n': 'lightcoral'},
    dodge=True
)
plt.title('Cell Population Frequency by Response')
plt.xlabel('Cell Population')
plt.ylabel('Cell Frequency (%)')
plt.legend(title='Responder', loc='lower left')
plt.tight_layout()
plt.savefig('cell_population_response.png')

# Save the filtered data for further analysis
save_data = pd.concat([responders, non_responders])
save_data.to_csv('cell-population-response.csv', index=False)
