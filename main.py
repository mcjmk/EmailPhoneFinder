#!/usr/bin/env python3
# Search for email addresses and phone numbers in the clipboard.
# Currently, only Polish phone number conventions are supported.

import sys
import re
import pyperclip

EMAIL_REGEX = re.compile(
    r"_*[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*_*"
)

# Polish conventions
PHONE_NUMBER_REGEX = r".*(?:\+?48)?(?:\s*\d{3}[\s-]*){3}.*"


def get_emails(string):
    return re.findall(EMAIL_REGEX, string)


def get_phone_numbers(string):
    return re.findall(PHONE_NUMBER_REGEX, string)


if __name__ == "__main__":

    try:
        text = str(pyperclip.paste())
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        sys.exit(1)

    get_phone_numbers(text)
    if emails := get_emails(text):
        print("EMAILS: ")
        for email in emails:
            print(email)

    if phone_numbers := get_phone_numbers(text):
        print("PHONE NUMBERS: ")
        for number in phone_numbers:
            print(number)
