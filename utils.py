import src.main as m
import os


def save_json():

    df = m.carregar_dados()

    if df.empty:
        print('the dataframe is empty')
        return
    
    os.makedirs('clean', exist_ok=True)

    df.to_json('clean/data.json', orient='records', lines=True)


if __name__ == '__main__':
    save_json()