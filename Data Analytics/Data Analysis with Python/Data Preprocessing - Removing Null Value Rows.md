## Data Preprocessing - Removing Null Value Rows

```markdown

When creating a DataFrame from a CSV file, many blank columns are imported as null values into the DataFrame, which later creates problems while operating on that DataFrame. `Pandas` `isnull()` and `notnull()` methods are used to check and manage NULL values in a DataFrame.

### DataFrame.isnull()
**Syntax:** `DataFrame.isnull()` or `Pandas.isnull("DataFrame Name")`  
**Parameters:** Object to check null values for  
**Return Type:** DataFrame of Boolean values which are True for NaN values  

If we add the `sum()` function after `isnull()`, it will give us the total number of data which are not present or null in our dataset.

Let's see with the help of an example:

```python
import pandas as pd
data = pd.read_csv("googleplaystore.csv")
print(data.isnull().sum())
```

**Output:**

```
App                  0
Category             0
Rating            1474
Reviews              0
Size                 0
Installs             0
Type                 1
Price                0
Content Rating       1
Genres               0
Last Updated         0
Current Ver          8
Android Ver          3
dtype: int64
```

So, we can see that our columns are `App`, `Category`, `Rating`, etc. The number displayed after the column names is the total number of null values that particular column contains.

We can delete all the rows which are present in our DataFrame with the help of `dropna()` function. Let's see the implementation of that now:

```python
df = data.dropna()
print(df.isnull().sum())
```

**Output:**

```
App               0
Category          0
Rating            0
Reviews           0
Size              0
Installs          0
Type              0
Price             0
Content Rating    0
Genres            0
Last Updated      0
Current Ver       0
Android Ver       0
dtype: int64
```

So, no more null values are present in any of the columns.
```
