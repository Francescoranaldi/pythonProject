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


def calculate_percentage_change(open_price, close_price):
    return ((close_price - open_price) / open_price) * 100

def process_csv_file(input_path, output_folder):
    output_path = os.path.join(output_folder, os.path.basename(input_path))

    with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        header.append('Percentage Change')

        writer.writerow(header)

        for row in reader:
            open_price = float(row[1])
            close_price = float(row[4])
            percentage_change = calculate_percentage_change(open_price, close_price)

            row.append(percentage_change)
            writer.writerow(row)

    return output_path

def main():
    # Step 1: Download CSV files
    local_folder = 'local_data'
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

    urls = [
        'https://finance.yahoo.com/q/hp?s=GOOG',
        'https://finance.yahoo.com/q/hp?s=IBM',
        'https://finance.yahoo.com/q/hp?s=MSFT'
    ]

    for url in urls:
        filename = f"{url.split('=')[-1]}.csv"
        download_stock_data(url, local_folder, filename)

    # Step 2: Process CSV files and calculate percentage change
    output_folder = 'output_data'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(local_folder):
        if filename.endswith(".csv"):
            input_path = os.path.join(local_folder, filename)
            process_csv_file(input_path, output_folder)

if __name__ == "__main__":
    main()

