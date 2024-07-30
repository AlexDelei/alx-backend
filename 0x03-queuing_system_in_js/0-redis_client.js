import { createClient } from "redis";

const client =  createClient();
client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));

if (client.connected()) {
  console.log('Redis client connected to the server');
};
