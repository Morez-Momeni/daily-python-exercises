# Problem 63: Secure Token Generator (Bottle Web App)

## Problem
Build a tiny web application that generates a **cryptographically secure URL-safe token** on every page load and displays it in a modern, styled HTML page.

## My Solution

I used the **Bottle** micro-framework to define a single route (`/`) and Python's built-in `secrets` module to generate the token.