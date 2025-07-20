// Java version of LittleBlackBooked
// Contact: rpgbyter@gmail.com
// GitHub: https://github.com/Byterleek

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class LittleBlackBooked {
    private String filePath;

    public LittleBlackBooked(String filePath) {
        this.filePath = filePath;
    }

    public List<String> search(String name, String email, String phone) throws IOException {
        if (name == null && email == null && phone == null) {
            throw new IllegalArgumentException("Please enter name, email or phone number");
        }

        String content = new String(Files.readAllBytes(Paths.get(filePath)));
        List<String> results = new ArrayList<>();

        if (name != null && !name.isEmpty()) {
            Pattern namePattern = Pattern.compile(Pattern.quote(name) + ".*?(?:\\n|$)", Pattern.CASE_INSENSITIVE);
            Matcher nameMatcher = namePattern.matcher(content);
            while (nameMatcher.find()) {
                results.add(nameMatcher.group().trim());
            }
        }

        if (email != null && !email.isEmpty()) {
            Pattern emailPattern = Pattern.compile(Pattern.quote(email) + ".*?(?:\\n|$)", Pattern.CASE_INSENSITIVE);
            Matcher emailMatcher = emailPattern.matcher(content);
            while (emailMatcher.find()) {
                results.add(emailMatcher.group().trim());
            }
        }

        if (phone != null && !phone.isEmpty()) {
            String normalizedPhone = phone.replaceAll("[^0-9]", "");
            String[] phonePatterns = {
                Pattern.quote(normalizedPhone),
                normalizedPhone.substring(0, 3) + "[ .-]?" + normalizedPhone.substring(3, 6) + "[ .-]?" + normalizedPhone.substring(6),
                "1?[ .-]?" + normalizedPhone.substring(0, 3) + "[ .-]?" + normalizedPhone.substring(3, 6) + "[ .-]?" + normalizedPhone.substring(6),
                "\\+?1?[ .-]?" + normalizedPhone.substring(0, 3) + "[ .-]?" + normalizedPhone.substring(3, 6) + "[ .-]?" + normalizedPhone.substring(6)
            };

            for (String pattern : phonePatterns) {
                Pattern phonePattern = Pattern.compile(".*?" + pattern + ".*?(?:\\n|$)", Pattern.CASE_INSENSITIVE);
                Matcher phoneMatcher = phonePattern.matcher(content);
                while (phoneMatcher.find()) {
                    results.add(phoneMatcher.group().trim());
                }
            }
        }

        return results;
    }

    public static void main(String[] args) {
        try {
            LittleBlackBooked book = new LittleBlackBooked("Jeffrey_Epstein39s_Little_Black_Book_unredacted_djvu.txt");
            List<String> results = book.search("John", "example@email.com", "1234567890");
            System.out.println("Found " + results.size() + " matches:");
            for (int i = 0; i < results.size(); i++) {
                System.out.println((i + 1) + ". " + results.get(i));
            }
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}