# image-diff
Create and reapply diffs between two images.


### Idea
Using machine learning super resolution you supply a LR (low resolution) image with the output being a HR (high resolution) image. This project will create a diff image between the LR source and the outputted HR image. 

The diff can then be reapplied to the LR source, effectively recreating a 1:1 match of the super resolution HR output.


### Project directory structure
Examples are provided in this project. `LR` and `HR` folders must be populated with images you supply.

The `diff` folder contains a diff between the LR and HR images.

The `result` folder contains the resulting image by applying a diff to the LR image. It will be identical to the HR image.


### python create_diff.py
This will create a diff between two images. Edit create_diff.py to point to the images you want to diff using HR_IMG and LR_IMAGE.


### python apply_diff.py
This will apply a diff file to the original LR source recreating the HR image. Edit apply_diff.py to point to the diff image and original LR image using DIFF_IMG and LR_IMG.