import requests, os, spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init(autoreset=True)

# ========================== SETUP ==========================

# Load Spotify credentials from environment variables
spotify_client_id = os.environ["SPOTIFY_BILLBOARD_CLIENT_ID"]
spotify_secret = os.environ["SPOTIFY_BILLBOARD_CLIENT_SECRET"]
spotify_redirect_url = "https://www.google.com/"

# Billboard Hot 100 base URL
URL = "https://www.billboard.com/charts/hot-100/"
# Spoofing user agent for web scraping
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

songs = []        # List of song titles from Billboard
songs_uris = []   # List of corresponding Spotify track URIs

# ========================== USER INPUT ==========================

# Ask user for a specific date to fetch chart data
print(f"\n{Fore.BLUE}{'🎵 Welcome to the Billboard Time Machine 🎵'}{Style.RESET_ALL}")
print("Enter a date to travel back and fetch the Billboard Hot 100!")
date = input(Fore.YELLOW + "[Format: YYYY-MM-DD]: " + Style.RESET_ALL)
year = date.split("-")[0]

# ========================== WEB SCRAPING ==========================

# Display chart title
print(f"\n{Fore.CYAN}{'='*60}")
print(f"{'🎶 Top 100 Songs from Billboard – ' + year:^60}")
print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")

# Fetch and parse the Billboard chart page
response = requests.get(url=f"{URL}{date}/", headers=header)
hot_billboard_site = response.text
soup = BeautifulSoup(hot_billboard_site, "html.parser")

# Extract song titles (limited to elements with 'a-no-trucate' class)
for song in soup.find_all(name="h3", class_="a-no-trucate"):
    songs.append(song.getText().strip())

# Preview the first 10 songs in terminal
for i, song in enumerate(songs[:10], 1):
    print(f"{i:>3}. {song}")
if len(songs) > 10:
    print(f"... and {len(songs) - 10} more songs.\n")

# ========================== SPOTIFY AUTH ==========================

# Authenticate with Spotify using spotipy
spot = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=spotify_redirect_url,
        client_id=spotify_client_id,
        client_secret=spotify_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Get current user's Spotify ID
user = spot.current_user()["id"]

# ========================== FIND SONGS ON SPOTIFY ==========================

# Inform user that Spotify search is in progress
print(f"\n{Fore.MAGENTA}{'='*60}")
print(f"{'🔍 Searching for Songs on Spotify':^60}")
print(f"{Fore.MAGENTA}{'='*60}{Style.RESET_ALL}")

# Search each song on Spotify by title and year
for song in songs:
    track = spot.search(q=f"track: {song} year: {year}", limit=1, type="track", offset=0)
    try:
        # Get the first matching track's URI
        track_uri = track["tracks"]["items"][0]["uri"]
        songs_uris.append(track_uri)
        print(f"{Fore.GREEN}✔ {song} {Style.DIM}-> {track_uri}")
    except IndexError:
        # Skip if song is not found on Spotify
        print(f"{Fore.RED}✘ {song} {Style.DIM}not found on Spotify. Skipped.")

# ========================== CREATE PLAYLIST ==========================

# Create new private playlist in the user's Spotify account
playlist = spot.user_playlist_create(
    user=user,
    name=f"100 Best Songs of {year}",
    public=False,
    collaborative=False,
    description="Playlist auto-generated using Python."
)

# Add all found songs to the new playlist
spot.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)

# ========================== DONE ==========================

# Final success message with playlist link
print(f"\n{'='*60}")
print(f"{'🎧 Playlist Created Successfully!':^60}")
print(f"{f'🎼 100 Best Songs of {year}':^60}")
print(f"{'='*60}{Style.RESET_ALL}")
print(f"{Fore.YELLOW}🎵 Playlist URL: {playlist['external_urls']['spotify']}")
