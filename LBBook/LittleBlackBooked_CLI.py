import re
def search_book(name='', email='', phone='', output_format='text'):
    try:
        with open('Jeffrey_Epstein39s_Little_Black_Book_unredacted_djvu.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            
        results = []
        if name:
            name_matches = re.findall(fr'(?i){re.escape(name)}.*?(?:
|$)', content)
            results.extend(name_matches)
        if email:
            email_matches = re.findall(fr'(?i){re.escape(email)}.*?(?:
|$)', content)
            results.extend(email_matches)
        if phone:
            normalized_phone = re.sub(r'[^0-9]', '', phone)
            phone_patterns = [
                re.escape(normalized_phone),
                f"{normalized_phone[:3]}[ .-]?{normalized_phone[3:6]}[ .-]?{normalized_phone[6:]}",
                f"1?[ .-]?{normalized_phone[:3]}[ .-]?{normalized_phone[3:6]}[ .-]?{normalized_phone[6:]}",
                f"\+?1?[ .-]?{normalized_phone[:3]}[ .-]?{normalized_phone[3:6]}[ .-]?{normalized_phone[6:]}"
            ]
            phone_matches = []
            for pattern in phone_patterns:
                phone_matches.extend(re.findall(fr'(?i).*?{pattern}.*?(?:
|$)', content))
            results.extend(phone_matches)
            
        if output_format == 'json':
            return {
                'results': results,
                'count': len(results),
                'email': 'mailto:rpgbyter@gmail.com',
                'github': 'https://github.com/Byterleek'
            }
        else:
            output = "Email results to: mailto:rpgbyter@gmail.com\n"
            output += "View more at: https://github.com/Byterleek\n\n"
            output += f"Found {len(results)} matches:\n\n"
            for i, match in enumerate(results, 1):
                output += f"{i}. {match.strip()}\n\n"
            return output
            
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='littleBlackBooked')
    parser.add_argument('--name', help='Name to search', default='')
    parser.add_argument('--email', help='Email to search', default='')
    parser.add_argument('--phone', help='Phone to search', default='')
    parser.add_argument('--json', help='JSON output', action='store_true')
    args = parser.parse_args()
    
    result = search_book(args.name, args.email, args.phone, 'json' if args.json else 'text')
    print(result)