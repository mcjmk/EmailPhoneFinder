#! python3
# EmailPhoneScraper.py - this script searches for email addresses and phone numbers in the clipboard content,
# extract them using regular expressions, and copies the results back to the clipboard.
# Currently, the script is set to recognize phone numbers following Polish conventions.

import sys
import pyperclip
import re

if __name__ == '__main__':

    try:
        text = str(pyperclip.paste())
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        sys.exit(1)

    emailRegex = re.compile(r'''
        ([a-zA-Z0-9._%+=-]+)  # username
        (@)                   # @ symbol
        ([a-zA-Z0-9-.]+)       # domain 
        (\.[a-zA-Z0-9]+)+        # dot-something 
        ''', re.VERBOSE)

    # Polish conventions
    numbersRegex = re.compile(r'''
        # mobile phone
        (\d{3})            # 3 digits
        ([\s-])?           # optional separator 
        (\d{3})            # 3 digits
        ([\s-])?           # optional separator 
        (\d{3})            # 3 digits 

        |                  # alternative 

        # landline phone
        (\d{2}|\(\d{2}\))?    # area code - 2 digits
        ([\s-])?              # optional separator 
        (\d{3})               # 3 digits
        ([\s-])?               # optional separator   
        (\d{2})               # 2 digits
        ([\s-])?               # optional separator  
        (\d{2})               # 2 digits  
        ''', re.VERBOSE)

    resultEmails = "\n".join("".join(email) for email in emailRegex.findall(text))
    resultNumbers = "\n".join("".join(number) for number in numbersRegex.findall(text))

    results = []
    if resultEmails:
        results.append(resultEmails)

    if resultNumbers:
        results.append(resultNumbers)

    result = "\n".join(results)

    if not result:
        print("No email addresses or phone numbers were found.")

    else:
        pyperclip.copy(result)
        print(f"Found and copied to clipboard:\n{result}")
