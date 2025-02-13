Brute-Force Login Script for Pluck CMS
=======================================

Description:
-------------
This Python script attempts to brute-force the login page of a Pluck CMS website. It reads potential passwords from a provided wordlist and submits them to the login form. The script specifically targets a form that requires three fields:
  - 'cont1': The password field.
  - 'bogus': A hidden honeypot field (must remain empty).
  - 'submit': The submit button value ('Log in').

The script considers the login successful if the login form is no longer present in the response HTML.

Requirements:
-------------
- Python 3.x
- The 'requests' library (Install via pip: `pip install requests`)
- A wordlist file containing potential passwords

Usage:
------
To run the script, use the following syntax:

    ./script.py <url> -wordlist <wordlist_path>

Where:
  - `<url>` is the target login URL.
  - `<wordlist_path>` is the path to your wordlist file.

Example:
--------
If your target URL is `http://example.com/login` and your wordlist is at `/home/user/wordlist.txt`, you would run:

    ./script.py http://example.com/login -wordlist /home/user/wordlist.txt

Additional Information:
-----------------------
- The script initiates a session and makes an initial GET request to capture any necessary cookies.
- It pauses for 30 seconds after every three failed attempts to help avoid triggering lockouts.
- Debug information is printed to the console for each attempt, including the response URL, history, and session cookies.

Author:
-------
alienfader

Disclaimer:
-----------
This script is intended for educational purposes and authorized security testing only. Ensure you have explicit permission before testing any website.
