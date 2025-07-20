#!/bin/bash

# Email sending script with attachments
# Note: This script will delete itself after execution for security

# Set temporary variables for email credentials
GMAIL_USER="rpggamer@gmail.com"
# Use an App Password instead of your main Gmail password
# Generate one here: https://myaccount.google.com/apppasswords
GMAIL_PASS="your_app_password_here"

# Read email content
EMAIL_CONTENT=$(cat "/Users/amre/Coding/LBBook/Email/email.md")

# Temporary directory for attachments
TEMP_DIR=$(mktemp -d)
cp "/Users/amre/Coding/LBBook/LBBook/LittleBlackBooked_CLI.py" "$TEMP_DIR/LittleBlackBooked_CLI.py"
cp "/Users/amre/Coding/LBBook/LBBook/LittleBlackBooked.py" "$TEMP_DIR/LittleBlackBooked.py"

# Send emails to each recipient
while read -r recipient; do
    echo "Sending to: $recipient"
    
    # Using sendemail tool with attachments
    sendemail -f "$GMAIL_USER" \
              -t "$recipient" \
              -u "Epstein's Contact List Copy" \
              -m "$EMAIL_CONTENT" \
              -a "$TEMP_DIR/LittleBlackBooked_CLI.py" \
              -a "$TEMP_DIR/LittleBlackBooked.py" \
              -s smtp.gmail.com:587 \
              -xu "$GMAIL_USER" \
              -xp "$GMAIL_PASS" \
              -o tls=yes
              
    sleep 2 # Rate limiting

done < "/Users/amre/Coding/LBBook/emails.txt"

# Clean up
rm -rf "$TEMP_DIR"
unset GMAIL_USER
unset GMAIL_PASS

# Self-destruct script for security
rm -- "$0"

echo "Emails sent with attachments and script deleted for security"