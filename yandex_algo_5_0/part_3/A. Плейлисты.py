with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())
    n_first_curr_song = int(reader.readline().strip())
    common_playlist = {song for song in reader.readline().strip().split(" ")}
    for i in range(n - 1):
        n_curr_song = int(reader.readline().strip())
        curr_play_set = {song for song in reader.readline().strip().split(" ")}
        common_playlist.intersection_update(curr_play_set)

playlist_list = list(common_playlist)
playlist_list.sort()

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(len(playlist_list)))
    file.write("\n")
    playlist_to_add = " ".join(song for song in playlist_list)
    file.write(playlist_to_add)
