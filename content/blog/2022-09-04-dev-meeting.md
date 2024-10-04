+++
title = 'Dev meeting - September 2022'
author = 'Pactus Team'
date = 2022-09-04T00:00:00+00:00
draft = false
tags = ['pactus', 'dev-meeting']
slug = 'dev-meeting'
image = "/images/pactus-blog-post-default.jpg"
+++

## Meeting Summary

The meeting took place on 04 September 2022, at 2:00 PM UTC via Google Meet,
with team members from different time zones joining to discuss key aspects of the Pactus project.

### NanoMsg instead of ZeroMQ

During the meeting, Joseph suggested using Nanomsg instead of ZeroMQ because building ZeroMQ is not easy,
especially in Windows. Additionally, we can use the pure Go implementation of Nanomsg.

The format of block events was defined as follows:

```text
<event_id: 1 byte><event_data: variant><height: 4 bytes><seq_num: 4 bytes>
```

As a consequence of this, smart contracts events can be defined more easily and
Infura-like services become simple, as we can just replay the events.

### Reviewing a Pull Request

Nagaraj's [pull request](https://github.com/pactus-project/pactus/pull/355) reviewed.

### Renaming project

The team discussed renaming (rebranding) the project and decided to create an online survey to
gather suggestions for a new name.
Everyone is encouraged to participate in the survey and suggest new names for the project.
