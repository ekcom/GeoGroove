# COUNTRYmen: UIUC Research Park Hackathon 2024

This repository contains the project "COUNTRYmen" developed for the UIUC Research Park Hackathon 2024. The project includes a frontend and backend service to search for artists from a specific city using the Spotify API.

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

CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REDIRECT_URI=http://localhost:8000/callback

