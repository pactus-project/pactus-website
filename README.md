# Pactus website

This repository contains all the content for the [https://pactus.org](https://pactus.org) website.

## Contributing to Documentation

Contributions to the website, including fixing typos or grammatical errors, are always welcome.
To contribute, simply edit the relevant page or open a pull request.

## Running the Website Locally

### Prerequisites:

For running the website locally, you need to have the following installed on your machine:

- [Git](https://git-scm.com/downloads/)
- [Node.js](https://nodejs.org/en/download)
- [Hugo](https://gohugo.io/)

Pactus website is powered by [Hugo](https://gohugo.io/).
Make sure you have installed the `extended` version of hugo on your machine.

#### Windows Users:

For Windows users, it's recommended to install [Msys2](https://www.msys2.org/)
which provides a Unix-like environment for running command-line tools.
Once you have Msys2 set up, you can install the required packages using the following commands:

```bash
# Install Git
pacman -S git

# Install Nodejs
pacman -S mingw-w64-nodejs

# Install Hugo
pacman -S mingw-w64-hugo
```

### Running Locally:

Once you have the prerequisites in place, follow these steps to get the website up and running locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/pactus-project/pactus-website.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd pactus-website
    ```

3. **Install dependencies:**

    ```bash
    npm install
    ```

4. **Run the website locally:**

    ```bash
    hugo server
    ```

This will start a local development server and open the website in your default web browser.

## Guidelines

Follow these guidelines to ensure high-quality contributions to the Pactus website project.

### New Blog Post

To create a new blog post, run:

```bash
hugo new content --kind blog blog/your-post-name.md
```

This command will create a new markdown file in the `content/blog` directory with the following front matter:

```markdown
+++
title = "Title goes here"
description = "Description goes here (Optional)"
author = "Your Name"
date = 2024-10-20T16:39:03+08:00
tags = [""]
image = "post-image.png"
+++
```

### Blog Assets

All blog post assets, including images, should be kept inside the `/assets/blog/<post-filename>/` folder.
The blog post file name and the directory you create for its assets should have the same name.

#### Images

For optimizing images in markdown files, use the image [shortcode](https://gohugo.io/content-management/shortcodes/):

```md
![Post Image]({{<image "post-image.png">}})
```

You can specify the absolute image path like this:

```md
![Post Image]({{<image "/images/post-image.png">}})
```

#### Other Assets

Other assets, like PDF files, can be linked similarly:

```md
[Post Doc]({{<asset "post-doc.pdf">}})
```

## Markdown

Markdown is a lightweight markup language that uses plain text formatting syntax to convert text into HTML,
making it easy to read and write for web content.

### Linting

Markdown linting helps ensure consistent style and formatting, detects syntax errors, improves readability,
and maintains best practices in Markdown documents.

To lint Markdown files, you can use the `mdl` ([MarkdownLint](https://github.com/DavidAnson/markdownlint)) command-line tool.
This tool checks your Markdown files against a set of rules and provides feedback on any issues found.

To install `mdl`, first you need to install [Ruby](https://www.ruby-lang.org/en/documentation/installation/).
Once you ensure Ruby installed on your system, you can install `mdl` by running:

```sh
gem install mdl
```

Then you can lint your Markdown files with the following command:

```sh
mdl --style=.mdlrc.rb ./content
```

This command will check all documents in the `content` folder for any linting issues and output them in the terminal.

## Additional Commands

There are some additional commands to check and improve the changes.
Below are some useful commands:

| Command                     | Task                                                                               |
| --------------------------- | ---------------------------------------------------------------------------------- |
| `npm run start`             | Start the website locally and watch for css changes                                |
| `npm run build`             | Build the website locally                                                          |
| `npm run prettier:setup`    | Set up [Prettier](https://prettier.io/)                                            |
| `npm run prettier`          | Check all HTML and Markdown files using Prettier                                   |
| `npm run lint:md:setup`     | Set up Markdown linting                                                            |
| `npm run lint:md`           | Lint Markdown files                                                                |
| `npm run lint:yml:setup`    | Set up YAML linting                                                                |
| `npm run lint:yml`          | Lint YAML files                                                                    |
| `npm run htmlproofer:setup` | Set up [html-proofer](https://github.com/gjtorikian/html-proofer) for link checker |
| `npm run htmlproofer`       | Check for broken links using html-proofer                                          |
| `npm run exif`              | Remove Meta Information from images using [ExifTool](https://exiftool.org/)        |

## Deployment

Updating the main branch will automatically deploy this repository through
[deploy](.github/workflows/deploy.yml) Github action.
