# Satoru Bot

Satoru Bot is a Telegram bot that provides daily horoscope readings based on zodiac signs. Users can ask for their horoscope for today, tomorrow, or any specific date.

```bash
  Telegram username: satoru_telbot
```
    
## Features

- **Start / Hello Command**: Initiates a conversation with the bot.
- **Horoscope Command**: Allows users to request their horoscope.
- **Zodiac Sign Selection**: Users can choose their zodiac sign from a list.
- **Date Selection**: Users can specify the date they want the horoscope for.
- **Horoscope Fetching**: Fetches daily horoscope from an external API.
- **Error Handling**: Handles errors gracefully in case the horoscope cannot be fetched.

## Usage

1. Start a conversation with the bot by sending `/start` or `/hello`.
2. Use the `/horoscope` command to request your horoscope.
3. Follow the prompts to select your zodiac sign and specify the date.
4. Receive your daily horoscope!

## Installation

1. Clone the repository:

```bash
git clone https://github.com/aastik7/Satoru-Bot.git
cd Satoru-Bot

```


2. Install the required dependencies:

```bash
pip install python-telegram-bot requests python-dotenv
```

3. Set up your environment variables. Create a `.env` file in the root directory and add your Telegram bot token:

```
BOT_TOKEN=your_telegram_bot_token
```

4. Run the bot:

```bash
python bot.py
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## Credits

This bot was created by [Aastik](https://github.com/aastik7).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Make sure to replace `your_telegram_bot_token` with your actual Telegram bot token, and update any other placeholders with the appropriate information.
