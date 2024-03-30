
change_csv_format.py--is a Python script that rearranges the trade history .csv file 
 from the Kinesis exchange to the format for Koinly or Cointracker.info.
It iterates through each line of the Kinesis.csv input file, extracts 
 necessary information from each row, and writes them to a new .csv file
 with the appropriate header.
The script then writes this data to the output file.
 Finally, it prints a message indicating that the conversion is complete.

Here are the steps involved in using the script:

1. Save the change_csv_format.py script to your desired location on your computer.
2. Open a terminal or command prompt and navigate to the directory containing the Python
    file.
3. Run the following command: 
    python3 change_csv_format.py
4. Select either Koinly, Cointracker.info or 'q' to quit.
5. Select the Kinesis trade history.csv file when prompted by entering its name, or 
    type 'q' to quit the script.
6. The script will create a new .csv file named `Kinesis_to_Koinly.csv` or
    'Kinesis_to_Cointracker.csv' in the same directory as the input file
    containing the data converted to Koinly format.

Note:
This script has been written with python3.10.12 and may work with
 earlier versions.
