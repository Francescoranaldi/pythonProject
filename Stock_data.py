import os
import csv
import requests
from urllib.parse import quote


def download_stock_data(symbol, local_folder, filename):
    base_url = "https://query1.finance.yahoo.com/v7/finance/download/"
    download_url = f"{base_url}{quote(symbol)}"

    response = requests.get(download_url)

    if response.status_code == 200:
        file_path = os.path.join(local_folder, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path
    else:
        print(f"Failed to download data for {symbol}. HTTP Status Code: {response.status_code}")
        return None


def main():
    local_folder = 'local_data'
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

    symbols = ['GOOG', 'IBM', 'MSFT']
    for symbol in symbols:
        filename = f"{symbol}.csv"
        download_stock_data(symbol, local_folder, filename)
