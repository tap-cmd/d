#Aim: Reshaping Hierarchical Data and Pivoting DataFrame Data.
import pandas as pd

print("Pandas Version: ", pd.__version__)

print("Step 1 :Create Hierarchical (MultiIndex) Data: ")
data = {
    "Sales": [25000, 30000, 20000, 28000]
}

index = pd.MultiIndex.from_tuples(
    [
        ("North", "Laptop"),
        ("North", "Mobile"),
        ("South", "Laptop"),
        ("South", "Mobile")
    ],
    names=["Region", "Product"]
)

df = pd.DataFrame(data, index=index)
print(df , " \n")

print("Step 2: Unstack (Reshape Rows → Columns)")

unstacked_df = df.unstack()
print(unstacked_df, " \n")

print("Step 3: Stack (Columns → Rows)")
future_stack=True 
stacked_df = unstacked_df.stack()
print(stacked_df, "\n")


print("Part B: Pivoting DataFrame  \n")

print("Create DataFrame \n")
data = {
    "Region": ["North", "North", "South", "South"],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile"],
    "Sales": [25000, 30000, 20000, 28000]
}

df2 = pd.DataFrame(data)
print(df2, " \n")

print("Pivot the DataFrame  \n")

pivot_df = df2.pivot(index="Region",
                     columns="Product",
                     values="Sales")
print(pivot_df, " \n")

print("Pivot Table (Aggregation)  \n")
pivot_table_df = pd.pivot_table(
    df2,
    index="Region",
    columns="Product",
    values="Sales",
    aggfunc="sum"
)
print(pivot_table_df, " \n")
