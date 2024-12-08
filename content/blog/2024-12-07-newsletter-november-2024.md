+++
title = "Pactus Newsletter, November 2024"
description = """
November Highlights: Pactus under attack, Zero-Fee Transactions, 6 million transactions & more ...
"""
author = "Pactus Team"
date = 2024-12-07T00:00:00+00:00
draft = false
tags = ["newsletter"]
image = "pactus-newsletter-november-2024.png"
+++

## Pactus Highlights

Welcome to the November 2024 edition of the Pactus Newsletter!
This month has seen steady progress and notable developments.
Let’s dive into the details.
This month has seen steady progress and notable development updates.
Let's dive into all the details.

## Pactus Reaches 6 Million Transactions

Pactus has processed over 6 million transactions!
This significant milestone underscores the ongoing growth of our network,
showcasing its resilience and continuous improvements in efficiency.
We remain committed to enhancing both performance and accessibility as we grow.
showcasing its resilience and the continued improvements in efficiency.
We remain committed to enhancing both performance and accessibility as we grow.

## Highlights from Twitter Spaces with Parifi

The recent Twitter Spaces session with [Parifi](https://x.com/0xParifi) was a fantastic success,
with great participation from both existing community members and newcomers.
The discussions on DeFi scalability, security, and making blockchain more accessible were insightful.

## Zealy Campaign Winners

Congratulations to the Zealy campaign winners!
Your dedication and hard work have truly shone through, and we are proud to celebrate your success.
If you are one of the winners, please remember to claim your prize before January 11th, 2025.
To view the Prize List, click [here](https://docs.google.com/spreadsheets/d/1QntkwUv-eoCB2Log_SAcBSFOKEQL38YlqZvQAzdgvz0).
[here](https://docs.google.com/spreadsheets/d/1QntkwUv-eoCB2Log_SAcBSFOKEQL38YlqZvQAzdgvz0).
Don't miss out on your well-deserved rewards!

## Lower Withdrawal Fees on Azbit

[Azbit](https://azbit.com/) has reduced the withdrawal fee for PAC coins by 33.33%.
This is a great step towards making PAC transactions more economical,
ensuring that our community has easier and more cost-effective access to their assets.
We are excited about this positive change,
and we remain dedicated to finding more ways to make PAC accessible to everyone.

## Version 1.6.0 (Mumbai) Release

This month, the [Pactus 1.6.0 (Mumbai)](https://pactus.org/2024/11/14/pactus-1.6.0-mumbai-released/) was released.
This update introduces a new consumption fee model based on the number of bytes each address sends to the network daily.
This model that is proposed by [PIP-31](https://pips.pactus.org/PIPs/pip-31),
enables the Pactus blockchain to support transactions with zero fees, also known as gas-less transactions.
You can check out this tutorial to learn more about zero-fee transactions on Pactus:
[How to Send Zero-Fee Transactions?](https://docs.pactus.org/tutorials/zero-fee-transactios/)

## New GUI Under Development

A new graphical interface for Pactus is now under development.
The team has started working on the GUI using the popular [Flutter](https://flutter.dev/) framework,
which supports cross-platform compilation, including mobile devices.
The ultimate goal of the new Pactus GUI is to enable validators to control their nodes directly from their phones.
Stay tuned for more exciting updates from the GUI development team!

## Notifications on the Way

Pactus currently lacks a standardized notification system.
There are many use cases where users might want notifications.
For instance, when a block is created or a transaction is confirmed.
The development team is drafting a new PIP for a notification service.
A potential candidate for implementing this system is
[ZeroMQ](https://github.com/bitcoin/bitcoin/blob/master/doc/zmq.md), a library also used in Bitcoin Core.

## Scoring Peers on the P2P Network

One effective way to prevent abnormal behavior from certain peers on the P2P network is
to assign a score based on their actions.
The development team is currently working on drafting a new PIP for peer scoring on the network.
This system will allow peers to detect and disconnect from malicious actors, ensuring network stability and security.

## Pactus Under Attack

In late November, the Pactus network came under a sophisticated spamming attack.
The attack involved spam transactions and network flooding with expired messages,
also known as a replay attack.
While the spam transactions had no impact on the consensus algorithm,
allowing validators to continue creating blocks as usual, the replay attack caused delays in the consensus process.
Upon detecting the issue, the development team quickly worked on a patch to help validators overcome the attack.
The good news is that the network is now stable, and Pactus is immune to replay attacks.
