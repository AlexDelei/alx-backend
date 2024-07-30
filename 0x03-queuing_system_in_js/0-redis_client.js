import { createClient } from "redis";

const client = await createClient()
  .on('error', error => console.log(`Redis client not connected to the server: ${error}`))
  .connect()