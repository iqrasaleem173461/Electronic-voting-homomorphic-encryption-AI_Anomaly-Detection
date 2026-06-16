import edge_tts
import base64
import os
import asyncio

# Available Urdu Voices in Edge TTS:
# ur-PK-UzmaNeural (Female)
# ur-PK-AsadNeural (Male)

async def text_to_speech_base64(text, language='ur'):
    voice = "ur-PK-UzmaNeural" if language == 'ur' else "en-US-AvaNeural"
    
    # Create temp file
    temp_file = "temp_voice.mp3"
    
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(temp_file)
    
    # Read as base64
    with open(temp_file, "rb") as f:
        audio_data = f.read()
        base64_audio = base64.b64encode(audio_data).decode('utf-8')
        
    # Cleanup
    if os.path.exists(temp_file):
        os.remove(temp_file)
        
    return base64_audio
