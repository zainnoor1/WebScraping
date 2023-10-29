import re

# Regex pattern for matching website URLs with optional "www" and various TLDs
website_regex = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]+?\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*)?'

# Test the regex pattern with a sample text
text = "Visit our website at https://www.sarlcakir.fr/ or https://www.facebook.com/CakirSARL/, or just example.org"
websites = re.findall(website_regex, text)

# List of company names or keywords to match against
company_names = ["Sarl", "cakir1", "sarl cakir1", "sarlcakir1", "ltd"]

# Function to determine if a website URL matches a company name
def matches_company_name(website, names):
    website_lower = website.lower()
    for name in names:
         if name.lower() in website_lower:
            return True
    return False

# Filter websites that match a company name
filtered_websites = [website for website in websites if matches_company_name(website, company_names)]

# Print the matched websites
for website in filtered_websites:
    print(website)
