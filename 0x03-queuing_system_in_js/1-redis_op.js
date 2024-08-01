import { print } from "redis";
const client = require('./0-redis_client');

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (err, value) => {
    console.log(value);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
