bestSellingAlbums = [
    {
        "artist": "Michael Jackson",
        "title": "Thriller",
        "year": 1982,
        "genres": ["pop", "post-disco", "funk", "rock"],
        "sale": 70000000,
    },
    {
        "artist": "AC/DC",
        "title": "Back in Black",
        "year": 1980,
        "genres": ["hard rock"],
        "sale": 50000000,
    },
    {
        "artist": "Whitney Houston",
        "title": "The Bodyguard",
        "year": 1992,
        "genres": ["r&b", "soul", "pop", "soundtrack"],
        "sale": 45000000,
    },
    {
        "artist": "Pink Floyd",
        "title": "The Dark Side of the Moon",
        "year": 1973,
        "genres": ["progressive rock"],
        "sale": 45000000,
    },
    {
        "artist": "Eagles",
        "title": "Their Greatest Hits (1971 - 1975)",
        "year": 1976,
        "genres": ["country rock", "soft rock", "folk rock"],
        "sale": 44000000,
    },
    {
        "artist": "Eagles",
        "title": "Hotel California",
        "year": 1976,
        "genres": ["soft rock"],
        "sale": 42000000,
    },
    {
        "artist": "Shania Twain",
        "title": "Come On Over",
        "year": 1997,
        "genres": ["country", "pop"],
        "sale": 40000000,
    },
    {
        "artist": "Fleetwood Mac",
        "title": "Rumours",
        "year": 1977,
        "genres": ["soft rock"],
        "sale": 40000000,
    },
]

# WRITE YOUR CODE HERE

# Calculate average sales income

total_sale = 0

for album in bestSellingAlbums:
    total_sale += album['sale']
average_sale = total_sale / len(bestSellingAlbums)
print(average_sale)

# Calculate average age

current_year = 2024
total_year = 0

for album in bestSellingAlbums:
    total_year += current_year - album['year']

average_year = total_year / len(bestSellingAlbums)
print(average_year)

# Newest and oldest album

newest_album = max(bestSellingAlbums, key=lambda album: album['year'])
oldest_album = min(bestSellingAlbums, key=lambda album: album['year'])

print(f"newest album: {newest_album['title']}({newest_album['year']})")
print(f"oldest album: {oldest_album['title']}({oldest_album['year']})")

# Albums of Eagles

eagles_albums = []
for album in bestSellingAlbums:
    if album["artist"] == "Eagles":
        eagles_albums.append(album)

total_sales = eagles_albums[0]["sale"] + eagles_albums[1]["sale"]

is_both_soft_rock = "soft rock" in eagles_albums[0]["genres"] and "soft rock" in eagles_albums[1]["genres"]

albums_eagles = {
    "artist": "Eagles",
    "albums": [eagles_albums[0]["title"], eagles_albums[1]["title"]],
    "sales": total_sales,
    "is_both_soft_rock": is_both_soft_rock
}

print(albums_eagles)

# Add an extra album

new_album = {
    "artist": "The Beatles",
    "title": "Abbey Road",
    "year": 1969,
    "genres": ["rock", "pop rock"],
    "sale": 32000000,
}

bestSellingAlbums.append(new_album)

print(bestSellingAlbums[-1])

# Like it or not

for album in bestSellingAlbums:
    if album["title"] in ["Thriller", "Abbey Road"]:
        album["i_like_it"] = True
    else:
        album["i_like_it"] = False

for album in bestSellingAlbums:
    print(album)        