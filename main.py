async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ইউআইডি আর্গুমেন্ট নেওয়া হচ্ছে
    if len(context.args) == 0:
        await update.message.reply_text("দয়া করে /profile এর সাথে ইউআইডি লিখো, যেমন: /profile 6681145827")
        return

    user_id = context.args[0]

    # ধরো player_data.json এ তোমার কাছে অনেক প্লেয়ার আছে 'players' নামে লিস্টে
    players = data.get("players", [])

    # ইউআইডি দিয়ে প্লেয়ার খোঁজা
    player = next((p for p in players if p["basicInfo"]["accountId"] == user_id), None)

    if not player:
        await update.message.reply_text(f"কোন প্লেয়ার পাওয়া যায়নি ইউআইডি: {user_id}")
        return

    nickname = player["basicInfo"].get("nickname", "N/A")
    level = player["basicInfo"].get("level", "N/A")
    # ... বাকি তথ্য

    text = f"👤 Nickname: {nickname}\n📊 Level: {level}\n..."
    await update.message.reply_text(text)
