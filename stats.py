def get_num_words(file_content):
    num_words = len(file_content.split())
    return num_words



def get_char_apps(file_content):
    src = "abcdefghijklmnopqrstuvwxyz0123456789\\][\"\',.;:|=+-_)(*&/^%$#@!~` "
    apps_count = {}
    for char in src:
        apps_count[char] = file_content.count(char)
        if file_content.count(char) == 0:
            del apps_count[char]
            break
    return apps_count



def sort(my_dict):
    apps_count_sort = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    return apps_count_sort


#sorted_dict_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    
