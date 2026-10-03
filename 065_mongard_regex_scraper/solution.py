"""
Problem #65: Scrape Mongard Courses with Regex
Date: 2026-10-03

Fetch the Mongard courses page and extract each course's slug and price
using a single compiled regular expression with named groups.
"""

import re
import requests

url = "https://www.mongard.ir/courses/"

regex = re.compile(
    r'<div class="card-body">.*?href="/courses/(?P<course>[^/]+)/".*?</div>.*?<div class="card-footer.*?<b><span>\s*(?P<price>.*?)\s*</span>',
    re.DOTALL | re.IGNORECASE
)

response = requests.get(url)
html = response.text

for match in regex.finditer(html):
    print(match.group("course"), "=>", match.group("price"))