const fs = require('fs');
const fetch = require('node-fetch');

async function getHosts() {
  let response = await fetch('https://one.cgm.im/api/hosts');
  let data = await response.json();
  return data;
}

getHosts().then((data) =>
  fs.writeFileSync('src/data/hosts.json', JSON.stringify(data, null, 2)),
);
