+++
title = "Pioneering Sustainable Blockchain"
author = "Pactus Team"
description = """
Running Pactus on Raspberry Pi Zero highlights energy efficiency, accessibility, and decentralization,
driven by innovations like SSPoS and pruned nodes.
"""
date = 2024-12-15T00:00:00+00:00
tags = ["marketing"]
image = "pactus-sustainable-blockchain.png"
+++

As the blockchain industry grows, the demand for energy-efficient, secure, and decentralized solutions increases.
At Pactus, we are committed to addressing these challenges by designing a blockchain network that
provides sustainability without compromising performance and security.

## Energy Efficiency at the Core of Pactus

One of Pactus's standout features is its ability to operate with minimal energy requirements.
Unlike most blockchain networks that demand significant computational power or high-spec dedicated servers,
Pactus validators can run on devices as energy-efficient as a
[Raspberry Pi Zero](https://www.raspberrypi.com/products/raspberry-pi-zero/), which consumes just 2 watts of power.

![Pactus on Raspberry Pi Zero]({{<image "pactus-raspberry-pi-zero.jpg">}})

By leveraging affordable personal computers and shared Virtual Private Servers (VPS),
Pactus ensures both energy efficiency and decentralization.
This means more people can participate in our network without needing expensive, specialized hardware.

## The Building Blocks of Efficiency

### SSPoS Consensus Model

At the heart of Pactus is the
[Solid State Proof of Stake (SSPoS)](https://docs.pactus.org/protocol/consensus/proof-of-stake/) consensus model.
This approach uses a fixed committee of 51 validators, which changes over time.
The limited committee size reduces the complexity and the number of messages exchanged during consensus,
enabling efficient network operations without compromising security or scalability.

The dynamic nature of committee membership ensures that the network remains decentralized and secure,
with validators regularly rotating based on a fair selection process.

### Pruned Nodes

Pactus supports [pruned nodes](https://docs.pactus.org/tutorials/pruned-nodes/),
which store only the last 10 days of blockchain data instead of the entire transaction history.
This innovation significantly reduces storage requirements—from gigabytes to just a few hundred megabytes—and
allows new validators to sync with the network in just a [few minutes](https://snapshot.pactus.org/).

### User Friendly Interface

Pactus offers both a user-friendly [GUI](https://pactus.org/download/#gui) and
a powerful [CLI](https://pactus.org/download/#cli), providing flexibility for users of all levels.
These interfaces make it simple for anyone to download and run Pactus on their chosen machine.
