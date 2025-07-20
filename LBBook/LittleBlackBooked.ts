// TypeScript version of LittleBlackBooked
// Contact: rpgbyter@gmail.com
// GitHub: https://github.com/Byterleek

interface SearchResult {
  index: number;
  content: string;
}

class LittleBlackBooked {
  private readonly filePath: string;
  
  constructor(filePath: string) {
    this.filePath = filePath;
  }

  async search(name?: string, email?: string, phone?: string): Promise<SearchResult[]> {
    if (!name && !email && !phone) {
      throw new Error("Please enter name, email or phone number");
    }

    try {
      const fs = await import('fs/promises');
      const content = await fs.readFile(this.filePath, 'utf-8');
      
      const results: SearchResult[] = [];
      
      if (name) {
        const nameRegex = new RegExp(`${this.escapeRegex(name)}.*?(?:\n|$)`, 'gi');
        const nameMatches = [...content.matchAll(nameRegex)];
        nameMatches.forEach((match, i) => {
          results.push({ index: i + 1, content: match[0].trim() });
        });
      }
      
      if (email) {
        const emailRegex = new RegExp(`${this.escapeRegex(email)}.*?(?:\n|$)`, 'gi');
        const emailMatches = [...content.matchAll(emailRegex)];
        emailMatches.forEach((match, i) => {
          results.push({ index: i + 1, content: match[0].trim() });
        });
      }
      
      if (phone) {
        const normalizedPhone = phone.replace(/[^0-9]/g, '');
        const phonePatterns = [
          this.escapeRegex(normalizedPhone),
          `${normalizedPhone.substring(0, 3)}[ .-]?${normalizedPhone.substring(3, 6)}[ .-]?${normalizedPhone.substring(6)}`,
          `1?[ .-]?${normalizedPhone.substring(0, 3)}[ .-]?${normalizedPhone.substring(3, 6)}[ .-]?${normalizedPhone.substring(6)}`,
          `\\+?1?[ .-]?${normalizedPhone.substring(0, 3)}[ .-]?${normalizedPhone.substring(3, 6)}[ .-]?${normalizedPhone.substring(6)}`
        ];
        
        phonePatterns.forEach(pattern => {
          const phoneRegex = new RegExp(`.*?${pattern}.*?(?:\n|$)`, 'gi');
          const phoneMatches = [...content.matchAll(phoneRegex)];
          phoneMatches.forEach((match, i) => {
            results.push({ index: i + 1, content: match[0].trim() });
          });
        });
      }
      
      return results;
    } catch (error) {
      throw new Error(`Failed to search: ${error instanceof Error ? error.message : String(error)}`);
    }
  }
  
  private escapeRegex(str: string): string {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }
}

// Example usage
// const book = new LittleBlackBooked('Jeffrey_Epstein39s_Little_Black_Book_unredacted_djvu.txt');
// book.search('John', 'example@email.com', '1234567890')
//   .then(results => console.log(results))
//   .catch(error => console.error(error));