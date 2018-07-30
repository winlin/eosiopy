import unittest

from eosiopy import NodeNetwork, RawinputParams, EosioParams


class EosioPyTestCase(unittest.TestCase):
    def test_get_info(self):
        info = NodeNetwork.get_info()
        self.assertTrue(isinstance(info, dict))
        block = NodeNetwork.get_block(1)
        self.assertTrue(isinstance(block, dict))

    def test_newaccount(self):
        raw = RawinputParams("newaccount", {"creator": "eosio", "name": "aeztcnjmhege", "owner": {"threshold": 1,
                                                                                                  "keys": [{
                                                                                                      "key": "EOS5XhYEWPJH2P77rh6dwMURsgjFodjXqTadSf1tNZAHVhnBpWyNu",
                                                                                                      "weight": 1}],
                                                                                                  "accounts": [],
                                                                                                  "waits": []},
                                            "active": {"threshold": 1, "keys": [
                                                {"key": "EOS7EZgfh13yVxaXuzH12cC2Yru7Wv1JNNNbxnSdZQXNX2hWAyBTm",
                                                 "weight": 1}], "accounts": [], "waits": []}}, "eosio", "eosio@active")
        eosiop_arams = EosioParams(raw.params_actions_list, "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3")
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        self.assertTrue(isinstance(net, dict))
        self.assertNotEqual(net.get("transaction_id", None), None)
        raw = RawinputParams("newaccount", {"creator": "eosio", "name": "aeztcnmmhege", "owner": {"threshold": 1,
                                                                                                  "keys": [{
                                                                                                      "key": "EOS5XhYEWPJH2P77rh6dwMURsgjFodjXqTadSf1tNZAHVhnBpWyNu",
                                                                                                      "weight": 1}],
                                                                                                  "accounts": [],
                                                                                                  "waits": []},
                                            "active": {"threshold": 1, "keys": [
                                                {"key": "EOS7EZgfh13yVxaXuzH12cC2Yru7Wv1JNNNbxnSdZQXNX2hWAyBTm",
                                                 "weight": 1}], "accounts": [], "waits": []}}, "eosio", "eosio@active")
        eosiop_arams = EosioParams(raw.params_actions_list, "5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3")
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        self.assertTrue(isinstance(net, dict))
        self.assertNotEqual(net.get("transaction_id", None), None)


if __name__ == '__main__':
    unittest.main()
