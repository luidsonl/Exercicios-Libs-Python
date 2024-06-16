import requests
import re

class YoutubePlaylistScrapper:
    def __init__(self, url : str):

        self.html = self.__fetch_data(url)
        self.title = self.__get_playlist_title(self.html)
        self.length = self.__get_playlist_length(self.html)
        self.duration = self.__get_playlist_duration(self.html)
        self.formated_duration = self.__seconds_to_hours(self.duration)

        

    def __fetch_data(self, url: str):
        try:
            response = requests.get(url)
            return response.text

        except:
            return ''
        
    def __get_playlist_duration(self, html: str):
        pattern = r'"simpleText":"(\d{1,2}:\d{2}(?::\d{2})?)"},"navigationEndpoint"'

        durations = re.findall(pattern, html)

        return self.__sum_durations(durations)
    

    def __get_playlist_length(self, html: str):
        pattern = r'"iconType":"ADD_TO_QUEUE_TAIL"'
        length = len(re.findall(pattern, html))
        return length
    
    def __sum_durations(self, durations: list):
        total_seconds = 0

        for duration in durations:
            parts = duration.split(':')

            has_hours = len(parts) > 2

            hours = int(parts[0]) if has_hours else 0
            minutes = int(parts[1]) if has_hours else int(parts[0])
            seconds = int(parts[2]) if has_hours else int(parts[1])

            total_seconds += hours * 3600 + minutes * 60 + seconds

        return total_seconds
    
    def __seconds_to_hours(self, seconds: int):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        return str(hours) + ':' + str(minutes) + ':' + str(seconds)
    
    def __get_playlist_title(self, html: str):
        pattern = r'"title":\{"simpleText":"([^"]+)"\}'
        try:
            match = re.search(pattern, html)
            if match:
                return match.group(1)
            else:
                return None 
        except AttributeError:
            return None