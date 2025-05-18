def get_num_words(file_content):
    num_words = len(file_content.split())
    return num_words



def get_char_apps(file_content):
    src = "abcdefghijklmnopqrstuvwxyz0123456789\\][\"\',.;:|=+-_)(*&/^%$#@!~` "
    b = int(0)
    apps_count = {}
    #apps = file_content
    for char in src:
        apps_count[char] = file_content.count(char)
    return apps_count
