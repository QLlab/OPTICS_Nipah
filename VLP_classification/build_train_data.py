import os
import pandas as pd

# Specify the root folder path containing subfolders
root_folder = r'.\'  # Replace with the actual root folder path

# Create an empty DataFrame to store the summarized data
summary_df = pd.DataFrame()

# Traverse the subfolders in the root folder
for folder_name in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder_name)

    # Check if the path is a directory
    if os.path.isdir(folder_path):
        # Traverse the files in the subfolder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Check if the file ends with ".csv"
            if file_name.endswith('.csv'):
                # Read the second column of the CSV file
                df = pd.read_csv(file_path)
                data = df.iloc[:, 1]  # Assume the second column has index 1

                # Construct a row of data, with '1' or '0' as the label followed by features
                row_data = pd.Series(['1'] + data.tolist())

                # Add the row to the summary DataFrame, handling inconsistent lengths
                summary_df = summary_df._append(row_data, ignore_index=True)

# Save the summarized DataFrame as a CSV file
summary_file_path = r'input your path'  # Replace with the actual save path
summary_df.to_csv(summary_file_path, index=False, header=False)

