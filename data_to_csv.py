from utils.get_directory_files import GetDirectoryFiles
from utils.stock_direction import StockDirection
from utils.pdf_file import PdfFile
import csv


def save_data_to_csv(data, filename):
  with open(filename, "w", newline="") as csvfile:
    fieldnames = []
    if data and data[0]:
      fieldnames += list(data[0].keys())  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)


  with open(filename, "w", newline="") as csvfile:
    fieldnames = []
    if data and data[0]:
      fieldnames += list(data[0].keys())  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

processed_report_data = []

files = GetDirectoryFiles()
files.set_directory_path("./data/reports")

for file in files.get_files():
  print(f"Processing {file}")
  try:
    release_date = file.split('.')[2]

    pdf_file = PdfFile()
    pdf_file.set_pdf_path(file)
    pdf_data = pdf_file.get_data()

    stock_info = StockDirection()
    stock_info.set_symbol("^BVSP")
    stock_info.set_start_date(release_date)
    stock_info.set_interval("1h")
    stock_direction = stock_info.get_first_candle_direction()

    processed_report_data.append({
        "releaseDate": release_date,
        "stockDirection": stock_direction,
        **pdf_data
    })

  except:
    print(f"Error reading {file}")

save_data_to_csv(processed_report_data, "./data/csv/reports-data.csv")

print("Reports data saved into csv file")