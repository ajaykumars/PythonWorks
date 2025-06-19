sub_directory = {
    'text' : ['.txt','.pdf','.doc'],
    'images' : ['.png','.jpg'],
    'videos' : ['.mov','.mp4','.avi'],
    'music' : ['.mp3','.m4a']
}

def pick_directory(extension_value):
    for category, extensions in sub_directory.items():
        for extension in extensions:
            if extension == extension_value:
                return category

print(pick_directory('.mov'))
