# Getting Started

## Step 1: Generate a Lightning Wallet & API Key

> **Tip:**  
> A Lightning wallet is specifically designed for ultra-fast transactions, making it ideal for use cases like a sniper bot.

### Create Your Wallet and API Key

Run `generate_wallet.py` to generate your wallet. The script will output your wallet details, including:  
- **API Key**  
- **Public Wallet Address**  
- **Private Key**  

### Important Information:  
**Secure Your Keys**  
- **Private Key:** Save your private key securely. You can restore your wallet at any time using this key and withdraw funds. However, anyone with access to your private key can do the same.  
- **API Key:** Securely store your API key. Anyone with your API key can trade using the funds in your wallet.

**Key Management Notes:**
- Your keys will disappear once you navigate away from this or rerun `generate_wallet.py` to create a new wallet and API key.  
- **Keys cannot be recovered if lost.**

---

## Step 2: Fund Your Wallet

Send any amount of SOL to the **public key** address of the wallet you created above.

---

## You're Ready to Trade!  
With your wallet funded, you can now trade using this bot. Run `main.py` to get started.
