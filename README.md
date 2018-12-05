# Memes 
Script to convert images to memes.

## Usage

### Prerequisites

* argparse==1.1
* json==2.0.9
* numpy==1.14.3
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

## Meme Generation
The current version of the script has the ability to create memes in four different formats using custom user defined images.
The script can be either in interactive or command line depending on chosen mode.

### Format 1
Text can be added to the top of the image in this format.

```
python meme_generator.py --mode=0 --format=1 --image1=path --text1=text
```
### Format 2
Text can be added to the bottom of the image.

```
python meme_generator.py --mode=0 --format=2 --image1=path --text1=text
```
### Format 3
Text can be added to both top and bottom of the image.

```
python meme_generator.py --mode=0 --format=3 --image1=path --text1=top --text2=bottom
```
### Format 4
Two images are concatenated sideways and contains both the top and bottom text.

```
python meme_generator.py --mode=0 --format=4 --image1=path --image2=path --text1=top --text2=bottom
```
Above formats can also be accessed interactively using mode=1

```
python meme_generator.py --mode=1 --format=1 
```
