+++
title = "Sandbox dApps on Pactus"
description = """
"""
author = "Pactus Team"
date = "2026-03-19T00:00:00"
tags = ["dapps", "smart contract"]
image = "pactus-sandbox-dapps.png"
+++

We are often asked about Pactus's plan for smart contracts, and it's an important question.
Pactus does have a plan to introduce a smart contract engine,
but it will differ from the typical smart contract platforms we’re familiar with. The reason is simple:
adopting the same concepts without bringing something new or
addressing existing issues won’t lead to meaningful progress.
In this article, we’ll explain the general idea and vision for smart contracts on Pactus.
Our goal is to keep the explanation straightforward and simple, but first,
let’s revisit a fundamental question: What is a smart contract?

## Smart Contract

What we call a "Smart Contract" is neither truly "smart" nor a "contract" in the traditional sense.
It’s simply a piece of code that runs when a transaction is included in a block.

This extends the blockchain’s functionality beyond just maintaining account balances;
it allows the blockchain to securely execute applications, which we refer to as decentralized applications, or dApps.

But how exactly do we "**execute an application**" on the blockchain?
To answer this, we need to understand something known as a stack machine.

## Stack machine

A [stack machine](https://en.wikipedia.org/wiki/Stack_machine) is a simple way to execute tasks in a specific order.
Imagine a stack as an empty container where you can either push plates into it or pop plates out.
Some of these plates are special; they're called operation codes (OPcodes) and they can interpret and
manipulate the items in the stack, such as performing addition.
Each OPcode is designed to carry out a specific function, enabling us to execute applications through this process.

![Stack Machine]({{<image "stack-machine.png">}})

In the context of blockchain, a stack machine provides an efficient way to
run dApps because it ensures that each step is executed securely and in the correct sequence.

## Bitcoin Stack Machine

Bitcoin uses a simple stack-based scripting system for executing transactions.
[Bitcoin Script](https://en.bitcoin.it/wiki/Script) runs within the Bitcoin stack machine.
Each transaction is executed and validated through this stack machine.
The Bitcoin stack machine is designed to be simple, secure, and efficient;
however, it lacks support for certain operations, such as loops and conditional statements,
and it does not offer persistent memory or storage.
One way to overcome these limitations is to extend the stack machine to support storage and
add more OPcodes.
This is what Ethereum achieved with the introduction of the Ethereum Virtual Machine (EVM).

## Ethereum Virtual Machine

The [Ethereum Virtual Machine (EVM)](https://ethereum.org/en/developers/docs/evm/) is
a stack-based machine that can run any kind of program.
It has all the necessary [OPCodes](https://www.evm.codes/) to execute applications,
as long as there is sufficient time and resources.

The EVM also has persistent memory, which lets it save and
load data on the blockchain. To use the EVM, the Ethereum team created a
programming language called [Solidity](https://soliditylang.org/).
The Solidity compiler turns human-readable code into machine code that the EVM can run.

The EVM may look like a good option at first, but as you get closer,
it starts to resemble a mirage, revealing many
[faults and shortcomings](https://earlz.medium.com/the-faults-and-shortcomings-of-the-evm-bde4d09b8b6a).
While the Bitcoin stack machine is designed to be simple, the EVM is quite complicated.
Its internal design is inefficient,
which led Ethereum to define [precompiled contracts](https://www.evm.codes/precompiled),
an anti-design pattern that further complicates the EVM.

Additionally, maintaining Solidity requires a huge amount of effort and resources.
This raises the question: can we use another stack-based machine? This is where WebAssembly comes in.

## WebAssembly

[WebAssembly (WASM)](https://webassembly.org/) is also a stack-based language designed to
run applications in major browsers.
Many programming languages, such as C++ and Rust, can be used to write WebAssembly code.
However, there is one significant problem: WebAssembly is not specifically designed for blockchain;
it is intended for running applications in a browser.

Nevertheless, this should not deter us from considering it.
With some small modifications, we can adapt WebAssembly for use outside the browser.
This is why many blockchains tend to use WebAssembly.

It seems we have a promising option here. However, we still have one unsolved issue: storage.

## Storage

In most blockchains, storage is handled inside a database.
Each piece of data is labeled with a key, allowing it to be retrieved later using the same key.
However, using a database to store application data is neither simple nor efficient.
Managing data over time can be impractical, and the cost of storing data is high.
This is why storage in blockchains can be expensive.

![Ethereum Storage]({{<image "ethereum-storage.png">}})

If we can keep these costs down or reduce them, we may be able to make blockchain applications
more accessible and cost-effective for developers and users alike.
This is where Pactus offers an innovative solution: storage as a file.

## Storage as File

Decentralized storage is expensive because all nodes in the blockchain need to maintain a copy of the data.
In contrast, centralized storage platforms can often provide more cost-effective solutions.
However, decentralized storage is safe and secure, effectively eliminating **trust** issues.
Additionally, it enhances data **availability and resilience**; even if some nodes go offline, the data remains accessible.

The solution Pactus offers is a dedicated storage file for each dApp, where everything related to the application,
including code and data, will be saved in a single file. This approach allows us to have isolated and **sandbox dApps**.

![Storage as File]({{<image "contract-storage-file.png">}})

## Sandbox dApp

Applications on the Pactus blockchain will be sandboxed, meaning each application exists inside a dedicated file.
All application code and data are contained within this file.
This allows users to purchase dedicated storage, such as 10 MB of data, and store their information accordingly.

![Pactus Sandbox dApp]({{<image "pactus-sandbox-dapp.png">}})

Similar to centralized storage platforms, users pay based on their needs.
The storage file is renewable; it is not permanent, and once it expires, it will be deleted.
Deleting a file simply means purging all data and code associated with a dApp.

## Real World Application

For developers, what’s important is how simple it is to develop a dApp on Pactus, and for end users,
how affordable it is to deploy one.
Pactus aims to address both of these issues.
So far, most smart contracts on Ethereum and other blockchains do not tackle real-world problems.
We have many examples of tokenized applications, but few examples of applications that address actual needs.

Pactus can turn the page by enabling the deployment of simple and secure applications that solve real-world issues.
For example, we can create a decentralized password manager.
Each wallet in Pactus can have a dedicated decentralized file that stores passwords in an encrypted format.
No one can decrypt these passwords except the wallet owner.
To recover passwords, users only need to recover their wallets.
This illustrates how the Pactus Layer-2 will function.
