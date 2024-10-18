+++
title = 'Download'
draft = false
layout = 'download'
type = 'download'
description = """
The Pactus Download page provides access to the latest software releases.
"""
+++

On this page you can find how to download and get the latest version of the Pactus software.

---

<h3 id="build">🏗️ Compile from Source Code</h3>

Project Pactus is distributed as open source software,
so the preferred way for installing it is to clone the source code from
the [GitHub](https://github.com/pactus-project/pactus) repository and compile the source code.

Instructions for compiling Pactus is provided on the
[install](https://github.com/pactus-project/pactus/blob/main/docs/install.md) page.

---

<h3 id="binary">⬇️ Download Stable Releases</h3>

You can also download the latest stable releases of Pactus.
These releases are updated automatically when a new version is released in
[GitHub repository](https://github.com/pactus-project/pactus).

{{<download_links>}}

<h3 id="downloader_script">Downloader script</h3>

For [Unix-like systems](https://en.wikipedia.org/wiki/Unix-like)
(e.g., Linux, macOS, or [MSYS2](https://en.wikipedia.org/wiki/Mingw-w64#MSYS2) on Windows),
there is a downloader script available.
This script can download the archived file, verify it, and extract it for you.
To use it, simply run the following command in your terminal:

<pre> 
curl --proto '=https' --tlsv1.2 -sSL https://github.com/pactus-project/pactus/releases/download/<span class="latest-version">---</span>/pactus_downloader.sh | sh
</pre>

---

<h3 id="docker">🐳 Docker Container</h3>

Advanced users can get the Pactus docker image from [Docker Hub](https://hub.docker.com/r/pactus/pactus).

You may follow this tutorial to set up and run your node using Docker:
[Run Pactus using Docker](https://docs.pactus.org/get-started/pactus-docker)
