const express = require('express');
const axios = require('axios');
const querystring = require('querystring');
require('dotenv').config();
const app = express();

// Load environment variables from .env file
const client_id = process.env.CLIENT_ID; // Your Spotify client ID
const client_secret = process.env.CLIENT_SECRET; // Your Spotify client secret
const redirect_uri = process.env.REDIRECT_URI; // Your redirect URI

// Endpoint to initiate login and authorization process
app.get('/login', (req, res) => {
    const scope = 'playlist-modify-public playlist-modify-private'; // Scopes for playlist modification
    // Redirect to Spotify's authorization page
    res.redirect('https://accounts.spotify.com/authorize?' +
        querystring.stringify({
            response_type: 'code',
            client_id: client_id,
            scope: scope,
            redirect_uri: redirect_uri
        }));
});

// Callback endpoint for Spotify to redirect to after authorization
app.get('/callback', async (req, res) => {
    const code = req.query.code || null; // Get authorization code from query parameters
    const authOptions = {
        url: 'https://accounts.spotify.com/api/token',
        data: querystring.stringify({
            code: code,
            redirect_uri: redirect_uri,
            grant_type: 'authorization_code'
        }),
        headers: {
            'Authorization': 'Basic ' + (Buffer.from(client_id + ':' + client_secret).toString('base64')),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    };

    try {
        // Exchange authorization code for access token
        const tokenResponse = await axios.post(authOptions.url, authOptions.data, { headers: authOptions.headers });
        const { access_token } = tokenResponse.data;

        // Get user details to create a playlist for the user
        const userOptions = {
            url: 'https://api.spotify.com/v1/me',
            headers: { 'Authorization': 'Bearer ' + access_token }
        };

        const userResponse = await axios.get(userOptions.url, { headers: userOptions.headers });
        const user_id = userResponse.data.id;

        // Create a new playlist
        const createPlaylistOptions = {
            url: `https://api.spotify.com/v1/users/${user_id}/playlists`,
            headers: { 'Authorization': 'Bearer ' + access_token },
            data: {
                name: 'My Vaca Playlist',
                description: 'A playlist curated by COUNTRYmen',
                public: false
            }
        };

        const createPlaylistResponse = await axios.post(createPlaylistOptions.url, createPlaylistOptions.data, { headers: createPlaylistOptions.headers });
        const playlist_id = createPlaylistResponse.data.id;
        const playlist_url = createPlaylistResponse.data.external_urls.spotify;

        console.log(`Playlist created with ID: ${playlist_id}`);

        // Redirect user to the newly created playlist in Spotify
        res.redirect(playlist_url);

    } catch (error) {
        // Redirect to an error page if token exchange or playlist creation fails
        res.redirect('/#' +
            querystring.stringify({
                error: 'invalid_token'
            }));
    }
});

// Start the Express server
console.log('Listening on 8000');
app.listen(8000);
