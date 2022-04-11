from brownie import network
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    fund_with_link,
)
from scripts.deploy_lottery import deploy_lottery
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    print(f"lottery = deploy_lottery()")
    lottery = deploy_lottery()
    print(f"account = get_account()")
    account = get_account()
    print(f"lottery.startLottery")
    lottery.startLottery({"from": account})
    print(f"entering lottery 1")
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    print(f"entering lottery 2")
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    print(f"fund_with_link(lottery)")
    fund_with_link(lottery)
    print(f" lottery.endLottery")
    lottery.endLottery({"from": account})
    print(f"time.sleep(10)")
    time.sleep(10)
    print(f"Assert")
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
