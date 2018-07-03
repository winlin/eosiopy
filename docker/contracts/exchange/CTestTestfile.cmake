# CMake generated Testfile for 
# Source directory: /eos/contracts/exchange
# Build directory: /tmp/build/contracts/exchange
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(validate_exchange_abi "/tmp/build/scripts/abi_is_json.py" "/eos/contracts/exchange/exchange.abi")
