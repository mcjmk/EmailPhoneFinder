# EmailPhoneFinder.py 
## Description
This simple python script allows you to quickly find email addresses and phone numbers in the source you provide.
No more need to look for them with your own eyes, let's let regular expressions do magic! :)

*Currently, the script is set to recognize only phone numbers following Polish conventions*

## Features
- Input formats: clipboard(default), txt, pdf, url
- Search for emails and phone numbers in your input
- Output formats: console(default), clipboard, txt 


## How to run
### Prerequisites
- Python 3.6 or newer

### Example
```sh
    python main.py -i input.txt -o result.txt
    python main.py -i https://en.wikipedia.org/wiki/Telephone_number -o numbers.txt
```


## Future Enhancements:
- [x] Add more options of output
- [ ] Add support for more phone numbers formats
- [ ] Develop a more user-friendly GUI.
- [ ] Enhance support for PDF
