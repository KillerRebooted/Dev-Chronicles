import requests

def get_book_details(search):

    def get_details(response):

        try:
            response["items"]
        except:
            return get_details(requests.get(f"https://www.googleapis.com/books/v1/volumes?q={search.replace(' ', '+')}").json())

        titles = [book["volumeInfo"].get("title") for book in response["items"]]
        ids = [book["id"] for book in response["items"]]
        authors = [book["volumeInfo"].get("authors", "") for book in response["items"]]
        publishers = [book["volumeInfo"].get("publisher", "") for book in response["items"]]
        publish_dates = [book["volumeInfo"].get("publishedDate", "") for book in response["items"]]
        descriptions = [book["volumeInfo"].get("description", "") for book in response["items"]]

        isbn10 = []
        isbn13 = []

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

        page_counts = [book["volumeInfo"].get("pageCount", "") for book in response["items"]]
        categories = [", ".join(book["volumeInfo"].get("categories", "")) for book in response["items"]]
        maturity_ratings = ["Inappropriate for certain Ages" if book["volumeInfo"].get("maturityRating", "")=="NOT_MATURE" else "Appropriate for all Ages" for book in response["items"]]
        thumbnails = [f"https://books.google.com/books/publisher/content/images/frontcover/{id}?fife=w1920-h1080&source=gbs_api" for id in ids]

        books = []

        for i in range(len(titles)):

            books.append({"title":titles[i], "id":ids[i], "authors":", ".join(authors[i]), "publisher":publishers[i], "publish_date":publish_dates[i], "description":descriptions[i], "isbn10":isbn10[i], "isbn13":isbn13[i], "page_count":page_counts[i], "categories":categories[i], "maturity_rating":maturity_ratings[i], "thumbnail":thumbnails[i]})

        return books

    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{search}").json()
    
    return get_details(response)

if __name__ == "__main__":
    print(get_book_details("9781974742943"))
    
    print(get_book_details("one punch man"))