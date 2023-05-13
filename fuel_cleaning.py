def clean_fuel_df(filepath):
    '''
    Given local filepath of fuel_consumption.csv, imports and cleans  file, then returns final datframe. 
    '''
    import numpy as np
    import pandas as pd
    
    # import data
    fuel_cols = ['month', 'airline_id', 'unique_carrier', 'carrier', 'carrier_name', 'carrier_group_new', 'sdomt_gallons', 'satl_gallons', 'spac_gallons', 'slat_gallons', 'sint_gallons', 'ts_gallons', 'tdomt_gallons', 'tint_gallons', 'total_gallons', 'sdomt_cost', 'satl_cost', 'spac_cost', 'slat_cost', 'sint_cost', 'ts_cost', 'tdomt_cost', 'tint_cost', 'total_cost', 'year']
    fuel_df = pd.read_csv(filepath, header=None, names=fuel_cols)

    # First row missing values can be matched to row beneath it
    fuel_df.iloc[0,2] = '0JQ'
    fuel_df.iloc[0,1] = 21236
    fuel_df.iloc[0,4] = 'Vision Airlines'

    # calculate missing tint_cost
    fuel_df['tint_cost'].fillna(value=(fuel_df['total_cost'] - fuel_df['tdomt_cost']), inplace=True)

    # calculate missing total_gallons
    fuel_df['total_gallons'].fillna(value=(fuel_df['tdomt_gallons'] + fuel_df['tint_gallons']), inplace=True)

    # calculate missing tdomt_gallons
    fuel_df['tdomt_gallons'].fillna(value=(fuel_df['total_gallons'] - fuel_df['tint_gallons']), inplace=True)

    # drop remaining rows with null values.
    fuel_df.dropna(inplace=True)

    return fuel_df

