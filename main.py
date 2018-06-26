from eosiopy.eosioparams import EosioParams
from eosiopy.nodenetwork import NodeNetwork
from eosiopy.rawinputparams import RawinputParams
from eosiopy import eosio_config
eosio_config.url="http://47.93.213.164"
eosio_config.port=8888
raw = RawinputParams("transfer", {
        "from": "eosio.token",
        "memo": "eosmoto",
        "quantity": "20.0000 EOS",
        "to": "eosio"
    }, "eosio.token", "eosio.token@active")

eosiop_arams=EosioParams(raw.params_actions_list,"5K7vdq9bEpTGZMryrc4LwcxeHAwMcrFuwskVujujpAfBoJwAo82")
net=NodeNetwork.push_transaction(eosiop_arams.trx_json)
print(net)