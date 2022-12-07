def get_formatted_name(first, last, middle=""):
    return f"{first.title()} {middle.title()} {last.title()}" if middle else f"{first.title()} {last.title()}"

