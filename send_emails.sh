#!/bin/bash

# Email sending script with temporary credentials
# Note: This script will delete itself after execution for security

# Set temporary variables for email credentials
GMAIL_USER="rpggamer@gmail.com"
GMAIL_PASS="Thetruth54321"

# Read email content
EMAIL_CONTENT=$(cat "/Users/amre/Coding/LBBook/Email/email.md")

# Send emails to each recipient
while read -r recipient; do
    echo "Sending to: $recipient"
    
    # Using sendemail tool (must be installed)
    sendemail -f "$GMAIL_USER" \
              -t "$recipient" \
              -u "Epstein's Contact List Copy" \
              -m "$EMAIL_CONTENT" \
              -s smtp.gmail.com:587 \
              -xu "$GMAIL_USER" \
              -xp "$GMAIL_PASS" \
              -o tls=yes
              
    sleep 2 # Rate limiting

done < "/Users/amre/Coding/LBBook/emails.txt"

# Clean up credentials from memory
unset GMAIL_USER
unset GMAIL_PASS

# Self-destruct script for security
rm -- "$0"

echo "Emails sent and script deleted for security"