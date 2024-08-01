### Learning objectives
1. How to run a Redis server on your machine
2. How to run simple operations with the Redis client
3. How to use a Redis client with Node JS for basic operations
4. How to store hash values in Redis
5. How to deal with async operations with Redis
6. How to use Kue as a queue system
7. How to build a basic Express app interacting with a Redis server
8. How to the build a basic Express app interacting with a Redis server and queue


**Entity** - An entity is a class that holds your data when you work with it.
**Schema** - A schema defines the fields on your entity, their types and how they are mapped internally

## What is Redis ?
- __Redis (REmote DIctionary Server)__ is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, and geospatial indexes with radius queries.

Redis is widely used in **web applications** for:
1. caching
2. session storage
3. real-time analytics
4. message queuing
5. a general-purpose NoSQL database.

Its speed and versatility make it a popular choice for developers looking to build high-performance applications.

#### <u>Here are some key features of Redis:</u>

1. **In-Memory Storage:** Redis stores data in memory, which allows for very fast read and write operations. This makes it an excellent choice for caching frequently accessed data.

2. **Persistence:** Although Redis is an in-memory database, it supports persistence by allowing you to dump the dataset to disk periodically or append each command to a log.

3. **Data Structures:** Redis supports a rich set of data types, including:

    - Strings: Simple key-value pairs.
    - Lists: Ordered collections of strings.
    - Sets: Unordered collections of unique strings.
    - Sorted Sets: Sets ordered by a score.
    - Hashes: Collections of key-value pairs.
    - Bitmaps and Bitfields: For bit-level operations.
    - HyperLogLogs: For approximating the cardinality of sets.
    - Geospatial Indexes: For storing and querying geospatial data.

4. **Atomic Operations:** Redis operations are atomic, meaning that they are completed entirely or not at all, which is critical for maintaining data consistency.

5. **Pub/Sub Messaging:** Redis supports publish/subscribe messaging, which allows clients to subscribe to channels and receive messages when new data is published.

6. **Replication and High Availability:** Redis supports master-slave replication, allowing data to be replicated across multiple servers. It also supports Redis Sentinel for high availability and monitoring.

7. **Redis Cluster:** Redis Cluster provides a way to run a Redis installation where data is automatically sharded across multiple Redis nodes.
