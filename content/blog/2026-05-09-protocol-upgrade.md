+++
title = "Protocol Upgrades in Pactus: Why Pactus Doesn’t Have Hard Forks"
description = """
An overview of how Pactus handles protocol upgrades in a coordinated way without chain splits or hard forks.
"""
author = "Pactus Team"
date = "2026-05-09T00:00:00"
tags = ["newsletter"]
image = "protocol-upgrade.png"
+++

Protocol upgrades are an important part of every blockchain network.
As networks evolve, they need to improve performance, add features, fix issues, or introduce new rules.

However, the way upgrades happen can be very different between Proof-of-Work and Proof-of-Stake systems.

Pactus uses a coordinated upgrade mechanism designed for a Proof-of-Stake network with finality.
To understand why this matters, it helps to first look at how upgrades work in Bitcoin.

## Hard Forks in Bitcoin

In Proof-of-Work blockchains like Bitcoin, protocol changes are commonly known as **hard forks**.

A hard fork happens when the network rules change in a way that older software can no longer fully validate new blocks.
Nodes running different versions of the protocol may temporarily follow different chains.

In most cases, the majority of miners, exchanges, wallets, and users eventually move
to the upgraded version of the network.
As the majority adopts the new rules, the older chain gradually becomes inactive.

Because Bitcoin uses Proof-of-Work, miners independently produce blocks and compete to extend the chain.
During upgrades, different parts of the network may temporarily produce incompatible blocks,
which is why the process is called a “fork.”

![Proof-of-Work chain]({{<image "liveness-over-safety.png">}})

Bitcoin has used signaling mechanisms during upgrades to measure miner readiness before activation.
One well-known example is the [SegWit](https://en.wikipedia.org/wiki/SegWit) upgrade,
where miners signaled support before the new rules became active.

Although most upgrades eventually converge to a single chain,
Proof-of-Work systems always carry the possibility that
parts of the community continue following different rules, potentially creating separate chains.

## Why Pactus Is Different

Pactus uses a **Proof-of-Stake** consensus model with block finality.
This changes the upgrade process fundamentally.

In Pactus, blocks are finalized by validators.
It means once a block becomes final, the network cannot continue from two competing histories

![Proof-of-Work chain]({{<image "safety-over-liveness.png">}})

Instead of miners competing to build different chains, validators coordinate on a single finalized chain.
Because of this, Pactus upgrades are better described as **protocol upgrades** rather than “hard forks.”

Validators that remain on older software will no longer be compatible
with the finalized chain after the activation point.
Since Pactus uses finality, the network always maintains a single agreed history.

## How Upgrade Support Is Signaled

The details of the upgrade mechanism are defined in
[PIP-51 (Protocol Upgrade Mechanism)](https://pips.pactus.org/PIPs/pip-51),
where the full technical specification is described.

In practice, validators communicate their readiness for a new protocol version through normal network activity.
When nodes connect to each other, they exchange their supported protocol versions,
and this information is also included in block proposals.
Over time, this creates a live picture of how much of the validator set is already running the new software.

Unlike many Proof-of-Stake systems that activate upgrades at a predetermined block height or epoch,
Pactus activates upgrades based on real-time validator support as described in PIP-51.

This allows the network to observe upgrade readiness directly from validator behavior,
without requiring any external coordination process.

## How the Upgrade Becomes Active

Once enough validators have upgraded, a proposer detects that a supermajority of the committee
supports the new protocol version.
At that point, the proposer begins producing blocks under the new rules by increasing the block version.

From this moment, the network transitions smoothly into the upgraded protocol.
Validators running the new version continue to validate and finalize blocks as usual,
while nodes that did not upgrade can no longer interpret the new block format or participate in consensus.
They fall out of sync and must upgrade to rejoin the network.

Because of finality, the network does not split into competing chains.
Instead, it continues forward as a single, unified history under the new protocol version.

## Why This Model Matters

Pactus protocol upgrades are a way for the network to improve and evolve over time without disrupting the chain.
Upgrades happen when most validators signal support for a new protocol version.
Once that support is strong enough, the block version is increased and the upgrade becomes active.

This reflects a unique design of Pactus, where upgrades happen in a smart, dynamic way through validator agreement.
