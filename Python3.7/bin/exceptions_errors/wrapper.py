def wrap(text, line_length):
    """Wrap a string to a specified line length.

    Args:
        text: The string to wrap.
        line_length: The line length in characters.

    Returns:
        ValueError: If line_length is not positive.
    """
    if line_length < 1:
        raise ValueError("line_length {} is not positive".format(line_length))

    words = text.split()

    if max(map(len, words)) > line_length:
        raise ValueError("line_length must be at least as long as the longest word")

    lines_of_words = []
    current_line_length = line_length
    for word in words:
        if current_line_length + len(word) > line_length:
            lines_of_words.append([])  # new line
            current_line_length = 0
        lines_of_words[-1].append(word)
        current_line_length += len(word) + len(' ')
    lines = [' '.join(line_of_words) for line_of_words in lines_of_words]
    result = '\n'.join(lines)
    assert all(len(line) <= line_length for line in result.splitlines())
    return result

wealth_of_nations = "adsadsa dsa ds ad sad sadsadsa dsadsa dsa dsa dsa dsadd" \
"asdasdsads dsa dsa dsa dsa dsa dsa dsaddddddddddddddd dsadsa dsa dsa dsa ds" \
"dddddddd ddddddddddd ssssssssss aaaaaaaaa sssssss ddddd sdasd ssssssssss s."


if __name__ == "__main__":
    print(wrap(wealth_of_nations, 18))
    # Will generate the error
    # wrap('asd as dsa  ds ds ds a sssssssssssssssssdddddddddddddddddddadadasdasdasdsadsadas ds s d123 213', 25)
