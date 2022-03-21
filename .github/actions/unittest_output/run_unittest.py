# Simple unit test for checking that all wanted columns are in our raw data
import pandas as pd

OUTPUT_COLUMNS = ["PassengerId","Survived"]

def unittest_input_cols(df: pd.DataFrame, cols: str, dataset_name: str):

    for row in df.iterrows():
        assert row[cols[1]] in [1,0] ,f"row with id {row[cols[0]]} has incorrect output format."

def main():
    # Read data
    output = pd.read_csv("data/output/final_predictions.csv")
    
    # Unit tests
    unittest_input_cols(output, OUTPUT_COLUMNS, 'output')
    
    # Success
    print('All input unit tests passed!')
    
if __name__ == '__main__':
    main()
