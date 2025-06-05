+++
title = "The Risk of Running Duplicated Nodes"
author = "Pactus Team"
date = 2024-12-04T00:00:00+00:00
tags = ["tutorial"]
image = "duplicate-nodes.png"
+++

## Summary

Some node operators in the Pactus network mistakenly believe that running multiple identical nodes
will increase their chances of earning more rewards.
However, this approach not only fails to increase their income but can also reduce their rewards.

For instance, a validator attempted to run seven identical nodes in different locations, expecting higher rewards.
The result, however, was the opposite of what they hoped for.
When considering the cost of running multiple machines, their rewards ended up decreasing instead of increasing.

## What Are Duplicated Nodes?

In the Pactus network, nodes are identified by two keys:

1. **Network Key:**
   The network key assigns an ID to the node and encrypts its messages within the peer-to-peer (P2P) network.
   It plays no role in the consensus algorithm, meaning a node operator can delete the `network_key` file,
   and Pactus will generate a new one for that node.
   However, this practice is not recommended, especially for bootstrap validators.

2. **Validator Keys:**
   Each node can be associated with one or more validator keys,
   which uniquely identify the validators within the consensus algorithm.
   These keys cannot be changed arbitrarily, as the consensus algorithm relies on them to track and
   verify the actions of each validator.

A duplicated node is defined as a node that shares the same validator keys but
uses a different network key and operates on a different machine.

## Why Are Duplicated Nodes Problematic?

Running duplicated nodes results in duplicate votes and double proposals in the consensus algorithm.
Pactus is designed to identify and reject such invalid inputs.

For instance, a duplicated node might send two proposals simultaneously,
each with different block data (e.g., different sets of transactions).
This scenario, known as double proposing, creates conflicting proposals.

In this situation, some validators vote for the first proposal, while the rest vote for the second.
This disagreement makes it unlikely for either proposal to gather enough votes to reach consensus.
As a result, the validator loses the opportunity to finalize their block and misses out on potential rewards.

## Network Disruption

Duplicated nodes may become unsynced with the network and start broadcasting expired or duplicated messages.
This can cause the consensus process to require more messages to reach an agreement,
and in some cases, it might trigger a snowball effect.

To mitigate this issue, Pactus has introduced a solution: nodes automatically discard messages related to past blocks.
This ensures that expired messages are contained and only affect a small group of neighboring nodes,
preventing widespread disruption.
