# Script by Thomas Pirchmoser (tommy_software@mailfence.com) 2024

'''
change_csv_format.py--a script that rearranges the trade history .csv
    file from the Kinesis exchange to the format for Koinly or
    Cointracker.info.
'''

import os.path
import sys


# Remove the converted .csv file if it exists so we can later
#   write to a new file by appending.
CONVERTED_FILE = "Kinesis_to_Koinly.csv"
CONVERTED_FILE1 = "Kinesis_to_CointrackerInfo.csv"

if os.path.exists(CONVERTED_FILE):
    os.remove(CONVERTED_FILE)

elif os.path.exists(CONVERTED_FILE1):
    os.remove(CONVERTED_FILE1)

# Constant values of the .csv file.
EXCHANGE = "Kinesis"
GROUP = None
TYPE = "Trade"


def csv_convert(csv, csv_head):
    ''' Convert the Kinesis .csv '''

    first_line = True

    # Open the file for reading.
    with open(csv, "r", encoding="utf-8") as infile:
        for row in infile:
            col = row.split(",")

            # Extract the buy amount and buy currency.
            buy = col[6], col[7]

            # Extract the sell amount and sell currency.
            sell = col[10], col[9]

            # Extract the fee amount and fee currency.
            fee = col[11], col[12]

            # Add a comment that displays the currency swap.
            comment = f"{sell[1]}->{buy[1]}"

            # Extract the date of the trade.
            date = col[0]

            # Organize the output.
            columns1 = f"{TYPE},{buy[0]},{buy[1]},{sell[0]},{sell[1]},"
            columns2 = f"{fee[0]},{fee[1]},{EXCHANGE},{GROUP},"
            columns3 = f"{comment},{date}"

            write_new_file(csv_head, columns1, columns2, columns3, first_line)

            # After the header is written to the new file
            #   set the first_line variable to false.
            first_line = False


def write_new_file(csv_header, col1, col2, col3, first):
    ''' Write the new header and columns to a file.'''

    # Check which header is used inorder to write to the approriate file.
    if "Buy Amount" in csv_header:
        write_to = "Kinesis_to_CointrackerInfo.csv"

    else:
        write_to = "Kinesis_to_Koinly.csv"

    with open(write_to, "a+",
              encoding="utf-8") as outfile:

        # On the first line write the header.
        if first:
            outfile.write(f"{csv_header}\n")

        outfile.write(f"{col1}{col2}{col3}\n")


def tax_platform():
    ''' Ask the user to choose the tax platform and
        assign the approriate header'''

    while True:
        msg = "Please choose the platform!"
        msg1 = "Enter the number 1 for Koinly, 2 for Cointracking.info"
        msg2 = "or q to quit."
        print(f"\n{msg: ^70}")
        print(f"{msg1: ^70}")
        print(f"{msg2: ^70}")

        platform = input("Enter: ")

        if platform == "q":
            sys.exit()

        elif platform == "1":
            header1 = "Type,Buy,Cur,Sell,Cur,Fee,Cur,"
            header2 = "Exchange,Group,Comment,Date"
            header = header1 + header2

            return "koinly", header

        elif platform == "2":
            header1 = "Type,Buy Amount,Buy Currency,Sell Amount,Sell Currency"
            header2 = ",Fee,Fee Currency,Exchange,Group,Comment,Date"
            header = header1 + header2

            return "cointracking.info", header

        else:
            continue


def main():
    ''' Request the user to input the file for convertion. '''

    # Get the platform and header.
    platform, header = tax_platform()

    while True:
        try:
            msg = "Please enter the Kinesis .csv to be converted or q to quit."
            print(f"{msg: ^70}")
            csv_file = input("File name: ")

            if csv_file == "q":
                sys.exit()

            # Verify that the input file is a valid .csv file by checking
            #   that number of columns matches the 'Kinesis.csv' columns.
            with open(csv_file, "r", encoding="utf-8") as infile:
                for row in infile:
                    col = row.split(",")
                    if len(col) != 14:
                        raise IndexError

            # Make a call to the csv_convert() and print a message.
            csv_convert(csv_file, header)

            if platform == "koinly":
                msg1 = "Converted file saved as'Kinesis_to_Koinly.csv'"
                print(f"\n{msg1:*^70}\n")

            else:
                msg1 = "Converted file saved as'Kinesis_to_Cointracker.csv'"
                print(f"\n{msg1:*^70}\n")

        except FileNotFoundError:
            msg3 = "File does not seem to exist!"
            print(f"{msg3: ^70}\n")

        except IndexError:
            msg = "There seems to be an issue with your 'Kinesis.csv' file!"
            msg1 = "Please verify that the file has 14 values per line."
            print(f"\n{msg:*^70}")
            print(f"{msg1: ^70}\n")

        else:
            break


if __name__ == "__main__":
    main()
