#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Valerie Yuan
# DATE CREATED: Jul 9, 2023                            
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
#     return None
# Retrieve the filenames from folder image_dir
    filename_list = listdir(image_dir)

    # Define our results dictionary
    results_dic = dict()

    # Process through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for filename in filename_list:

        # Skip file if starts with . (like .DS_Store of Mac OSX) because it isn't an image file
        if filename[0] != ".":
            # Creates temporary label variable to hold pet label name extracted 
            pet_label = ""

            # Define list of lower case words of the filename (split by _)
            image_name = filename.lower().split("_")

            # Create pet_name by:
            for word in image_name:
                # Only add to pet_name if word is all alphabets
                if word.isalpha():
                    pet_label += word + " "

            # Strip off starting/trailing whitespace characters 
            pet_label = pet_label.strip()

            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates 
            if filename not in results_dic:
                results_dic[filename] = [pet_label]

            else:
                print("** Warning: Duplicate files exist in directory:", 
                      filename)

    # Return the results dictionary
    return results_dic
