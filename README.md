# IPYNBrenderer
IPYNBrenderer is a Python package designed to render YouTube tutorial videos and reference websites directly into Jupyter notebooks, making it convenient for you to reference them in the future.

[IPYNBrenderer Documentation](https://divyuk.github.io/onipynbrenderer/)

# Installation
To get started with IPYNBrenderer, follow these simple installation steps:

### Prerequisites
Before you begin, make sure you have Python and pip installed on your system. IPYNBrenderer is compatible with Python 3.6 and above.

### Installing the Package
You can easily install the IPYNBrenderer package using pip. Open your terminal or command prompt and run the following command:
```
pip install onipynbrenderer
```

This will download and install the package, along with any required dependencies.

# Usage
Once the package is installed, you can use it in your Colab or Jupyter notebooks to render YouTube tutorial videos and reference websites. Here's a basic example of how to use it:

python
```
from onipynbrenderer import render_youtube_video, render_website

# Render a YouTube video
render_youtube_video("https://www.youtube.com/watch?v=your_video_id")

# Render a website
render_website("https://www.example.com")
```
These functions will embed the YouTube video or website content directly into your notebook, making it easy to access and reference.



# API Reference
- **Rendering YouTube Videos**
  - Embed YouTube videos in Jupyter notebooks.
  - Accepts a YouTube video URL, height, and width.

- **Rendering Reference Websites**
  - Embed reference websites in Jupyter notebooks.
  - Accepts a website URL, height, and width.
## Rendering YouTube Videos
### Example
```
from onipynbrenderer import render_youtube_video

# Example usage
url = "https://www.youtube.com/watch?v=your_video_id"
height = 720
width = 600

response = render_youtube_video(url, height, width)
```
### Arguments

| Argument | Type | Description                                      | Default Value |
|----------|------|--------------------------------------------------|---------------|
| URL      | str  | Input URL of a YouTube video as a string.       | -             |
| height   | int  | Height of the video to display in Jupyter notebook. | 720         |
| width    | int  | Width of the video to display in Jupyter notebook.  | 600         |

### Response

| Return    | Type | Description                                      |
|-----------|------|--------------------------------------------------|
| Response  | str  | "success" if the rendering is successful, or "InvalidURLException" if the URL is invalid. |



## Rendering Reference Websites
### Example
```
from onipynbrenderer import render_website

# Example usage
url = "https://www.example.com"
height = "600"
width = "100%"

response = render_website(url, height, width)
```

### Arguments
| Argument | Type | Description                                       | Default Value |
|----------|------|---------------------------------------------------|---------------|
| URL      | str  | Input URL of a reference website as a string.     | -             |
| height   | str  | Height of the website to display in Jupyter notebook. | "600"         |
| width    | str  | Width of the website to display in Jupyter notebook.  | "100%"        |

### Response
| Return    | Type | Description                                      |
|-----------|------|--------------------------------------------------|
| Response  | str  | "success" if the rendering is successful, or "InvalidURLException" if the URL is invalid. |


# Contributing
We welcome contributions from the community. If you have suggestions, find a bug, or want to add new features, please open an issue on our GitHub repository and submit a pull request.

### Happy coding!
