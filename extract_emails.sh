#!/bin/bash

# Extract emails from Jeffrey Epstein's contact list
grep -E -o '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' /Users/amre/Coding/LBBook/LBBook/Jeffrey_Epstein39s_Little_Black_Book_unredacted_djvu.txt | sort | uniq > /Users/amre/Coding/LBBook/emails.txt

echo "Emails extracted to emails.txt"