import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plot

SPI_URL = "D:\\UMassD\\Semester 2 Fall\\CIS 568 DV\\DataVizFall2020_Colab\\Individual Project\\data\\SPI.xlsx"
EFI_URL = "D:\\UMassD\\Semester 2 Fall\\CIS 568 DV\\DataVizFall2020_Colab\\Individual Project\\data\\EFI.csv"


def get_latest_data():
    spi_data = pd.read_excel(SPI_URL)
    spi_data = spi_data[spi_data['SPI_year'] == 2020]
    efi_data = pd.read_csv(EFI_URL)
    efi_data = efi_data[efi_data['Index_Year'] == 2020]
    res = efi_data[["Name", "Economic_Freedom_Index"]].merge(
        spi_data[['Country', 'Social_Progress_Index']], left_on=["Name"],
        right_on=["Country"],
        suffixes=("_efi", "_spi"))
    res = res[['Name', 'Economic_Freedom_Index', 'Social_Progress_Index']]
    res = res.reset_index(drop=True)
    # return res
    return res.to_json(orient="records")

def get_data():
    spi_data = pd.read_excel(SPI_URL)
    efi_data = pd.read_csv(EFI_URL)
    res = efi_data[["Name", "Index_Year", "Economic_Freedom_Index"]].merge(
        spi_data[['SPI_country_code', 'Country', 'SPI_year', 'Social_Progress_Index']], left_on=["Name", "Index_Year"],
        right_on=["Country", "SPI_year"],
        suffixes=("_efi", "_spi"))
    res = res[['Name','Index_Year','SPI_country_code','Economic_Freedom_Index','Social_Progress_Index']]
    res = res.reset_index(drop=True)
    # return res
    return res.to_json(orient="records")


def get_Correlation(corr_attr, year):
    year = int(year)
    if corr_attr == "efi":
        data = pd.read_csv(EFI_URL)
        data = data[data['Index_Year'] == year]
        # Name, Index_Year, Economic_Freedom_Index, Property_Rights, Judicial_Effectiveness, Government_Integrity,
        # Tax_Burden, Government_Spending, Fiscal_Health, Business_Freedom, Labor_Freedom, Monetary_Freedom,
        # Trade_Freedom, Investment_Freedom, Financial_Freedom

        data.drop('Name', inplace=True, axis=1)
        data.drop('Index_Year', inplace=True, axis=1)
        # res = res.sort_values('Social_Progress_Index').head(10)
    elif corr_attr == "spi":
        data = pd.read_excel(SPI_URL)
        data = data[data['SPI_year'] == year]
        # res = res.sort_values('Social_Progress_Index').head(10)
        data = data[['Social_Progress_Index', 'Basic_Human_Needs', 'Foundations_of_Wellbeing', 'Opportunity']]

    data = data.fillna(0)
    data = data.reset_index(drop=True)

    data_dict = {
        "data": data.to_json(),
        "corr": data.corr().fillna(0).to_json(orient="index")
    }

    return data_dict
    # return data


# data = get_Correlation("efi","2015")
# print(data.corr().fillna(0))
# get_data().to_csv("test.csv", index=False)
# get_latest_data()['Name'].to_csv("countries_name.csv", index=False)