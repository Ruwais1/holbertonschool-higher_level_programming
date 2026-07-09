import requests
import csv


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder API and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print("Status Code: {}".format(response.status_code))
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches posts and saves their id, title, and body to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data into a list of dictionaries
        structured_data = [
            {'id': post.get('id'), 'title': post.get('title'), 'body': post.get('body')}
            for post in posts
        ]
        
        # Write the structured data to a CSV file
        with open("posts.csv", "w", encoding="utf-8", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_data)
