import pandas as pd

SPI_URL = "D:\\UMassD\\Semester 2 Fall\\CIS 568\\DataVizFall2020_Colab\\Individual Project\\data\\SPI.xlsx"
EFI_URL = "D:\\UMassD\\Semester 2 Fall\\CIS 568\\DataVizFall2020_Colab\\Individual Project\\data\\EFI.csv"


def get_data():
    spi_data = pd.read_excel(SPI_URL)
    res = spi_data[spi_data['SPI_year'] == 2020]
    # res = res.sort_values('Social_Progress_Index').head(10)
    res = res[['SPI_Rank', 'SPI_country_code', 'Country', 'Social_Progress_Index']]
    res = res.reset_index(drop=True)
    # return res
    return res.to_json(orient="records")

def get_Correlation():
    spi_data = pd.read_excel(SPI_URL)
    res = spi_data[spi_data['SPI year'] == 2020]
    # res = res.sort_values('Social_Progress_Index').head(10)
    res = res[['SPI_Rank', 'Country', 'Social_Progress_Index']]
    res = res.reset_index(drop=True)
    # return res
    return res.to_json(orient="records")
# print(get_data()['Country'])
