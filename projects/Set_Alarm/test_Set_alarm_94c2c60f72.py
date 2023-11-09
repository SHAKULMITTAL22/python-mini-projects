def set_alarm():
    # Get time input
    alarm_time = input("Enter the alarm time(HH:MM): ")
    
    # Validate the time format
    if re.search(r'^([01]\d|2[0-3]):([0-5]\d)$', alarm_time):
        # Check if musics are present in the folder
        musics = os.listdir('/musics')
        if len(musics) == 0:
            print('No musics to play the alarm found.')
        else:
            # Room for more conditions when music files are present
    else:
        print("Invalid time format!!!")
