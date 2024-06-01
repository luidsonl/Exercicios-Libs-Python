from YoutubePlaylistScrapper import YoutubePlaylistScrapper

# URL da playlist do youtube
URL = 'https://www.youtube.com/playlist?list=OLAK5uy_kPd0sUOZ_aiVfrD16g_Mx1lVBssK8RIso'

playlist = YoutubePlaylistScrapper(URL)

print(playlist.title)
print(playlist.duration)
print(playlist.formated_duration)
print(playlist.length)

