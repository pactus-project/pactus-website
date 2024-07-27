+++
title = 'Download'
draft = false
layout = 'download'
type = 'download'
+++

{{<translate "dict.download.welcome">}}

---

<h2 id="build ">🏗️ {{<translate "dict.download.compile_from_source_code">}}</h2>

{{<translate "dict.download.project_pactus_is_distributed">}}

{{<translate "dict.download.instructions_for_compiling">}}

---

<h2 id="binary">⬇️ {{<translate "dict.download.stable_releases">}}</h2>

{{<translate "dict.download.stable_releases_desc">}}

<br>

{{<download_links>}}


<h3 id="downloader_script">{{<translate "dict.download.downloader_script">}}</h3>

{{<translate "dict.download.downloader_script_explained">}}

```sh
curl --proto '=https' --tlsv1.2 -sSL https://github.com/pactus-project/pactus/releases/download/v{{ site.latest_version }}/pactus_downloader.sh | sh
```

---

<h2 id="docker">🐳 {{<translate "dict.download.docker">}}</h2>

{{<translate "dict.download.docker_desc">}}

{{<translate "dict.download.docker_after_download">}} [{{<translate "dict.guide.run_pactus_docker">}}](https://docs.pactus.org/get-started/pactus-docker)
