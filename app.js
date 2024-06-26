const express = require('express');
const axios = require('axios');
const querystring = require('querystring');
require('dotenv').config();
const app = express();

app.use(express.json()); // To handle JSON payloads

// Middleware to log all requests
app.use((req, res, next) => {
    console.log(`${req.method} request to ${req.url}`);
    next();
});

const client_id = process.env.CLIENT_ID; // Your Spotify client ID
const client_secret = process.env.CLIENT_SECRET; // Your Spotify client secret
const redirect_uri = process.env.REDIRECT_URI; // Your redirect URI

// Endpoint to initiate login and authorization process
app.get('/login', (req, res) => {
    const scope = 'playlist-modify-public playlist-modify-private';
    res.redirect('https://accounts.spotify.com/authorize?' + querystring.stringify({
        response_type: 'code',
        client_id: client_id,
        scope: scope,
        redirect_uri: redirect_uri
    }));
});

app.get('/callback', async (req, res) => {
    const code = req.query.code || null;
    if (!code) {
        res.redirect('/#' + querystring.stringify({ error: 'invalid_request' }));
        return;
    }

    const tokenOptions = {
        method: 'post',
        url: 'https://accounts.spotify.com/api/token',
        data: querystring.stringify({
            code: code,
            redirect_uri: redirect_uri,
            grant_type: 'authorization_code'
        }),
        headers: {
            'Authorization': 'Basic ' + Buffer.from(client_id + ':' + client_secret).toString('base64'),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    };

    try {
        const response = await axios(tokenOptions);
        const access_token = response.data.access_token;
        // Send token to the client securely instead of redirecting with it in the URL
        res.json({ access_token }); // This can be handled by your client to make further requests
    } catch (error) {
        console.error('Error during token acquisition:', error.response ? error.response.data : error.message);
        res.redirect('/#' + querystring.stringify({ error: 'access_token_error' }));
    }
});


app.post('/create_playlist', async (req, res) => {
    const access_token = req.body.access_token;
    const tracks = req.body.tracks; // Assuming tracks are passed correctly as an array in the body

    if (!access_token) {
        res.status(400).send('Access Token is required');
        return;
    }

    try {
        // Get user details
        const userResponse = await axios({
            method: 'get',
            url: 'https://api.spotify.com/v1/me',
            headers: { 'Authorization': 'Bearer ' + access_token }
        });
        const user_id = userResponse.data.id;

        // Create a new playlist
        const createPlaylistOptions = {
            method: 'post',
            url: `https://api.spotify.com/v1/users/${user_id}/playlists`,
            headers: { 'Authorization': 'Bearer ' + access_token },
            data: {
                name: 'My Awesome Playlist',
                description: 'Created via API',
                public: false
            }
        };
        const createPlaylistResponse = await axios(createPlaylistOptions);
        const playlist_id = createPlaylistResponse.data.id;

        // Add tracks to the playlist
        const addTracksOptions = {
            method: 'post',
            url: `https://api.spotify.com/v1/playlists/${playlist_id}/tracks`,
            headers: { 'Authorization': 'Bearer ' + access_token },
            data: { uris: tracks }
        };
        await axios(addTracksOptions);

        res.json({ message: 'Playlist created and tracks added successfully', playlist_url: createPlaylistResponse.data.external_urls.spotify });
    } catch (error) {
        console.error('Failed to create playlist or add tracks:', error.response ? error.response.data : error.message);
        res.status(500).json({ error: 'Failed to create playlist or add tracks', details: error.response ? error.response.data : error.message });
    }
});

// Start the Express server
app.listen(8000, () => {
    console.log('Listening on 8000');
});
