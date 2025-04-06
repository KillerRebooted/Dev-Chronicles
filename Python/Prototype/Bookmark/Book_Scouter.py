import requests
import pycountry

def get_language_name(code):
    language = pycountry.languages.get(alpha_2=code)
    return language.name if language else "Unknown"

def get_book_details(search):

    def get_details(response):
        
        # If the input isn't an ISBN Number, redo search with input as a Book Name Query
        try:
            response["items"]
        except:
            return get_details(requests.get(f"https://www.googleapis.com/books/v1/volumes?q={search.replace(' ', '+')}").json())

        # Get useful details about the book from the response.json()

        titles = [book["volumeInfo"].get("title") for book in response["items"]]
        ids = [book["id"] for book in response["items"]]
        authors = [book["volumeInfo"].get("authors", "") for book in response["items"]]
        publishers = [book["volumeInfo"].get("publisher", "") for book in response["items"]]
        publish_dates = [book["volumeInfo"].get("publishedDate", "") for book in response["items"]]
        descriptions = [book["volumeInfo"].get("description", "") for book in response["items"]]
        page_counts = [book["volumeInfo"].get("pageCount", "") for book in response["items"]]
        categories = [book["volumeInfo"].get("categories", "") for book in response["items"]]
        maturity_ratings = ["Intended for a Mature Audience" if book["volumeInfo"].get("maturityRating", "")=="MATURE" else "Suitable for All Ages" for book in response["items"]]
        language = [get_language_name(book["volumeInfo"].get("language", "")) for book in response["items"]]
        thumbnails = [f"https://books.google.com/books/publisher/content/images/frontcover/{id}?fife=w1920-h1080&source=gbs_api" for id in ids]

        isbn10 = []
        isbn13 = []

        # Get ISBN Numbers from "items". If they don't exist, return ""
        for i in response["items"]:
            isbn10_value = ""
            isbn13_value = ""
            
            try:
                for j in i["volumeInfo"]["industryIdentifiers"]:
                    if j["type"] == "ISBN_10":
                        isbn10_value = j["identifier"]
                    if j["type"] == "ISBN_13":
                        isbn13_value = j["identifier"]

            except:
                pass
            
            isbn10.append(isbn10_value)
            isbn13.append(isbn13_value)

        books = []

        for i in range(len(titles)):

            books.append({"title":titles[i], "id":ids[i], "authors":", ".join(authors[i]), "publisher":publishers[i], "publish_date":publish_dates[i], "description":descriptions[i], "isbn10":isbn10[i], "isbn13":isbn13[i], "page_count":page_counts[i], "categories":", ".join(categories[i]), "maturity_rating":maturity_ratings[i], "language":language[i], "thumbnail":thumbnails[i]})

        return books

    # Get Search Results assuming input is an ISBN Number
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{search}").json()
    
    return get_details(response)

if __name__ == "__main__":
    
    print(get_book_details("9781974742943"))
    print(get_book_details("one punch man"))