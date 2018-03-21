"""
Sabah Siddique
CSCI-UA 60 Assignment 5 - Python CGI

This program scrubs the data set found from the link below.
Data source: https://www.kaggle.com/thec03u5/fifa-18-demo-player-dataset
"""

import unicodedata


"""
Scrub the data set
"""
def scrub():
    
    # Source and target file names
    s_name = "fifa_data.csv"
    t_name = s_name[:-4] + "_out.csv"

    try:
        s = open(s_name, "r")   ## open source file in read mode
    except:
        print("Error opening file!")
    else:
        t = open(t_name, "w")   ## open target file in write mode

        # Parse through source file
        for line in s:

            # Include only rows with one of the following three club names in them
            if "Spanish Primera División" in line or "English Premier League" in line or "Italian Serie A" in line:
                
                # Pass line to replace_char()
                #line = replace_char(line)
                

                # Store the data to be written to target file
                new_line = ""
                # Store data in the current line in a list
                values = line.split(",")

                # Based on my requirements, the following indices are  to be written to target file
                include = [1, 2, 3, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
            
                for i in range(len(values)):
                    # Omit the specified indices
                    if i not in include:
                        continue
                    else:
                        # Append the data to new_line
                        new_line += values[i] + ","

                # Strip accents from new_line
                new_line = strip_accents(new_line)
                print(new_line)

                # Remove the trailing tab character, add newline character
                new_line = new_line.rstrip(",") + "\n"
                # Write new_line to target file
                t.write(new_line)


"""
Strip accents from the given string
"""
def strip_accents(new_line):
    # Try converting string to unicode
    try:
        new_line = unicode(new_line, 'utf-8')
    except (TypeError, NameError):
        pass
    new_line = unicodedata.normalize('NFD', new_line)
    new_line = new_line.encode('ascii', 'ignore')
    new_line = new_line.decode("utf-8")
    return str(new_line)


scrub()