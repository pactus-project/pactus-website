+++
title = "Pactus Newsletter, June 2026"
description = """
June was an active month. A major release landed, the network dealt with
a real protocol-level vulnerability and recovered cleanly, and a new proposal
put the long-term reward economics of the chain up for community discussion.
"""
author = "Pactus Team"
date = "2026-07-02T00:00:00"
tags = ["newsletter"]
image = "pactus-newsletter-june-2026.png"
+++

## What Happened in June

June was an active month. A major release landed, the network dealt with a
real protocol-level vulnerability and recovered cleanly, and a new proposal
put the long-term reward economics of the chain up for community discussion.

## Pactus 1.15.0 (Bucharest)

**Released June 9, 2026.** Bucharest is one of the more technically significant
releases of the year. The headline addition is support for the **Secp256k1**
cryptographic curve, introduced through
**[PIP-53](https://pips.pactus.org/PIPs/pip-53)**. This is the same curve used
by Bitcoin and most of the broader ecosystem, meaning Pactus can now derive
addresses compatible with popular external wallets, including hardware wallets.
The feature will be activated in the next protocol upgrade.

Bucharest also ships a **Config Editor** inside the GUI — no more manual
configuration file editing — and migrates the GUI from **GTK3 to GTK4**,
putting the interface on a more modern, maintainable foundation.

Shortly after Bucharest shipped, a critical vulnerability was identified
(**[PIP-54](https://pips.pactus.org/PIPs/pip-54)**): an integer overflow in the
transaction validation layer that could be used to disrupt block production.
The team responded quickly, patched it and documented the exploit and the fix
publicly through the PIP process.

**[Download the latest version →](https://pactus.org/download/)**

> **Important:** If you are still on an older version, upgrade now. Outdated
> nodes do not produce blocks and do not earn rewards.

## PIP-55: Block Reward Halving Schedule

A new improvement proposal was submitted to the community in June:
**[PIP-55](https://pips.pactus.org/PIPs/pip-55)** proposes introducing a
periodic block reward halving schedule, reducing the PAC reward per block at
defined intervals over time.

This is a meaningful conversation for the community to have. Pactus was built
on a flat reward model — one PAC per block, constant forever — specifically to
avoid the wealth centralization effects that halving can create in a Proof of
Stake system. PIP-55 challenges that design choice. Read the proposal,
understand both sides, and make your voice heard.

**[Read PIP-55 →](https://pips.pactus.org/PIPs/pip-55)**

## Wrapto Bridge Update

The Polygon and Base WPAC bridge contracts on
**[Wrapto](https://wrapto.app/)** were retired in June following a security
incident.

## Stay Connected

The Pactus community lives and grows across multiple platforms. Wherever you
are most comfortable, show up, share ideas, ask questions, and help newcomers
find their way.

## Thank You

To every validator who upgraded without hesitation. To the developers who
found, documented, and patched a live exploit in real time. To everyone
weighing in on PIP-55 with actual arguments.

June tested the network and the community. Both held.

Let's keep building.
