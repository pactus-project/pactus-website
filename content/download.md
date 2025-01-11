+++
title = "Download"
draft = false
layout = "download"
type = "download"
description = """
The Pactus Download page provides access to the latest software releases.
"""
+++

On this page you can find how to download and get the latest version of the Pactus software.

---

### 🏗️ Compile from Source Code {#build}

Project Pactus is distributed as open source software,
so the preferred way for installing it is to clone the source code from
the [GitHub](https://github.com/pactus-project/pactus) repository and compile the source code.

Instructions for compiling Pactus is provided on the
[install](https://github.com/pactus-project/pactus/blob/main/docs/install.md) page.

---

### ⬇️ Download Stable Releases {#binary}

You can also download the latest stable releases of Pactus.
These releases are updated automatically when a new version is released in
[GitHub repository](https://github.com/pactus-project/pactus).

{{<download_links>}}

### Downloader script {#downloader_script}

For [Unix-like systems](https://en.wikipedia.org/wiki/Unix-like)
(e.g., Linux, macOS, or [MSYS2](https://en.wikipedia.org/wiki/Mingw-w64#MSYS2) on Windows),
there is a downloader script available.
This script can download the archived file, verify it, and extract it for you.
To use it, simply run the following command in your terminal:

<pre>
curl --proto '=https' --tlsv1.2 -sSL <span class="release-tag-link">---</span>/pactus_downloader.sh | sh
</pre>

---

### 🐳 Docker Container {#docker}

Advanced users can get the Pactus docker image from [Docker Hub](https://hub.docker.com/r/pactus/pactus).

You may follow this tutorial to set up and run your node using Docker:
[Run Pactus using Docker](https://docs.pactus.org/get-started/pactus-docker)
