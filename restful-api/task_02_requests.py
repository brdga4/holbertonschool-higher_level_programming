import csv
import requests

api_url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints out the titles.
    Uses a guard clause to stop early if the network call fails.
    """
    response = requests.get(api_url)
    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    posts = response.json()
    for post in posts:
        print(post["title"])


def fetch_and_save_posts():
    """
    Fetches posts, parses out id, title, and body fields,
    and serializes the structured data directly into a CSV file.
    """
    response = requests.get(api_url)

    if response.status_code != 200:
        return

    posts = response.json()
    filtered_posts = []

    for post in posts:
        clean_dictionary = {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"],
        }
        filtered_posts.append(clean_dictionary)

    fieldnames = ["id", "title", "body"]

    with open("posts.csv", mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_posts)
