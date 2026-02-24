# Problem 12: Validate IPv4 Address and Identify Famous DNS

## Problem
Write a function that checks if a given string is a valid IPv4 address.  
Additionally, if the IP matches a well‑known public DNS server, the function should identify it.

**Expected behavior:**
- If the IP is found in the `FAMOUS_DNS` dictionary, return the name of the DNS server (a string).
- Otherwise, validate the IP format:
  - Must have exactly four octets separated by dots.
  - Each octet must be an integer between 0 and 255 inclusive.
  - If valid, return `True`; if invalid, return `False`.

---

## My Solution

I wrote a function `ip_check(ip)` that first checks a predefined dictionary of famous DNS servers. If the IP is present, it immediately returns the server name. If not, it proceeds to validate the IPv4 format.
