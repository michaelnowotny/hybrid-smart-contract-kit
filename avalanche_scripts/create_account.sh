curl --location --request POST '127.0.0.1:9650/ext/keystore' \
--header 'Content-Type: application/json' \
--data-raw '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"keystore.createUser",
    "params" :{
        "username": "Avalanche",
        "password": "Ava-123;X5"
    }
}'

curl --location --request POST '127.0.0.1:9650/ext/bc/X' \
--header 'Content-Type: application/json' \
--data-raw '{
    "jsonrpc":"2.0",
    "id"     :1,
    "method" :"avm.importKey",
    "params" :{
        "username": "Avalanche",
        "password": "Ava-123;X5",
        "privateKey":"PrivateKey-ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN"
    }
}'

curl --location --request POST '127.0.0.1:9650/ext/bc/C/avax' \
--header 'Content-Type: application/json' \
--data-raw '{
    "method": "avax.importKey",
    "params": {
        "username": "Avalanche",
        "password": "Ava-123;X5",
        "privateKey":"PrivateKey-ewoqjP7PxY4yr3iLTpLisriqt94hdyDFNgchSxGGztUrTXtNN"
    },
    "jsonrpc": "2.0",
    "id": 1
}'
