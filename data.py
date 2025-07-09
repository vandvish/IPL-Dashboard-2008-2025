import pandas as pd
import os

def clean_ipl_data(input_file='IPL_cleaned.csv', output_format='csv'):
    try:
        df = pd.read_csv(input_file)
        
        # Data cleaning steps
        empty_cols = [col for col in df.columns if df[col].isna().all()]
        if empty_cols:
            df.drop(columns=empty_cols, inplace=True)

        missing_indicators = ['', 'NA', 'N/A', 'NaN', 'null', 'NULL', '?', '-', 'na', 'n/a', 'None']
        df.replace(missing_indicators, pd.NA, inplace=True)

        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)

        base_name = os.path.splitext(input_file)[0]
        
        if output_format == 'parquet':
            try:
                output_file = f"{base_name}.parquet"
                df.to_parquet(output_file, engine='pyarrow')
            except ImportError:
                print("PyArrow not found. Falling back to CSV format.")
                output_format = 'csv'
        
        if output_format == 'feather':
            try:
                output_file = f"{base_name}.feather"
                df.to_feather(output_file)
            except ImportError:
                print("Feather format not supported. Falling back to CSV.")
                output_format = 'csv'
        
        if output_format == 'csv':
            output_file = f"{base_name}_processed.csv"
            df.to_csv(output_file, index=False)
        
        return df, output_file

    except Exception as e:
        print(f"Error during processing: {str(e)}")
        return None, None

if __name__ == "__main__":
    cleaned_df, output_path = clean_ipl_data()
    if output_path:
        print(f"Data cleaning complete. Output saved to: {output_path}")
    else:
        print("Data cleaning failed. Check error messages above.")