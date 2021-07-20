from web3 import Web3
import json
from tqdm import tqdm

abi = """[{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_rewardsDistribution","type":"address"},{"internalType":"address","name":"_rewardsToken","type":"address"},{"internalType":"address","name":"_stakingToken","type":"address"},{"internalType":"uint258","name":"_startEmission","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerNominated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"isPaused","type":"bool"}],"name":"PauseChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Recovered","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"reward","type":"uint256"}],"name":"RewardAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"reward","type":"uint256"}],"name":"RewardPaid","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"newDuration","type":"uint256"}],"name":"RewardsDurationUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Staked","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"StartEmissionUpdated","type":"uint256"}],"name":"StartEmissionUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdrawn","type":"event"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"earned","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"exit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getRewardForDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastPauseTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastTimeRewardApplicable","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lastUpdateTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"nominateNewOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"nominatedOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"reward","type":"uint256"}],"name":"notifyRewardAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"periodFinish","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256","name":"tokenAmount","type":"uint256"}],"name":"recoverERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rewardPerToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardPerTokenStored","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardRate","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"rewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardsDistribution","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardsDuration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewardsToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_paused","type":"bool"}],"name":"setPaused","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_rewardsDistribution","type":"address"}],"name":"setRewardsDistribution","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_rewardsDuration","type":"uint256"}],"name":"setRewardsDuration","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_startEmission","type":"uint256"}],"name":"setStartEmission","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"stake","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"stakingToken","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startEmission","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"timestamp","type":"uint256"}],"name":"updatePeriodFinish","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userRewardPerTokenPaid","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]"""
web3 = Web3(Web3.HTTPProvider("https://eth-mainnet.alchemyapi.io/v2/Hu4cG7pHmFEg47MtltDPCOTH50sbNIv4"))
stETH = web3.eth.contract(abi=abi, address="0xd46f9546ebAbAAC44DC1B6D0Ac1eeb357D34FBeB")
stWBTC = web3.eth.contract(abi=abi, address="0x1d27a3A92330693B897db9B1C26290Ba381049b1")
stUSDC = web3.eth.contract(abi=abi, address="0xe79734461499246b6A8C8e768B96bebd0C891f63")

save_intermediate_values = True

ethRewards = {} 
with open("./ETHStakers.json") as f:
    data = json.loads(f.read())
for datum in tqdm(data):
    if datum['user'].lower() in ethRewards:
        continue 
    reward = stETH.functions.earned(datum['user']).call({}, block_identifier=12850000)
    ethRewards[datum['user'].lower()] = reward
if save_intermediate_values:
    with open("./stETHRewards.json", "w+") as f:
        f.write(json.dumps(ethRewards))

wbtcRewards = {} 
with open("./WBTCStakers.json") as f:
    data = json.loads(f.read())
for datum in tqdm(data):
    if datum['user'].lower() in wbtcRewards:
        continue
    reward = stWBTC.functions.earned(datum['user']).call({}, block_identifier=12850000)
    wbtcRewards[datum['user'].lower()] = reward
if save_intermediate_values:
    with open("./stWBTCRewards.json", "w+") as f:
        f.write(json.dumps(wbtcRewards))

usdcRewards = {} 
with open("./USDCStakers.json") as f:
    data = json.loads(f.read())
for datum in tqdm(data):
    if datum['user'].lower() in usdcRewards:
        continue
    reward = stUSDC.functions.earned(datum['user']).call({}, block_identifier=12850000)
    usdcRewards[datum['user'].lower()] = reward
if save_intermediate_values:
    with open("./stUSDCRewards.json", "w+") as f:
        f.write(json.dumps(usdcRewards))

ETH_RBN_allocation = 3071165 * 10**18
WBTC_RBN_allocation = 3047369 * 10**18
USDC_RBN_allocation = 3881466 * 10**18

ethTotalRewards = sum(ethRewards.values())
wbtcTotalRewards = sum(wbtcRewards.values())
usdcTotalRewards = sum(usdcRewards.values())

totalRBN = usdcTotalRewards + wbtcTotalRewards + ethTotalRewards

assert(totalRBN < ETH_RBN_allocation + WBTC_RBN_allocation + USDC_RBN_allocation)


ETHleftoverRBN  = (ETH_RBN_allocation - ethTotalRewards) / 10**18
WBTCleftoverRBN = (WBTC_RBN_allocation - wbtcTotalRewards) / 10**18
USDCleftoverRBN = (USDC_RBN_allocation - usdcTotalRewards) / 10**18

print(f"Total RBN: {totalRBN / 10**18}")
print(f"ETH RBN remaining: {ETHleftoverRBN}")
print(f"WBTC RBN remaining: {WBTCleftoverRBN}")
print(f"USDC RBN remaining: {USDCleftoverRBN}")

disperse_payouts = {}
vault_bonuses = [ 
    ETHleftoverRBN / (ETH_RBN_allocation / 10**18),
    WBTCleftoverRBN / (WBTC_RBN_allocation / 10**18),
    USDCleftoverRBN / (USDC_RBN_allocation / 10**18),
]

print(f"ETH bonus: {vault_bonuses[0]}")
print(f"WBTC bonus: {vault_bonuses[1]}")
print(f"USDC bonus: {vault_bonuses[2]}")

for vault, bonus in zip([ethRewards, wbtcRewards, usdcRewards], vault_bonuses):
    for account, reward_amount in vault.items():
        if reward_amount:
            disperse_payouts[account] = disperse_payouts.setdefault(account, 0) + \
                                            reward_amount * bonus
disperse_payouts = {k:v/10**18 for k, v in disperse_payouts.items()}

data = {
    "totalRBN":totalRBN,
    "ETH Total Rewards": ethTotalRewards,
    "ETH Rewards": ethRewards,
    "WBTC Total Rewards": wbtcTotalRewards,
    "WBTC Rewards": wbtcRewards,
    "USDC Total Rewards": usdcTotalRewards,
    "USDC Rewards": usdcRewards,
}

with open("./rewardSummary.json", 'w+') as f:
    f.write(json.dumps(data))

with open("./disperse_payouts.json", 'w+') as f:
    f.write(json.dumps(disperse_payouts))
