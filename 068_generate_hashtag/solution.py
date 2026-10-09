def generate_hashtag(phrase: str):
    if not phrase:
        return "false"
    res = phrase.strip().title()
    res = res.replace(" ", "")
    res = '#' + res
    if len(res) > 140 or len(res) == 1:
        return "false"

    elif not res:
        return "false"
    else:
        return res


if __name__ == "__main__":
    test = [
        ("    hello     world   ", "#HelloWorld"),
        ("", "false"),
        ("Python is great", "#PythonIsGreat"),
        ("Do We have a Hashtag", "#DoWeHaveAHashtag"),
    ]

    for Input, expected in test:
        result = generate_hashtag(Input)
        if result == expected:
            print(f"[PASS] Input: {Input} , result: {result} , expected: {expected}")
        else:
            print(f"[FAILED] Input: {Input} , result: {result} , expected: {expected}")