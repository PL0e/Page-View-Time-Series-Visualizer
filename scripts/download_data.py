import urllib.request
from pathlib import Path

def download_fcc_data():
    """
    Download the freeCodeCamp forum page views dataset.
    """
    url = "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/master/fcc-forum-pageviews.csv"
    filename = "fcc-forum-pageviews.csv"
    
    print(f"[v0] Downloading data from {url}...")
    
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"[v0] Successfully downloaded '{filename}'")
        
        # Verify the file
        file_path = Path(filename)
        if file_path.exists():
            file_size = file_path.stat().st_size
            print(f"[v0] File size: {file_size:,} bytes")
        
    except Exception as e:
        print(f"[v0] Error downloading file: {e}")

if __name__ == "__main__":
    download_fcc_data()
