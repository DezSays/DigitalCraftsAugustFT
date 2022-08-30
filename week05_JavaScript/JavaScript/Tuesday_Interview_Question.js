//  Write a function to return the song names from the top tracks list.

songs = {
    "artists": [
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/1iNqsUDUraNWrj00bqssQG"
        },
        "href": "https://api.spotify.com/v1/artists/1iNqsUDUraNWrj00bqssQG",
        "id": "1iNqsUDUraNWrj00bqssQG",
        "name": "Dreamville",
        "type": "artist",
        "uri": "spotify:artist:1iNqsUDUraNWrj00bqssQG"
    },
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5"
        },
        "href": "https://api.spotify.com/v1/artists/6l3HvQ5sa6mXTsMTB19rO5",
        "id": "6l3HvQ5sa6mXTsMTB19rO5",
        "name": "J. Cole",
        "type": "artist",
        "uri": "spotify:artist:6l3HvQ5sa6mXTsMTB19rO5"
    },
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/75WcpJKWXBV3o3cfluWapK"
        },
        "href": "https://api.spotify.com/v1/artists/75WcpJKWXBV3o3cfluWapK",
        "id": "75WcpJKWXBV3o3cfluWapK",
        "name": "Lute",
        "type": "artist",
        "uri": "spotify:artist:75WcpJKWXBV3o3cfluWapK"
    },
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/4r63FhuTkUYltbVAg5TQnk"
        },
        "href": "https://api.spotify.com/v1/artists/4r63FhuTkUYltbVAg5TQnk",
        "id": "4r63FhuTkUYltbVAg5TQnk",
        "name": "DaBaby",
        "type": "artist",
        "uri": "spotify:artist:4r63FhuTkUYltbVAg5TQnk"
    }
],
"disc_number": 1,
"duration_ms": 202040,
"explicit": true,
"external_ids": {
    "isrc": "USUM71912963"
},
"external_urls": {
    "spotify": "https://open.spotify.com/track/6MF4tRr5lU8qok8IKaFOBE"
},
"href": "https://api.spotify.com/v1/tracks/6MF4tRr5lU8qok8IKaFOBE",
"id": "6MF4tRr5lU8qok8IKaFOBE",
"is_local": false,
"is_playable": true,
"name": "Under The Sun (with J. Cole & Lute feat. DaBaby)",
"popularity": 74,
"preview_url": null,
"track_number": 1,
"type": "track",
"uri": "spotify:track:6MF4tRr5lU8qok8IKaFOBE"
},
{
"album": {
    "album_type": "album",
    "artists": [
        {
            "external_urls": {
                "spotify": "https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5"
            },
            "href": "https://api.spotify.com/v1/artists/6l3HvQ5sa6mXTsMTB19rO5",
            "id": "6l3HvQ5sa6mXTsMTB19rO5",
            "name": "J. Cole",
            "type": "artist",
            "uri": "spotify:artist:6l3HvQ5sa6mXTsMTB19rO5"
        }
    ],
    "external_urls": {
        "spotify": "https://open.spotify.com/album/4JAvwK4APPArjIsOdGoJXX"
    },
    "href": "https://api.spotify.com/v1/albums/4JAvwK4APPArjIsOdGoJXX",
    "id": "4JAvwK4APPArjIsOdGoJXX",
    "images": [
        {
            "height": 640,
            "url": "https://i.scdn.co/image/ab67616d0000b27310e6745bb2f179dd3616b85f",
            "width": 640
        },
        {
            "height": 300,
            "url": "https://i.scdn.co/image/ab67616d00001e0210e6745bb2f179dd3616b85f",
            "width": 300
        },
        {
            "height": 64,
            "url": "https://i.scdn.co/image/ab67616d0000485110e6745bb2f179dd3616b85f",
            "width": 64
        }
    ],
    "name": "The Off-Season",
    "release_date": "2021-05-14",
    "release_date_precision": "day",
    "total_tracks": 12,
    "type": "album",
    "uri": "spotify:album:4JAvwK4APPArjIsOdGoJXX"
},
"artists": [
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5"
        },
        "href": "https://api.spotify.com/v1/artists/6l3HvQ5sa6mXTsMTB19rO5",
        "id": "6l3HvQ5sa6mXTsMTB19rO5",
        "name": "J. Cole",
        "type": "artist",
        "uri": "spotify:artist:6l3HvQ5sa6mXTsMTB19rO5"
    }
],
"disc_number": 1,
"duration_ms": 148421,
"explicit": true,
"external_ids": {
    "isrc": "QMJMT2103632"
},
"external_urls": {
    "spotify": "https://open.spotify.com/track/2cnKST6T9qUo2i907lm8zX"
},
"href": "https://api.spotify.com/v1/tracks/2cnKST6T9qUo2i907lm8zX",
"id": "2cnKST6T9qUo2i907lm8zX",
"is_local": false,
"is_playable": true,
"name": "a m a r i",
"popularity": 74,
"preview_url": null,
"track_number": 2,
"type": "track",
"uri": "spotify:track:2cnKST6T9qUo2i907lm8zX"
}

// Shortcut
function findSongs(songs) {
    console.log(songs.name) 
}
findSongs(songs)