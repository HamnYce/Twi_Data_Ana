# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_Place_Name_From_Text = dataiku.Dataset("Twi_Data_Place_Name_From_Text")
Twi_Data_Place_Name_From_Text_df = Twi_Data_Place_Name_From_Text.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Twi_Data_Place_Name_Clean_df = Twi_Data_Place_Name_From_Text_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_Place_Name_Clean = dataiku.Dataset("Twi_Data_Place_Name_Clean")
Twi_Data_Place_Name_Clean.write_with_schema(Twi_Data_Place_Name_Clean_df)
