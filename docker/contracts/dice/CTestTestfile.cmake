# CMake generated Testfile for 
# Source directory: /eos/contracts/dice
# Build directory: /tmp/build/contracts/dice
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(validate_dice_abi "/tmp/build/scripts/abi_is_json.py" "/eos/contracts/dice/dice.abi")
