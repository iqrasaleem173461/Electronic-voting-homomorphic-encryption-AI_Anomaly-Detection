import asyncio
import edge_tts
import base64

async def test():
    try:
        text = "اسلام علیکم"
        voice = "ur-PK-UzmaNeural"
        print(f"Testing with voice {voice} and text: {text}")
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save("test_ur.mp3")
        print("Success: Urdu file saved")
        
        text_en = "Hello this is a test"
        voice_en = "en-US-AvaNeural"
        print(f"Testing with voice {voice_en} and text: {text_en}")
        communicate_en = edge_tts.Communicate(text_en, voice_en)
        await communicate_en.save("test_en.mp3")
        print("Success: English file saved")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test())
