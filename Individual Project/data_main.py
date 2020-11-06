import pandas as pd
import json

SPI_URL = "D:\\UMassD\\Semester 2 Fall\\CIS 568 DV\\DataVizFall2020_Colab\\Individual Project\\data\\SPI.xlsx"
EFI_URL = "D:\\UMassD\\Semester 2 Fall\\CIS 568 DV\\DataVizFall2020_Colab\\Individual Project\\data\\EFI.csv"

data = []
def get_data():
    spi_data = pd.read_excel(SPI_URL)
    res = spi_data[spi_data['SPI_year'] == 2020]
    # res = res.sort_values('Social_Progress_Index').head(10)
    res = res[['SPI_Rank', 'SPI_country_code', 'Country', 'Social_Progress_Index']]
    res = res.reset_index(drop=True)
    # return res
    return res.to_json(orient="records")


def get_Correlation(attr_var="efi"):
    if (attr_var == "efi"):
        data = pd.read_csv(EFI_URL)
        data = data[data['Index_Year'] == 2020]
        # Name, Index_Year, Overall_Score, Property_Rights, Judicial_Effectiveness, Government_Integrity, Tax_Burden, Government_Spending, Fiscal_Health, Business_Freedom, Labor_Freedom, Monetary_Freedom, Trade_Freedom, Investment_Freedom, Financial_Freedom

        data.drop('Name', inplace=True, axis=1)
        data.drop('Index_Year', inplace=True, axis=1)
        # res = res.sort_values('Social_Progress_Index').head(10)
    elif (attr_var == "spi"):
        data = pd.read_excel(SPI_URL)
        data = data[data['SPI_year'] == 2020]
        # res = res.sort_values('Social_Progress_Index').head(10)
        data = data[['Social_Progress_Index', 'Basic_Human_Needs', 'Foundations_of_Wellbeing', 'Opportunity']]

    dict = {
        "data": data.to_json(),
        "corr": data.corr().to_json(orient="index")
    }

    return dict


print(get_Correlation())
