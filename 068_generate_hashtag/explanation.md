# Problem 68: Generate Hashtag

## Problem
Write a function `generate_hashtag(phrase)` that converts a phrase into a hashtag:
- Remove leading/trailing spaces.
- Capitalize the first letter of each word (Title Case).
- Remove all spaces.
- Prepend a `#`.
- If the result is longer than 140 characters or is just `#` (empty phrase), return `"false"`.

**Examples:**
- `"    hello     world   "` → `"#HelloWorld"`
- `""` → `"false"`
- `"Python is great"` → `"#PythonIsGreat"`
- `"Do We have a Hashtag"` → `"#DoWeHaveAHashtag"`