import os


def folders():
    analysis_folder_name = "./data_for_analysis"
    if not os.path.isdir(analysis_folder_name):
        os.mkdir(analysis_folder_name)
        print("Created folder: " + analysis_folder_name)
    folder_prefix = analysis_folder_name + "/England_data"
    if not os.path.isdir(folder_prefix):
        os.mkdir(folder_prefix)
        print("Created folder: " + folder_prefix)
    return folder_prefix