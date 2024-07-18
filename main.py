#!/usr/bin/env python3
# Search for email addresses and phone numbers in the clipboard.
# Currently, only Polish phone number conventions are supported.

import argparse
import sys
from regex_util import get_emails, get_phone_numbers
from clipboard_handler import clipboard_input, clipboard_output
from pdf_handler import pdf_input
from txt_handler import txt_input, txt_output
from url_handler import url_input


def parse_args():
    parser = argparse.ArgumentParser(
        description="Search email and phone number in given source"
    )
    parser.add_argument(
        "-i",
        "--input",
        default="clipboard",
        help="Specify the input type and value ex: 'clipboard', 'txt', 'console', 'url', 'pdf'",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="console",
        help="Specify the output type and value, ex.: 'clipboard', 'txt', 'console'",
    )
    return parser.parse_args()


def determine_type(s):
    if s in ["clipboard", "console"]:
        return s
    if s.endswith(".txt"):
        return "txt"
    if s.endswith(".pdf"):
        return "pdf"
    if s.startswith("http") or s.endswith(".com"):
        return "url"


def get_results(text):
    results = ""
    if emails := get_emails(text):
        print("EMAILS: ")
        results += f"EMAILS:\n"
        for email in emails:
            print(email)
            results += f"{email}\n"

    if phone_numbers := get_phone_numbers(text):
        print("PHONE NUMBERS: ")
        results += "\nPHONE NUMBERS:\n"
        for number in phone_numbers:
            print(number)
            results += f"{number}\n"

    return results


def get_text(args):
    input_type = determine_type(args.input)
    match input_type:
        case "clipboard":
            return clipboard_input()
        case "txt":
            return txt_input(args.input)
        case "url":
            return url_input(args.input)
        case "pdf":
            return pdf_input(args.input)
        case _:
            sys.exit("Error, unsupported type!")


def handle_output(args, results):
    output_type = determine_type(args.output)
    match output_type:
        case "clipboard":
            clipboard_output(results)
        case "txt":
            txt_output(results, args.output)


def main():
    args = parse_args()
    text = get_text(args)
    results = get_results(text)
    handle_output(args, results)


if __name__ == "__main__":
    main()
