# CSV Trimmer

## Introduciton
This project was made in Python 3.8.3. I made it for fun but feel free to use it however you want.
It does exactly what it says on the tin i.e. trims extra unused elements from your .csv files.
## Usage
1. Place your .csv file in this directory.
2. Run ```python csv_trimmer.py *csv file name*```
3. Profit
## Example
Input:
```bash
user@computer: python mycsvfile.csv 
```
mycsvfile.csv
```csv
"LatD", "LatM", "LatS", "NS", "LonD", "LonM", "LonS", "EW", "City", "State", , ,
   41,    5,   59, "N",     80,   39,    0, "W", "Youngstown", OH, , ,
   42,   52,   48, "N",     97,   23,   23, "W", "Yankton", SD, , ,
   ...
```
Output:  
mycsvfile_trimmed.csv
```csv
"LatD", "LatM", "LatS", "NS", "LonD", "LonM", "LonS", "EW", "City", "State"
41, 5, 59, "N", 80, 39, 0, "W", "Youngstown", OH
42, 52, 48, "N", 97, 23, 23, "W", "Yankton", SD
```
## Requirements
* Python
## DISCLAMER:
**I am not responsible for damaging any important data with this script.**
