import ndjson
import os
import json


def convert_ndjson(loading_directory, name, directory):
    with open(loading_directory + '/' + name) as f:
        data = ndjson.load(f)
        folder_location = directory + '/' + name[:-7]
        if os.path.exists(folder_location) is False:
            os.makedirs(folder_location)
        count = 1
        for line in data:
            path = folder_location + '/' + str(count)
            with open(path + '.json', 'w') as fp:
                json.dump(line, fp)
            print(name[:-7] + ': ' + str(count))
            count += 1


def convert_all_ndjsons(loading_directory, saving_directory):
    file_names = [f for f in os.listdir(loading_directory)]
    number_of_files = len(file_names)
    count = 1
    for file_name in file_names:
        print('converting ' + file_name)
        convert_ndjson(loading_directory, file_name, saving_directory)
        print(str(count) + '/' + str(number_of_files) + ' complete')
        count += 1


convert_all_ndjsons('full/simplified', 'doodles')
