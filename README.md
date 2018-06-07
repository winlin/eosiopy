# About/关于

**EosioPy** is a python EOS tool,which is developed by  Gao jinfeng

**EosioPy**是一个python eos工具集合。

-------------------------------



### Installation/安装

EosioPy requires to run python3.6+.


```sh
$ pip instll eosiopy
```


### Simple to use/简单使用
你可以执行任何eosio支持的合约[eosio官方文档](https://eosio.github.io/eos/group__contractdev.html)

You can perform any contract supported by eosio[eosio Official documents](https://eosio.github.io/eos/group__contractdev.html)

```python
from eosiopy.eosioparams import EosioParams
from eosiopy.nodenetwork import NodeNetwork
from eosiopy.rawinputparams import RawinputParams
raw = RawinputParams("transfer", {
        "from": "eosio.token",
        "memo": "dd",
        "quantity": "20.0000 EOS",
        "to": "eosio"
    }, "eosio.token", "eosio.token@active")

eosiop_arams=EosioParams(raw.eos_params,"5K7vdq9bEpTGZMryrc4LwcxeHAwMcrFuwskVujujpAfBoJwAo82")
net=NodeNetwork.push_transaction(eosiop_arams.trx_json)
print(net)
```


### Change config/更改默认配置

You can change the default node address before sending the request (default is 127.0.0.1:8888)

你可以在发送请求之前更改默认的节点地址(默认是 127.0.0.1:8888)

### Use the advanced/进阶使用
You can also generate all parameters manually without using the default parameters.

你也可以不使用默认参数生成，手动生成所有参数
```python
from eosiopy.eosioparams import EosioParams
from eosiopy.nodenetwork import NodeNetwork
﻿params={
    "available_keys": [
        "EOS7yq2yoio7zBhMMjKR41iTun4P86gyq5bi8fXgy6X3FvH4CwKp6",
        "EOS8hdhrncnn1fKk21iHb7g9F8Q7MGa3VdfDiYEffqVeNVgo9iJ5K"
    ],
    "transaction": {
        "actions": [
            {
                "account": "eosio.token",
                "authorization": [
                    {
                        "actor": "eosio.token",
                        "permission": "active"
                    }
                ],
                "data": "00a6823403ea305500e1f505000000000445455300000000046d656d6f",
                "name": "issue"
            }
        ],
        "context_free_actions": [
        ],
        "context_free_data": [
        ],
        "delay_sec": 0,
        "expiration": 1527587389,
        "max_cpu_usage_ms": 0,
        "max_net_usage_words": 0,
        "ref_block_num": 26471,
        "ref_block_prefix": 519107831,
        "signatures": [
        ]
    }
}
eosiop_arams=EosioParams(﻿params,"5K7vdq9bEpTGZMryrc4LwcxeHAwMcrFuwskVujujpAfBoJwAo82")
net=NodeNetwork.push_transaction(eosiop_arams.trx_json)
print(net)
```
###LICENSE/版权

**License**

Released under GNU General Public License v3.0
