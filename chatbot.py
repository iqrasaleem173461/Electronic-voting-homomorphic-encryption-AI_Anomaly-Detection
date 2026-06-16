import spacy

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

def get_chatbot_response(message, language='ur'):
    msg = message.lower()
    
    if language == 'ur':
        # Conversational Urdu Responses
        if any(word in msg for word in ["hello", "hi", "salam", "سلام", "hey"]):
            return "Assalam-o-Alaikum! Main SecureVote ka digital assistant hoon. Main aapki kya madad kar sakta hoon? Aap mujhse vote daalne ya registration ke baare mein pooch sakte hain."

        if any(word in msg for word in ["vote", "ووٹ", "cast", "daal"]):
            return "ووٹ ڈالنا بہت آسان ہے۔ پہلے لاگ ان کریں، پھر ڈیش بورڈ پر جا کر فعال الیکشن منتخب کریں۔ اپنے پسندیدہ امیدوار پر کلک کریں اور تصدیق کر دیں۔ آپ کا ووٹ مکمل طور پر خفیہ اور محفوظ رہے گا۔"
            
        if any(word in msg for word in ["register", "رجسٹر", "account", "بنا", "sign"]):
            return "رجسٹریشن کے لیے آپ کو اپنا نام، CNIC نمبر اور موبائل نمبر دینا ہوگا۔ ہم آپ کی معلومات کی تصدیق نادرہ سے کرتے ہیں تاکہ الیکشن میں کوئی غلطی نہ ہو۔"

        if any(word in msg for word in ["security", "محفوظ", "fraud", "حفاظت", "safe"]):
            return "ہمارا سسٹم دنیا کے جدید ترین سیکیورٹی پروٹوکولز پر مبنی ہے۔ ہم آرٹیفیشل انٹیلیجنس کا استعمال کرتے ہیں تاکہ کسی بھی قسم کے فراڈ کو روکا جا سکے۔ آپ کا ووٹ انکرپٹڈ فارم میں اسٹور ہوتا ہے۔"

        if any(word in msg for word in ["election", "الیکشن", "result", "کب", "kab"]):
            return "الیکشن کی تمام تفصیلات آپ کے ڈیش بورڈ پر دستیاب ہیں۔ وہاں آپ دیکھ سکتے ہیں کہ کون سے الیکشن جاری ہیں اور نتائج کی صورتحال کیا ہے۔"

        return "معذرت، میں آپ کی بات پوری طرح نہیں سمجھ سکا۔ کیا آپ ووٹنگ، رجسٹریشن یا سیکیورٹی کے بارے میں پوچھنا چاہتے ہیں؟"

    else:
        # Conversational English Responses
        if any(word in msg for word in ["hello", "hi", "hey"]):
            return "Hello! I'm your SecureVote assistant. I can help you with voting, registration, or system security. What's on your mind?"

        if any(word in msg for word in ["vote", "cast", "how"]):
            return "To cast your vote, log in to your portal, select an active election from the dashboard, pick your candidate, and click confirm. It's fast and secure!"

        if any(word in msg for word in ["register", "signup", "account"]):
            return "You can register by providing your name, CNIC, and phone number. We sync with NADRA to ensure only eligible voters are registered."

        if any(word in msg for word in ["security", "safe", "fraud"]):
            return "Security is our top priority. We use AI-powered fraud detection and end-to-end encryption to keep every vote anonymous and tamper-proof."

        return "I'm not sure I understand. Could you please rephrase? I can assist with voting steps, registration, or technical queries."
