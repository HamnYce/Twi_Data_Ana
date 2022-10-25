# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Twi_Data_Place_Name_Extract_prepared = dataiku.Dataset("Twi_Data_Place_Name_Extract_prepared")
Twi_Data_Place_Name_Extract_prepared_df = Twi_Data_Place_Name_Extract_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Twi_Data_clean_place_name_df = Twi_Data_Place_Name_Extract_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
Twi_Data_clean_place_name = dataiku.Dataset("Twi_Data_clean_place_name")
Twi_Data_clean_place_name.write_with_schema(Twi_Data_clean_place_name_df)
