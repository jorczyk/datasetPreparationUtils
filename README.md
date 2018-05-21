# datasetPreparationUtils

The result of script would be two directories containing train and test samples, split in ratio provided by user.

As input provide a path to main directory containging entire dataset.
Train/test samples ratio could be set using N variable in code

For program to work properly the directory hierarchy should look like this:

main_dataset_directory  <--- the folder name you should provide as imput

|__first_entity_samples  <--- this subfolder would be renamed to "0"

|__second_entity_samples  <--- this subfolder would be renamed to "1"

WARNING - script would rename your original database directories names - backup copy highly recommended!
