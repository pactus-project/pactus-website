+++
title = "Energy Efficiency of Pactus"
description = ""
author = "Pactus Team"
date = 2024-12-29T16:10:34+01:00
tags = ["announcement", "release"]
image = "energy-efficiency-of-pactus.png"
+++
Through our innovative architecture and operational mechanisms, Pactus
demonstrates remarkable energy efficiency.​ Pactus blockchain has the
strength to utilize low-power devices, such as Raspberry Pi Zero,
which consumes only 2 watts of power. This contrasts with
traditional blockchain networks, which depend on energy-intensive
mining rigs and high-specification servers.

By integrating personal computers and shared Virtual Private Servers (VPS),
Pactus ensures a balance between energy efficiency and high performance,
thereby minimizing the environmental impact and fostering a more
democratic network participation model.

## What is SSPoS
The SSPoS consensus model adopted by Pactus is essential to its
energy-efficient framework. This model includes a fixed committee
of 51 validators that changes over time, limiting the number of
participants and reducing the volume of messages exchanged
during the consensus process—such restrictions
effectively lower energy consumption while ensuring
robust security and scalable operations.

## Understanding Sortition Algorithm 
The Sortition Algorithm is a cornerstone of Pactus, enabling the
equitable and randomized selection of validators for the committee.
By leveraging a VRF, the algorithm generates a random value between
0 and the total staked coins. Validators qualify for committee membership
if their assigned number falls below their stake. Upon including
their sortition transaction in a block, they replace the
longest-serving committee member.

Pactus leverages pruned nodes to significantly reduce storage
needs by retaining only the last 10 days of blocks.
This streamlined approach enables new validators to sync in
approximately 15 minutes, enhancing accessibility for users with
lower-end hardware and expanding participation.
Moreover, we incorporate an optimized messaging system
with ten simplified message types and deterministic serialization,
effectively reducing network traffic and computational demands.

Stay tuned for more information
