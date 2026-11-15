+++
title = "PIP-50 Activated: Native State Anchoring Is Live on Pactus"
description = """
Pactus network activated PIP-50: Native State Anchoring at block 8,738,127,
upgrading to Protocol Version 5 and giving every account one on-chain anchor slot.
"""
author = "Pactus Team"
date = "2026-11-13T00:00:00"
tags = ["upgrade", "announcement", "pip"]
image = "pip-50-activated.png"
+++

The Pactus network has successfully activated
**[PIP-50: Native State Anchoring](https://pips.pactus.org/PIPs/pip-50)** at
**[block 8,738,127](https://pactusscan.com/block/8738127)**, produced on
13 November 2026 at 12:47:20 UTC. This upgrade moves the network to **Protocol Version 5**
and gives every Pactus account a new capability: a single, live slot for anchoring a
commitment to data directly in the chain state.

As with previous upgrades, the transition happened without a hard fork. Following the protocol
upgrade mechanism of [PIP-51](https://pips.pactus.org/PIPs/pip-51), proposers raised the block
version as soon as more than 75% of committee power supported Protocol Version 5.
Block 8,738,126 was the last block of version 4, the very next block was version 5, and block
production continued without interruption.

## What Changed?

PIP-50 adds one optional anchor to each account. An anchor is a small, verifiable record that
lives in the current state of the network:

| Field              | What it holds                                                                |
| ------------------ | ---------------------------------------------------------------------------- |
| Digest             | A bounded commitment, such as the hash of a file or a Merkle root            |
| Pointer (optional) | A link to the off-chain bytes, for example an IPFS or HTTPS URI              |
| Type hint          | A short label that tells applications how to read the anchor                 |
| Deposit            | A refundable amount of PAC locked while the anchor exists                    |
| Timestamps         | Creation and update heights, written by the protocol itself                  |

Anchors are managed with a new transaction type with two actions:

- **Set** creates the anchor or replaces its content. It locks a deposit of at least 1 PAC
  (the initial `MinAnchorDeposit`).
- **Delete** removes the anchor and refunds the locked deposit.

The timestamps come from the block that includes the transaction, not from the transaction
itself, so nobody can backdate an anchor.

## Why It Matters

Most blockchains can prove that some data was written at some point in history, but reading it
back usually requires an archive node and a search through old blocks. PIP-50 takes a different
approach: the anchor is part of the **live global state**. Even a pruned node can answer the
question "what does this account currently commit to?" in a single lookup.

This opens the door to simple, low-cost building blocks:

- **Document stamping** — prove that a contract, report or certificate existed in a given form.
- **Decentralized identity** — publish the current hash of a DID document.
- **Revocation registries** — point to the latest list of revoked credentials.
- **Service manifests** — let a project announce the current version of its configuration or
  release files.

Because the deposit is refunded on deletion, an anchor costs only the transaction fee over its
lifetime, while the deposit discourages spam and keeps the state small.

PIP-50 also defines **PAC-ANCHOR-1**, an optional application profile for hashing a single file
or committing many files under one Merkle root, so wallets and dApps can verify each other's
anchors in the same way.

## Anchors on PactusScan

You can follow anchoring activity on the [PactusScan](https://pactusscan.com) block explorer:

- The activation block [8,738,127](https://pactusscan.com/block/8738127) marks the start of
  Protocol Version 5.
- The first anchor on mainnet was set at
  [block 8,738,167](https://pactusscan.com/block/8738167), only 40 blocks after activation.
- Every address page shows the current anchor of that account, including its digest, pointer
  and locked deposit.
- The committee page shows which protocol versions the current committee supports.

Developers who want to experiment first can use the
[anchor lookup demo](https://pactusscan.com/anchor-demo), which reads anchors through the
PactusScan API.

## Important Notice for Validators and Node Operators

Protocol Version 5 is **not backward compatible**. Nodes that still run a release without
Protocol Version 5 support cannot follow version 5 blocks. They will stop synchronizing,
cannot take part in consensus, and will not receive block rewards.

If you have not done so yet, **upgrade to [Pactus 1.17.0 (Berlin)](https://pactus.org/download/)
or later right away**. The release notes also describe the new node APIs for anchors:
`GetAnchor`, `ListAnchors`, `GetRawAnchorTransaction`, and the `anchor_info` ZeroMQ topic.

## Looking Ahead

Protocol Version 5 is the fourth protocol upgrade carried out through the
[PIP-51](https://pips.pactus.org/PIPs/pip-51) mechanism, after the reward split, validator
delegation, and the block reward halving. Each one shows that Pactus can add meaningful
features while keeping a single, finalized chain.

With native state anchoring, Pactus gains a simple and verifiable way to connect real-world
data to the blockchain. We thank every validator who upgraded in time, and every developer who
tested anchors on the testnet. We look forward to seeing what the community builds on top of it.
