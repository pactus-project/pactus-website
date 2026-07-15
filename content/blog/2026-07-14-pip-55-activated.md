+++
title = "PIP-55 Activated: Block Reward Halving Successfully Implemented"
description = """
Pactus network successfully activated PIP-55: Block Reward Halving at block 7,675,113,
upgrading to Protocol Version 4 and introducing a long-term predictable issuance schedule.
"""
author = "Pactus Team"
date = "2026-07-14T00:00:00"
tags = ["upgrade", "announcement", "pip"]
image = "pip-55-activated.png"
+++

The Pactus network has successfully activated
**[PIP-55: Block Reward Halving](https://pips.pactus.org/PIPs/pip-55)** at
**[block 7,675,113](https://pactusscan.com/block/7675113)**, marking another important
milestone in the evolution of the protocol. This protocol upgrade increases the network to
**Protocol Version 4** and introduces Pactus's first block reward halving schedule.

Unlike Proof-of-Work blockchains that rely on hard forks, Pactus uses a coordinated protocol
upgrade mechanism. Once a supermajority of validators signaled support for Protocol Version 4,
the network automatically transitioned to the new protocol without creating competing chains
or interrupting block production.

## What Changed?

PIP-55 introduces a predictable issuance schedule by reducing the block reward over time.
Instead of maintaining a constant reward forever, the network now follows a long-term
monetary policy with scheduled halvings.

The reward schedule is:

| Block Height            | Block Reward |
| ----------------------- | -----------: |
| 1 – 8,000,000           |    1.000 PAC |
| 8,000,001 – 24,000,000  |    0.500 PAC |
| 24,000,001 – 56,000,000 |    0.250 PAC |
| 56,000,001 onward       |    0.125 PAC |

This change gradually reduces inflation while preserving a permanent tail emission that
continues to incentivize validators and secure the network for the long term. The existing
70/30 reward split between validators and the Pactus Foundation remains unchanged, with both
portions scaling proportionally after each halving.

## Why It Matters

A sustainable blockchain requires a sustainable monetary policy.

By introducing scheduled reward reductions, Pactus establishes a transparent and predictable
issuance model that balances network security with long-term inflation control. As the network
continues to grow, transaction fees are expected to play an increasingly important role in
validator revenue while block rewards gradually decrease.

PIP-55 represents another step toward a mature and economically sustainable blockchain protocol.

## Important Notice for Validators

The upgrade became active at **block 7,675,113** after the network reached the required
validator support.

If your node has **not** been upgraded to a Protocol Version 4 compatible release, it will no
longer be able to synchronize with the network, participate in consensus, or receive block
rewards.

All validator operators should [upgrade immediately](https://pactus.org/download/) if they
have not already done so.

## Looking Ahead

Protocol upgrades are how Pactus continues to evolve while maintaining a single finalized
blockchain. Thanks to the protocol upgrade mechanism introduced in
[PIP-51](https://pips.pactus.org/PIPs/pip-51), new features and protocol improvements can be
activated safely through validator coordination rather than disruptive hard forks.

We would like to thank all validator operators and community members who upgraded their nodes
and helped ensure another smooth network transition. Together, we continue building a more
secure, sustainable, and decentralized blockchain.
