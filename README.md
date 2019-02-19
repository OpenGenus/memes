# Memes

Script to convert images to memes.

## Usage

### Prerequisites

* argparse==1.1
* json==2.0.9
* PILLOW==5.1.0

### Structure
The folder **data** will have folders within it which will represent categories. Each category folder will have a name and a file **“data.txt”** within it which will hold the category detail. Within each category, there can be sub-categories or images. Images can have any descriptive name say *img.jpg* . Along with the image, there maybe another file *img.json* which will contain the image data.

Format of *img.json*

```
{
	"img_name": {
		"description": "img_description"
	}
}

```

### Preprocessing
Images in data folder can be preprocessed by running the following command.
```
python preprocess.py --data="path" --width=600
```
Preprocessed images are scaled according to the width provided and converted to jpg format.

### Indexing
Index script maintains index.json which contains the description of images present in the data. Description varies depending on the presence of img.json.
```
python index_data.py
```
### Searching
With searchp script now you can search for images present index json file. Current version compares the search string to the description of images.

There are two types of search:

* Index - Displays image in accordance with input .Can be enabled by setting index_search to 1
* String - Displays image from search string entered .Enabled by default.

Each of the types have two modes:

* Command Line
```
python searchp.py --mode=0 --search_str=string
python searchp.py --mode=0 --index_search=1 --search_idx=index
```

* Interactive
```
python searchp.py --mode=1
```
## Recommendation
The script has ability to recommend memes based on the meme location and the word match in the description of the meme.
```
python recommendation.py --meme=image_path
```

## Meme Generation
The current version of the script has the ability to create memes in four different formats using custom user defined images.
The script can be either in interactive or command line depending on chosen mode.

### Format 1
Text can be added either at the top `type 1`, at the bottom `type 2`, or at both `type 3`.
[See more](format_details.md#Format 1:)

```
python meme_generator.py --mode=0 --format=1 --image1=path --text1=text
```

### Format 2
Two images are merged vertically and texts can be added to the top of image 1 and to the bottom of image 2.
[See more](format_details.md#Format 2:)
```
python meme_generator.py --mode=0 --format=2 --image1=path --image2=path --text1=text --text2=text
```
### Format 3
Two images are merged horizontally and texts appear in four styles type 1, type 2, type 3, type 4.
[See more](format_details.md#Format 3:)

```
python meme_generator.py --mode=0 --format=3 --image1=path --image2 =path --text1=text --text2=text
```

Above formats can also be accessed interactively using mode=1

```
python meme_generator.py --mode=1 --format=1
```

## Features
* Use the generated meme to set as desktop background.

```
# Under development. To try the script run:
python utilities.py "<image-path>"
```
