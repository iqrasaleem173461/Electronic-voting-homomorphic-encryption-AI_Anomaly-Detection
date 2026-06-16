import asyncio
import edge_tts
import os

# Configuration
PAGES = [
    {
        "path": "/",
        "filename": "welcome_home_ur.mp3",
        "text": "خوش آمدید! آپ اس ویب سائٹ کے ذریعے اپنا ووٹ محفوظ اور شفاف طریقے سے ڈال سکتے ہیں۔ رجسٹریشن کے لیے 'رجسٹر' بٹن دبائیں۔"
    },
    {
        "path": "/dashboard",
        "filename": "dashboard_help_ur.mp3",
        "text": "یہ آپ کا ڈیش بورڈ ہے۔ یہاں آپ انتخابات، امیدواروں کی تفصیلات اور اپنے ووٹ کا سٹیٹس دیکھ سکتے ہیں۔"
    },
    {
        "path": "/register",
        "filename": "register_help_ur.mp3",
        "text": "رجسٹریشن کے لیے اپنا شناختی کارڈ نمبر اور موبائل نمبر درج کریں۔ ہم آپ کی معلومات کو نادرا کے ریکارڈ سے تصدیق کریں گے۔"
    },
    {
        "path": "/login",
        "filename": "login_help_ur.mp3",
        "text": "اپنے رجسٹرڈ شناختی کارڈ اور پاس ورڈ کے ساتھ لاگ ان کریں۔"
    },
    {
        "path": "/vote",
        "filename": "vote_help_ur.mp3",
        "text": "ووٹ ڈالنے کے لیے اپنے پسندیدہ امیدوار کا انتخاب کریں اور 'کاسٹ ووٹ' بٹن دبائیں۔ یاد رہے کہ آپ صرف ایک ہی ووٹ ڈال سکتے ہیں۔"
    },
    {
        "path": "/otp",
        "filename": "otp_help_ur.mp3",
        "text": "آپ کے موبائل نمبر پر موصول ہونے والا چھ ہندسوں کا کوڈ درج کر کے اپنی تصدیق مکمل کریں۔"
    },
    {
        "path": "/verify",
        "filename": "verify_help_ur.mp3",
        "text": "نادرا کے ریکارڈ سے تصدیق کے لیے اپنی مکمل تفصیلات فراہم کریں۔"
    }
]

OUTPUT_DIR = os.path.join("..", "backend", "public", "uploads", "guides")
VOICE = "ur-PK-UzmaNeural"

async def generate():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    for page in PAGES:
        print(f"Generating audio for {page['path']}...")
        output_path = os.path.join(OUTPUT_DIR, page['filename'])
        
        communicate = edge_tts.Communicate(page['text'], VOICE)
        await communicate.save(output_path)
        print(f"Saved: {output_path}")

if __name__ == "__main__":
    asyncio.run(generate())
