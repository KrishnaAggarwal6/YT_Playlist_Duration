import pytube

while True:
    playlist_link = input("Paste Link of playlist: ")
    playlist = pytube.Playlist(playlist_link)
    total_duration = 0

    for video_url in playlist.video_urls:
        video = pytube.YouTube(video_url)
        duration_seconds = video.length
        total_duration += duration_seconds

    hours, remainder = divmod(total_duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    totalvideos = len(playlist)
    print("Total duration:", f"{hours:02d}:{minutes:02d}:{seconds:02d} and videos = {totalvideos}")
    

    choice = input("Do you want to go again? (yes/no): ").lower()
    if choice != "yes":
        break