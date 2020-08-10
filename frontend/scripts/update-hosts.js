const fs = require('fs');
const fetch = require('node-fetch');

async function getHosts() {
  // TODO: update url
  let response = await fetch('http://one.cgm.im:8000/api/hosts');
  let data = await response.json();
  return data;
}

getHosts().then((data) =>
  fs.writeFileSync('src/data/hosts.json', JSON.stringify(data, null, 2)),
);
