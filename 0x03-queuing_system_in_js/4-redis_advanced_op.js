import { print } from "redis";
const client = require('./0-redis_client');

client.HSET('HolbertonSchools', 'Portland', 50, print);
client.HSET('HolbertonSchools', 'Seattle', 80, print);
client.HSET('HolbertonSchools', 'New York', 20, print);
client.HSET('HolbertonSchools', 'Bogota', 20, print);
client.HSET('HolbertonSchools', 'Cali', 40, print);
client.HSET('HolbertonSchools', 'Paris', 2, print);

client.HGETALL('HolbertonSchools');
