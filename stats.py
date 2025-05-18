def get_num_words(file_content):
    num_words = len(file_content.split())
    return num_words



def get_char_apps(file_content):
    src = "abcdefghijklmnopqrstuvwxyz0123456789\\][\"\',.;:|=+-_)(*&/^%$#@!~` "
    apps_count = {}
    for char in src:
        apps_count[char] = file_content.count(char)
    return apps_count
