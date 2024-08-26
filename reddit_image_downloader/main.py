import json
import praw
import requests
from zipfile import ZipFile
from requests.exceptions import RequestException
from praw.exceptions import APIException, ClientException
import re
from .spinner import Spinner
from tqdm import tqdm
import shutil

def load_config():
    """Load configuration from config.json."""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: config.json file not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: config.json is not a valid JSON file.")
        exit(1)

def extract_post_id(post_url):
    """Extract post ID from Reddit URL."""
    match = re.search(r'/r/[^/]+/comments/([a-zA-Z0-9_]+)', post_url)
    if match:
        return match.group(1)
    else:
        print("Error: Unable to extract post ID from URL.")
        return None

def contains_images(comment):
    """Check if the comment contains image URLs."""
    return any(url.startswith('https://preview.redd.it/') for url in comment.body.split())

def process_comment(comment, zipf):
    """Process an individual comment, handling images and recursion."""
    if isinstance(comment, praw.models.Comment):
        if contains_images(comment):
            # Find all image URLs in the comment
            image_urls = [url for url in comment.body.split() if url.startswith('https://preview.redd.it/')]
            
            for image_url in image_urls:
                try:
                    # Download and save each image
                    response = requests.get(image_url)
                    response.raise_for_status()  # Check for HTTP errors
                    
                    # Ensure proper file extension
                    content_type = response.headers.get('Content-Type', '')
                    if 'jpeg' in content_type:
                        image_ext = '.jpeg'
                    elif 'png' in content_type:
                        image_ext = '.png'
                    else:
                        image_ext = '.jpg'  # Default fallback

                    image_name = f"{image_url.split('/')[-1].split('?')[0]}{image_ext}"
                    
                    # Add image to ZIP file
                    zipf.writestr(image_name, response.content)

                except RequestException as e:
                    print(f"Failed to download image from {image_url}. Error: {e}")
        
        # Recursively process replies
        for reply in comment.replies:
            process_comment(reply, zipf)

def download_images_from_post(post_url, output_zip, config):
    """Download images from Reddit comments and save them into a ZIP file."""
    post_id = extract_post_id(post_url)
    if not post_id:
        return

    try:
        # Initialize Reddit API with credentials from config
        reddit = praw.Reddit(
            client_id=config['REDDIT_CLIENT_ID'],
            client_secret=config['REDDIT_SECRET'],
            user_agent=config['REDDIT_USER_AGENT']
        )
        
        # Get Reddit post
        submission = reddit.submission(id=post_id)
        print(f"Fetched post: {submission.title}")
        print(f"Fetched Author: u/{submission.author.name}")
        print(f"Subreddit Name: r/{submission.subreddit.display_name}")
        print(f"Post Content: \n{submission.selftext}")

        if not submission:
            print(f"Error: Submission with ID {post_id} not found.")
            return
        
        # Flatten the comment tree to handle all comments
        submission.comments.replace_more(limit=None)  # Fetch all comments

        # Collect all comments to process
        comments_list = list(submission.comments.list())
        num_images = 0
        image_urls = []
        for comment in comments_list:
            if contains_images(comment):
                image_urls.extend([url for url in comment.body.split() if url.startswith('https://preview.redd.it/')])

        num_images = len(image_urls)
        
        if num_images == 0:
            print("No images found in comments.")
            return

        # Create ZIP file and start overall progress bar
        with ZipFile(output_zip, 'w') as zipf:
            # Start the spinner
            spinner = Spinner(message="Downloading images")
            spinner.start()
            
            # Clear console screen size
            terminal_size = shutil.get_terminal_size().lines
            progress_desc = "Downloading images"
            
            with tqdm(total=num_images, desc=progress_desc, unit="image", dynamic_ncols=True) as pbar:
                for image_url in image_urls:
                    try:
                        # Download and save each image
                        response = requests.get(image_url)
                        response.raise_for_status()  # Check for HTTP errors
                        
                        # Ensure proper file extension
                        content_type = response.headers.get('Content-Type', '')
                        if 'jpeg' in content_type:
                            image_ext = '.jpeg'
                        elif 'png' in content_type:
                            image_ext = '.png'
                        else:
                            image_ext = '.jpg'  # Default fallback

                        image_name = f"{image_url.split('/')[-1].split('?')[0]}{image_ext}"
                        
                        # Add image to ZIP file
                        zipf.writestr(image_name, response.content)
                        pbar.update(1)  # Update progress bar
                        
                    except RequestException as e:
                        print(f"Failed to download image from {image_url}. Error: {e}")

            # Stop the spinner
            spinner.stop()
        
        # Print final completion message
        print(f"\nImages have been downloaded and saved to {output_zip}.")

    except (APIException, ClientException) as e:
        print(f"Reddit API error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
