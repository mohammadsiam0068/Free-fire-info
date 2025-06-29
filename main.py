from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json

# 🔐 তোমার BotFather থেকে পাওয়া টোকেন এখানে বসাও
BOT_TOKEN = "7940124369:AAHsl3z8awdJ7L651zSBUNbLeNO80eTTKdg"

# 📄 JSON ফাইল থেকে প্রোফাইল ডেটা লোড করছে
with open("player_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# /start কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 হ্যালো! /profile লিখে তোমার Free Fire প্রোফাইল দেখো!")

# /profile কমান্ড হ্যান্ডলার
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    player = data["player_info"]["basicInfo"]
    clan = data["player_info"]["clanBasicInfo"]
    
    nickname = player.get("nickname", "N/A")
    level = player.get("level", "N/A")
    rank = player.get("rank", "N/A")
    cs_rank = player.get("csRank", "N/A")
    region = player.get("region", "N/A")
    likes = player.get("liked", 0)

    clan_name = clan.get("clanName", "N/A")
    clan_level = clan.get("clanLevel", "N/A")
    clan_members = clan.get("memberNum", "N/A")

    text = f"""🎮 [Free Fire Profile]
👤 Nickname: {nickname}
📊 Level: {level}
🏅 BR Rank Code: {rank}
🎯 CS Rank Code: {cs_rank}
❤️ Likes: {likes}
🌍 Region: {region}

👥 Clan: {clan_name}
⭐ Clan Level: {clan_level}
👤 Members: {clan_members}
"""
    await update.message.reply_text(text)

# বট অ্যাপ তৈরি ও হ্যান্ডলার রেজিস্টার
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("profile", profile))

# বট চালু
print("🤖 Bot is running...")
app.run_polling()
