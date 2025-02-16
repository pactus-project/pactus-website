+++
title = "Pactus Newsletter, September 2024"
description = """
September Highlights: TOKEN2049, 4 Million Transactions, New Website & more ...
"""
author = "Pactus Team"
date = 2024-10-03T00:00:00+00:00
tags = ["newsletter"]
image = "pactus-newsletter-september-2024.png"
+++

## Pactus Highlights

Welcome to the October 2024 edition of the Pactus Newsletter[^1].
This month has been packed with major milestones, exciting developments, and a fantastic experience at TOKEN2049.
Read on for a detailed breakdown of everything we’ve achieved together.

### TOKEN2049: A Remarkable Experience in Singapore

We just wrapped up [TOKEN2049](https://www.token2049.com/), and it was an unforgettable experience.
From rubbing shoulders with the brightest minds in blockchain to discussing potential collaborations,
the event was a game-changer for Pactus. The innovation and energy we witnessed have left us more inspired than ever.
This milestone also highlights how far we’ve come since our mainnet launch.
None of this would have been possible without the incredible support from our community.
TOKEN2049 is just the start of something even bigger, and we’re excited for what’s ahead!

### 4 Million Transactions Processed on Pactus

Pactus has processed over 4 million transactions.
This isn't just a statistic; it's a testament to the trust and strength of our growing community.
Every transaction reinforces our commitment to speed, low fees, and scalability.
With your ongoing support, we're ready to tackle the next big milestone.

### Pactus Listed on Azbit Exchange

Pactus is now officially listed on the [Azbit](https://azbit.com/) exchange.
This listing marks another significant step in our mission to make Pactus more accessible to a global audience.
Azbit’s platform offers a user-friendly experience with a wide range of trading pairs,
helping us reach new users and increase liquidity for Pactus.
This is just one of many exciting milestones in our journey toward widespread adoption.
We’re continuing to explore more exchange listings and opportunities to increase visibility for Pactus.

### The New Pactus Website is Live

The brand-new Pactus website is live! With a fresh design, enhanced functionality, and a user-friendly interface.
This revamped platform is built with our community in mind.
Our goal is to make it easier for both newcomers and experienced users to access information, explore Pactus features,
and get involved.
The previous version of the website has been archived and is still accessible at
[https://old.pactus.org/](https://old.pactus.org/).

Explore the new website: [https://pactus.org/](https://pactus.org/).

![Development Report]({{<image "pactus-development-report-september-2024.png" >}})

### Ed25519 Curve Support

In September, we integrated support for the Ed25519 cryptographic curve on the Pactus blockchain.
This brings multiple benefits, including more efficient transaction verification,
as Ed25519 uses less data and operates faster compared to the current BLS signature scheme.
Importantly, Ed25519 is widely adopted by third-party applications, particularly mobile wallets.

With Ed25519 now on our testnet, we aim to enable it on the mainnet in the upcoming v1.5.0 release,
which will introduce a mandatory hard fork for all validators.
Additionally, the team is drafting a proposal to integrate Pactus with
[TrustWallet-Core](https://github.com/trustwallet/wallet-core),
the engine used by [Trust Wallet](https://trustwallet.com/) and other mobile wallets like
[Gem Wallet](https://gemwallet.com/).
This move will open doors for Pactus to be listed on popular third-party platforms,
increasing accessibility for our users.

### TPS Measurement Enhancements

A significant focus this month was on improving the overall performance of the Pactus blockchain.
These optimizations will enable us to measure the true Transactions Per Second (TPS) that Pactus can handle.
We are on track to publish a detailed report on our TPS results soon, showcasing Pactus' scalability potential.

### Python-SDK Release

In an exciting milestone, we released the first version of the
[Pactus Python-SDK](https://github.com/pactus-project/python-sdk).
This toolkit allows developers of all levels to easily interact with the Pactus blockchain using Python,
one of the most popular programming languages.
Supporting both BLS and Ed25519 signature schemes, the SDK simplifies tasks like transaction creation,
signing, and API interactions.
The SDK is available under the MIT license, and developers can start building with it today.

### Pactus Improvement Proposals (PIPs)

Currently, [PIP-31](https://pips.pactus.org/PIPs/pip-31) which introduces the consumptional fee model,
is the most active proposal within the development team.
Scheduled for implementation in version 1.6.0, this model will allow for gas-less transactions,
giving users the option to submit transactions without a fee,
albeit with slower confirmation times compared to fee-paid transactions.

In addition, we are actively discussing
[PIP-32](https://pips.pactus.org/PIPs/pip-32) and
[PIP-33](https://pips.pactus.org/PIPs/pip-33), which address community concerns regarding reserved coins in Pactus.
While we have no plans to move any reserved coins without notifying the community,
we are working on trustless solutions to ensure transparency and maintain confidence within the Pactus ecosystem.
Your feedback on these PIPs is crucial to shaping the future of our blockchain.

### PacViewer updates

The [PacViewer](https://pacviewer.com/) has received some updates over the past month.
Notably it includes address aliasing and [Holder](https://pacviewer.com/holders) page.

[^1]: The Pactus monthly newsletter is published on our website and
distributed to subscribers via email during the first week of each month.
It recaps key highlights and important news from the previous month.
