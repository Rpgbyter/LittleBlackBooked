from flask import Flask, request, jsonify
import re

app = Flask("littleBlackBooked")

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    
    try:
        with open('/Users/amre/Coding/LBBook/LBBook/Jeffrey_Epstein39s_Little_Black_Book_unredacted_djvu.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            
        results = []
        if name:
            name_pattern = f'(?i){re.escape(name)}.*?(?:\n|$)'
            name_matches = re.findall(name_pattern, content)
            results.extend(name_matches)
        if email:
            email_pattern = f'(?i){re.escape(email)}.*?(?:\n|$)'
            email_matches = re.findall(email_pattern, content)
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
                phone_pattern = f'(?i).*?{pattern}.*?(?:\n|$)'
                phone_matches.extend(re.findall(phone_pattern, content))
            results.extend(phone_matches)
            
        return jsonify({
            'results': results,
            'count': len(results),
            'email': 'mailto:rpgbyter@gmail.com',
            'github': 'https://github.com/Byterleek'
        })
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return app.send_static_file('LittleBlackBooked_HTML.html')

if __name__ == '__main__':
    app.run(debug=True)