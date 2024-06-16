from YoutubePlaylistScrapper import YoutubePlaylistScrapper

# URL da playlist do youtube
URL = 'https://www.youtube.com/playlist?list=PL_xRyXins848nDj2v-TJYahzvs-XW9sVV'

playlist = YoutubePlaylistScrapper(URL)

print(playlist.title)
print(playlist.duration)
print(playlist.formated_duration)
print(playlist.length)