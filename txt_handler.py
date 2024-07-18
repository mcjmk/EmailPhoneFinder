def txt_input(filename):
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
    return text


def txt_output(results, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(results)
