# Fivem Status Bot

![GitHub](https://img.shields.io/github/license/AdarshSudo/Fivem-status-bot)
![GitHub issues](https://img.shields.io/github/issues/AdarshSudo/Fivem-status-bot)
![GitHub forks](https://img.shields.io/github/forks/AdarshSudo/Fivem-status-bot)
![GitHub stars](https://img.shields.io/github/stars/AdarshSudo/Fivem-status-bot)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/AdarshSudo/Fivem-status-bot)

A Discord bot for monitoring the status of your FiveM servers and providing various utility commands.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands](#commands)

## Introduction

[Fivem-status-bot](https://github.com/YourGitHubUsername/Fivem-status-bot) is a Discord bot designed to keep you informed about the status of your FiveM servers. It also includes utility commands for managing your Discord server. The bot is built using Python and the Discord API.

## Features

- Real-time monitoring of your FiveM servers.
- Notifications on server status changes.
- Utility commands for managing your Discord server.
- Customizable server status messages.
- Easy-to-use Discord bot commands.

## Prerequisites

Before setting up and running the bot, make sure you have the following:

- [Python](https://www.python.org/) installed on your server.
- A Discord bot token. You can create one through the [Discord Developer Portal](https://discord.com/developers/applications).
- The necessary Python packages (`discord`, `asyncio`, `requests`) installed.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YourGitHubUsername/Fivem-status-bot.git


## Configuration

1. Navigate to the project directory:

   ```bash
   cd Fivem-status-bot
   ```

2.Install the required Python packages:

   ```bash
   pip install discord asyncio requests
   ```

3.Configure the bot by editing the config class in the main.py file. Provide your Discord bot token, FiveM server IP and port, and Discord server ID.



## Usage

   ```bash
   python main.py
   ```
   

## Commands

Commands

    -say (or -s) [text]: Make the bot send an embedded message with your specified text.
    -hsay (or -hs) [text]: Send a hidden message as the bot.
    -pid [player_id]: Look up a player by their FiveM ID and display their information.
    -run: Display instructions for starting the FiveM server.
    -help: Show a list of available bot commands.
    -players: List online players on the FiveM server.
    -ip [ip_address]: Look up information about an IP address using the IP-API.

Please make sure your Discord bot has the necessary permissions to execute these commands.




