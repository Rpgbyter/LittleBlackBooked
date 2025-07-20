import tkinter as tk
from tkinter import messagebox
import re

def search_book():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    
    if not name and not email and not phone:
        messagebox.showerror("Error", "Please enter name, email or phone number")
        return
    
    try:
        with open('Jeffrey_Epstein39s_Little_Black_Book_unredacted_djvu.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            
        results = []
        if name:
            name_matches = re.findall(fr'(?i){re.escape(name)}.*?(?:\n|$)', content)
            results.extend(name_matches)
            
        if email:
            email_matches = re.findall(fr'(?i){re.escape(email)}.*?(?:\n|$)', content)
            results.extend(email_matches)
            
        if phone:
            # Normalize phone input and handle different formats
            normalized_phone = re.sub(r'[^0-9]', '', phone)
            # Search for numbers with various separators and country codes
            phone_patterns = [
                re.escape(normalized_phone),  # Exact match
                f"{normalized_phone[:3]}[ .-]?{normalized_phone[3:6]}[ .-]?{normalized_phone[6:]}",  # US format
                f"1?[ .-]?{normalized_phone[:3]}[ .-]?{normalized_phone[3:6]}[ .-]?{normalized_phone[6:]}",  # Optional 1
                f"\\+?1?[ .-]?{normalized_phone[:3]}[ .-]?{normalized_phone[3:6]}[ .-]?{normalized_phone[6:]}"  # Optional +1
            ]
            
            phone_matches = []
            for pattern in phone_patterns:
                phone_matches.extend(re.findall(fr'(?i).*?{pattern}.*?(?:\n|$)', content))
            results.extend(phone_matches)
            
        if results:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Email results to: mailto:rpgbyter@gmail.com\n\n")
            result_text.insert(tk.END, "View more at: https://github.com/Byterleek\n\n")
            result_text.insert(tk.END, f"Found {len(results)} matches:\n\n")
            for i, match in enumerate(results, 1):
                result_text.insert(tk.END, f"{i}. {match.strip()}\n\n")
        else:
            messagebox.showinfo("No matches", "No entries found matching your search")
            
    except Exception as e:
        messagebox.showerror("Error", f"Failed to search: {str(e)}")

# Create main window
root = tk.Tk()
root.title("littleBlackBooked")
root.geometry("600x400")

# Input fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

tk.Label(root, text="Phone Number:").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

# Search button
search_btn = tk.Button(root, text="Search", command=search_book)
search_btn.pack(pady=10)

# Results display
tk.Label(root, text="Results:").pack()
result_text = tk.Text(root, wrap=tk.WORD)
result_text.pack(expand=True, fill=tk.BOTH)
result_text.insert(tk.END, "Email results to: mailto:rpgbyter@gmail.com\n\n")
result_text.insert(tk.END, "View more at: https://github.com/Byterleek\n\n")

def send_email():
    import webbrowser
    import urllib.parse
    
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    results = "\n".join(result_text.get(1.0, tk.END).split("\n")[3:]).strip()
    
    if not results.strip() or "No entries found" in results:
        messagebox.showerror("Error", "No search results to email")
        return
    
    subject = "Little Black Book Search Results"
    body = f"Search results for:\nName: {name}\nEmail: {email}\nPhone: {phone}\n\n{results}"
    
    mailto = f"mailto:rpgbyter@gmail.com?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
    webbrowser.open(mailto)

root.mainloop()