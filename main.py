import pandas as pd
from pathlib import Path
import numpy as np


def carregar_dados():

    file = Path('..', 'raw', 'data.csv')

    df = pd.read_csv(file)

    # this call is to calculate the sum, mean, min, max and count of the Price column grouped by Condition
    price_agg = df.groupby('Condition').agg({
        'Price': [np.sum, np.mean, np.min, np.max, 'size']
    })

    # this call is to count the number of values in the Condition column
    counting_values = df['Condition'].value_counts()
    print(counting_values)

    # this call is to calculate the sum, mean, min, max and count of the Price column grouped by Brand
    agg_price = df.groupby('Bran')['Price'].agg(
        [np.sum, np.mean, np.min, np.max, 'size']
    )
    print(agg_price)

    # this call is to count the number of values in the Brand column
    counting_brand = df['Brand'].value_counts()
    print(counting_brand)

    print(df.head(10))
    return  price_agg


# this is the main function
def main():
    df = carregar_dados()

    print(df.head(10))

# this is the entry point of the script
if __name__ == '__main__':
    main()