# GeoGroove: UIUC Research Park Hackathon 2024

GeoGroove revolutionizes music discovery by allowing Spotify users to find new music from popular artists based on specific locations—all in just one click.

**Received Skillful Execution award for [UIRP hackathon](https://github.com/uirphack/2024/blob/master/README.md)**

![A demo of GeoGroove, featuring city selection, Spotify authentication, and seamless playlist creation.](./demo.gif)

## Problem Statement

As an avid music listener embarking on a road trip to Champaign, Illinois, you yearn to connect with artists who truly embody the spirit of this city. Music reflects the culture you’re surrounded by, and you want to find artists who authentically represent what it’s like to be from Champaign. However, existing platforms lack a feature that makes this possible. This is why we created GeoGroove.

## Solution

GeoGroove provides a seamless way for Spotify users to discover music from popular artists representing different locations. With GeoGroove, you can specify the location—whether it's the destination of your next vacation or an area you’ve always wanted to explore—and we will create a playlist of the most popular artists from that area.

### How It Works

1. **Specify Your Location**: Enter a list of desired locations into GeoGroove. This could be your next vacation destination or an area you’re interested in exploring musically.

2. **Extract Representative Artists**: We utilize the MusicBrainz Database to extract representative artists of different geographic locations using Python.

3. **Sort by Popularity**: We take a smaller sample of the data and use the Spotify API to sort these artists by Spotify's popularity metric, selecting top artists from each specified location.

4. **Fetch Popular Tracks**: Using the Spotify API, we fetch the most popular tracks of each of the selected artists.

5. **Create and Populate Playlist**: Log in to Spotify to authenticate and give us permission to create a playlist. GeoGroove will then create the playlist and add the new tracks from these artists to your Spotify account.

### Example Use Case

Imagine you are on a road trip to Champaign, Illinois. With GeoGroove, you can explore the music that embodies the local culture by discovering artists who started their careers or grew up in Champaign. This way, you can connect with the soul of the place through its music.

## Technical Implementation

### Data Sources

- **MusicBrainz API**: Used to extract representative artists of different geographic locations.
- **Spotify API**: Used to sort artists by popularity and fetch their most popular tracks.

### Steps

1. **Extract Artists Data**: 
    - Use MusicBrainz API to gather data on artists from specific locations.
    - Process this data using a Python script to filter and select relevant artists.

2. **Sort and Select Artists**:
    - Use the Spotify API to sort the selected artists by their popularity.
    - Select a subset of the top 10 artists from each specified location.

3. **Fetch Tracks and Create Playlist**:
    - Use the Spotify API to fetch the most popular tracks of the selected artists.
    - Authenticate the user with Spotify and create a new playlist.
    - Add the fetched tracks to the newly created playlist.


## Getting Started

### Prerequisites

Before you begin, ensure you have Docker installed on your system. You can download and install Docker from the [official Docker website](https://docs.docker.com/engine/install/).

### Setup and Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ekcom/COUNTRYmen.git
    cd COUNTRYmen
    ```

2. **Build and start the services**:
    ```sh
    docker-compose up -d
    ```

    This command will build the Docker images and start the frontend and backend services.

### Environment Variables

Ensure you have a `.env` file in your backend directory with the following content:

```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://localhost:8000/callback
```
