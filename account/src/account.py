import json

with open("output.txt","r",encoding="utf-8") as f:
  address = f.read()
address = address.split("pubkey: ")[1].split("\n")[0]

with open("secret.json","r",encoding="utf-8") as f:
  secret = json.load(f)

print(json.dumps({
  "address":address,
  "private_key":secret
}))