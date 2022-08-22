---
title: Building with Quantum Ledger Database
image: images/posts/building-with-quantum-ledger-database/index.png
date: 2019-12-05T12:01:37+01:00
tags: aws-reinvent-2019
type: "post"
draft: true
---

Last year at re:Invent, [Quantum Ledger Database](https://aws.amazon.com/qldb/) was announced. Amazon QLDB is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log ‎owned by a central trusted authority. In today's workshop, no Python will be used, we're writing Java today. *Yay for curly braces!*

## QLDB fundamentals
The typical database log is hidden for the user, it is used for system things like recovery. It is not immutable, it can be modified by people on the operations team for example. QLDB took a different view on this, they use an append-only journal. You can insert any document model you want since QLDB is a NoSQL database. The inserted documents are appended to the end of the journal as a block. The block also included system information like the date the block was added. This information is also queryable. Whem you first insert a document, it is assigned version 0. When you update the document, the version is increased. When you delete it, the deletion is recorded as a transaction as well.
### Immutable journal
Records can not be altered, there is no API the change things in the journal. All actions, including deletes are written to the journal.
### Cryptographic verification
When data is stored, the document is cryptographically verified and the block hash is stored in the block.
### Ease of use
Documents are stored in Amazon Ion format and are queried using PartiQL *pronounced as 'Party Queue El' (or not, I'm not your mom)*

## PartiQL and Amazon Ion
PartiQL is the query language used in QLDB. To make data easy to move between multiple types of database, one language can be used to query it. It's SQL compatible language with minimal extensions. As stated above, it is format and datastore independent. Most statement and functions that you already know from SQL are supported in PartiQL.
Amazon Ion aims to be effecient in changing data between applications. There is no schema, so it can grow as the application needs. It supports both a human readable text format and a binary format for efficiency. SQL scalar types are covered like numbers and strings. This thing looks like JSON, and as a MongoDB user, this looks promising.

## QLDB and Java
The [Java Driver API](https://github.com/awslabs/amazon-qldb-driver-java) is open-source on GitHub. It does all the cool stuff like session pooling, transaction commit handling and automatic retries for recoverable errors. *The NodeJS and Python drivers are also availble, but why would you even bother?*

## Verification
QLDB generates a sha256 for each document. Use the API of QLDB to verify the documents that exist in the journal. With this, you can make sure that a document has not been altered. So when someone with the wrong data, who claims that they have the right data, you can ask them to prove that their data is right. And they will fail.

## QLDB Streaming **NEW**
Ingest QLDB streams into Kinesis, process it directly with Lambda. Comparable to DynamoDB streams.

{% asset_img summary.jpg "Building applications on Amazon QLDB" %}

### Useful resources
- [PartiQL](https://aws.amazon.com/blogs/opensource/announcing-partiql-one-query-language-for-all-your-data/)
- [Amazon Ion](http://amzn.github.io/ion-docs/)
- [QLDB explained](https://www.youtube.com/watch?v=jcZ_rsLJrqk)
- [Workshop resources](https://github.com/aws-samples/amazon-qldb-dmv-sample-java)
