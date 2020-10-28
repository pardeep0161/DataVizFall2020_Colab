import pandas as pd


SPI_URL = "C:\\Users\\Parde\\PycharmProjects\\pythonProject\\Individual Project\\data\\SPI.xlsx"
EFI_URL = "C:\\Users\\Parde\\PycharmProjects\\pythonProject\\Individual Project\\data\\EFI.csv"


def get_data():
    spi_data = pd.read_excel(SPI_URL)
    res = spi_data[spi_data['SPI year'] == 2020]
    res = res.sort_values('Social_Progress_Index').head(10)
    res = res[['SPI_Rank', 'Country', 'Social_Progress_Index']]
    res = res.reset_index(drop=True)
    return res.to_json(orient="records")

# print(get_data())