import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data.csv")
print(data)

data['log2_FC'] = (data['treated'] / data['control']).apply(lambda x: None if x <= 0 else np.log2(x))

Upregulated_gene = data.nlargest (10,'log2_FC')

Downregulated_gene = data.nsmallest(10,'log2_FC')

print("\nTop Upregulated Genes:\n", Upregulated_gene[['gene_name', 'log2_FC']])
print("\nTop Downregulated Genes:\n", Downregulated_gene[['gene_name', 'log2_FC']])


plt.figure(figsize=(8, 5))

plt.bar(Upregulated_gene['gene_name'], Upregulated_gene['log2_FC'],
        color='green', label='Upregulated genes', width=0.4)
plt.bar(Downregulated_gene['gene_name'], Downregulated_gene['log2_FC'],
        color='black', label='Downregulated genes', width=0.4)

plt.xticks(rotation=45, ha='right')
plt.title("Top Differentially Expressed Genes")
plt.ylabel("Log2 Fold Change")
plt.grid( axis='y', linestyle ='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
