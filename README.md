# Pactus website

This repository contains all the content for the [https://pactus.org](https://pactus.org) website.

## Contributing to Documentation

Contributions to the website, including fixing typos or grammatical errors, are always welcome.
To contribute, simply edit the relevant page or open a pull request.

## Running Locally

For running the website locally, you need to have the following installed on your machine:

- [Hugo](https://gohugo.io/)
- [Yarn](https://yarnpkg.com/) or [npm](https://www.npmjs.com/)

Pactus website is powered by [Hugo](https://gohugo.io/).
Make sure you have installed the `extended` version of hugo on your machine.

Now, clone this repository and run it locally using the following commands:

```bash
git clone https://github.com/pactus-project/pactus-website.git
cd pactus-website

yarn install
hugo server
```

## Guidelines

Follow these guidelines to ensure high-quality contributions to the Pactus website project.

### Creating a new blog post

For creating new blog post run:

```bash
hugo new content --kind blog blog/your-post-name.md
```

This command will create a new markdown file in the `content/blog` directory with the following front matter:

```markdown
+++
title = ''
description = ''
author = ''
date = 2022-08-29T00:00:00+00:00
tags = ['']
image = "pic.jpg"
+++
```

Make sure to fill all the fields carefully as they are important for SEO and user-friendly URLs.\
After creating the file, you can start writing your blog post.\
You can see your blog post in `http://localhost:1313/blog/your-post-slug` \

- **Note that description field is optional**

- **Note that for image only use the image name, the image should be in the `/assets/blog/post-filename/pic.jpg` directory**

### static assets

For adding images, you can use the `/assets/blog/post-filename/image.png` directory.

### Image

For optimizing images in markdown files use image shortcode: \
`{{<blogImage  url="image.png" title="image title" class="">}}` \
for class parameter check [tailwindcss](https://tailwindcss.com/) or just leave it empty

### asset url

`{{<asset "asset.pdf">}}`

example use:

`[link]({{<asset "asset.pdf">}})`

### Style change

For changing style in `assets/css/main.css` and running website concurrently run:

```bash
npm run start
```

### Additional commands

There are some additional commands that help you to check and improve your changes.
First you need Install [yarn](https://yarnpkg.com/).

- Check all HTML and markdown files:

```bash
yarn run prettier::setup
yarn run prettier
```

- Lint markdown files:

```bash
yarn run lint:md:setup
yarn run lint:md
```

- Lint YAML files:

```bash
yarn run lint:yml:setup
yarn run lint:yml
```

- Check for broken links:

```bash
yarn run htmlproofer:setup
yarn run htmlproofer
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

## Deployment

Updating the main branch will automatically deploy this repository through
[deploy](.github/workflows/deploy.yml) Github action.
