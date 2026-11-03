+++
title = "Pactus Newsletter, October 2026"
description = """
October brought one release and one community project. Pactus 1.17.0 (Berlin)
arrived on October 28 with Native State Anchoring and a redesigned GUI.
Meanwhile, a community builder started work on Pactus Pages, a directory built
on the new anchoring feature.
"""
author = "Pactus Team"
date = "2026-11-03T00:00:00"
tags = ["newsletter"]
image = "pactus-newsletter-october-2026.png"
+++

## What Happened in October

October brought one release and one community project. Pactus 1.17.0 (Berlin)
arrived on October 28 with Native State Anchoring and a redesigned GUI.
Meanwhile, a community builder started work on Pactus Pages, a directory built
on the new anchoring feature.

## Pactus 1.17.0 (Berlin) Released

**Native State Anchoring (PIP-50).** Every account can now hold one active
anchor slot for a fingerprint (hash) of a document, profile or list. Anyone can
verify it later. A refundable deposit of at least 1 PAC is required, and
timestamps come from the block itself, so they cannot be backdated. New node
APIs let wallets and apps read, build and watch anchors.

Anchoring is shipped with this release but is not yet active on Mainnet. It
activates at protocol version 5, once validators more than 75% of committee
power supports it.

**New GUI.** Sidebar navigation, redesigned dashboards, light and dark themes, a
Max button for amounts, and balance and stake shown in address lists.

**Wallet migration.** Legacy JSON wallets can now move to the modern SQLite
storage from the GUI, the CLI or gRPC.

**Security.** Delegated withdrawals now require the stake owner's signature, and
quorum certificates are bound to vote height and round.

**How to upgrade.** Close your current version, uninstall it, then install
Berlin. If you use the archived (portable) version, simply replace the file.
Validators should upgrade early once version 5 activates, since older nodes will
not be able to follow the chain once version 5 activates.

Download it from the [download page](https://pactus.org/download).

## Community Spotlight: Pactus Pages

A community member is building Pactus Pages, the yellow pages of the Pactus
chain. Profiles are anchored on chain with PIP-50 and verified in your browser.
It is an early project, and since anchoring is not live on Mainnet yet, the
testnet version is the place to try it.

- Demo: <https://pactus.page/?demo#/>
- Testnet: <https://testnet.pactus.page/>

## Resources for Builders

- API guides: <https://docs.pactusscan.com/>
- Working API examples: <https://demo.pactusscan.com/>
- dApp ideas: <https://dapps.pactusscan.com/>

## Stay Connected

Join the community on Discord, Telegram and X.

## Thank You

Thanks to the validators who upgrade each release and to the builders turning
new features into real tools.
