# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_Place_Name_From_Text = dataiku.Dataset("Twi_Data_Place_Name_From_Text")
Twi_Data_Place_Name_From_Text_df = Twi_Data_Place_Name_From_Text.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
place_names = Twi_Data_Place_Name_From_Text_df['place_name']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
stripped_place_names = []
for place in place_names:
    stripped_place_names.append(place..strip("'").strip('"'))
stripped_place_names

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
Twi_Data_Place_Name_Clean_df = Twi_Data_Place_Name_From_Text_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Place_Name_Clean = dataiku.Dataset("Twi_Data_Place_Name_Clean")
Twi_Data_Place_Name_Clean.write_with_schema(Twi_Data_Place_Name_Clean_df)