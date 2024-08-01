import { promisify } from 'util';
import { createClient, print } from "redis";

const client = createClient();
const promisifyClient = promisify(client.GET);

client.on('error', error => console.log(`Redis client not connected to the server: ${error}`));

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

const getAsync = promisify(client.GET).bind(client);

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.log(error)
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
