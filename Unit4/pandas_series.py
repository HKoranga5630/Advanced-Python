import pandas as pd
import numpy as np

# Generate ten random numbers
random_numbers = np.random.rand(10)

# Create a Pandas Series
series = pd.Series(random_numbers)

# Display the Series
print("Pandas Series with ten random numbers:")
print(series)