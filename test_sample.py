def calculate_rent(area, location, amenities):
    base_price = area * 50
    if location == "Koramangala":
        base_price *= 1.5
    return base_price + len(amenities) * 1000

def scrape_property_data(url, max_pages):
    results = []
    for page in range(max_pages):
        # scraping logic here
        pass
    return results
