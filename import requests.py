import requests
from bs4 import BeautifulSoup

def is_related_to_company(result, company_name):
    # Modify this function based on how you want to determine if the result is related to the company
    # For simplicity, we'll check if the company name appears in the result text
    return company_name.lower() in result.text.lower()

def scrape_company_phone_number(company_name):
    url = f"https://www.google.com/search?q={company_name}"

    headers = {
        'User-Agent': 'Your User Agent Here'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract search results
        search_results = soup.find_all('div', {'class': 'BNeawe vvjwJb AP7Wnd'})

        # Filter and extract phone numbers from relevant results
        relevant_phone_numbers = []
        for result in search_results:
            if is_related_to_company(result, company_name):
                phone_number = result.text.strip()
                relevant_phone_numbers.append(phone_number)

        return relevant_phone_numbers

    else:
        print("Error:", response.status_code)
        return None

if __name__ == "__main__":
    company_name = "Sarl Cakir"
    phone_numbers = scrape_company_phone_number(company_name)

    if phone_numbers:
        print("Relevant phone numbers:")
        for idx, phone_number in enumerate(phone_numbers, start=1):
            print(f"{idx}. {phone_number}")
    else:
        print("No relevant phone numbers found.")
