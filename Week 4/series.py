# find max , min and avergae  
import pandas as pd

ages = pd.Series([22,35,58], name="Age")

print("Maximum Age:", ages.max())
print("Minimum Age:", ages.min())
print("Average Age:", ages.mean())