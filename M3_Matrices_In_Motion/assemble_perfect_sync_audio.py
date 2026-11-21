"""
assemble_perfect_sync_audio.py — Audio Synchronizer with Thumbnail Splash Intro
Prepends thumbnail for 2.0 seconds at the beginning of the video,
and shifts audio timing by exactly +2.0s to maintain perfect visual sync.
"""

import os
import subprocess
import wave
import numpy as np

PROJECT_DIR = "/Users/deveshgupta/Desktop/MATHS_VIDEO_LINEAR_TRANSFORMATION/M3_Matrices_In_Motion"
RAW_AUDIO = os.path.join(PROJECT_DIR, "user_voiceover.mp3")
BASE_VIDEO = os.path.join(PROJECT_DIR, "media/videos/main/1080p60/MatricesInMotion.mp4")
THUMBNAIL_PNG = os.path.join(PROJECT_DIR, "thumbnail.png")
THUMBNAIL_JPG = os.path.join(PROJECT_DIR, "thumbnail.jpg")
TEMP_DIR = "/tmp/voiceover_perfect_sync"
os.makedirs(TEMP_DIR, exist_ok=True)

# Step 1: Create 2.0-second video of thumbnail
THUMB_INTRO_MP4 = os.path.join(TEMP_DIR, "thumb_intro.mp4")
subprocess.run([
    "ffmpeg", "-y", "-loop", "1", "-i", THUMBNAIL_PNG,
    "-t", "2.0", "-r", "60", "-c:v", "libx264", "-pix_fmt", "yuv420p",
    THUMB_INTRO_MP4
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Step 2: Concat thumbnail intro with master animation video
CONCAT_LIST = os.path.join(TEMP_DIR, "concat_list.txt")
with open(CONCAT_LIST, "w") as f:
    f.write(f"file '{THUMB_INTRO_MP4}'\n")
    f.write(f"file '{BASE_VIDEO}'\n")

VIDEO_WITH_THUMB = os.path.join(TEMP_DIR, "video_with_thumb.mp4")
subprocess.run([
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", CONCAT_LIST,
    "-c", "copy", VIDEO_WITH_THUMB
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Probe combined video duration
res = subprocess.run([
    "ffprobe", "-v", "error", "-show_entries", "format=duration",
    "-of", "default=noprint_wrappers=1:nokey=1", VIDEO_WITH_THUMB
], capture_output=True, text=True)
TOTAL_VIDEO_DURATION = float(res.stdout.strip())
print(f"Total Video Duration (with 2s thumbnail intro): {TOTAL_VIDEO_DURATION:.2f}s")

# Step 3: Convert raw audio to 48kHz mono 16-bit WAV
RAW_WAV = os.path.join(TEMP_DIR, "raw_48k.wav")
subprocess.run([
    "ffmpeg", "-y", "-i", RAW_AUDIO,
    "-af", "highpass=f=80,lowpass=f=12000",
    "-ar", "48000", "-ac", "1", RAW_WAV
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

with wave.open(RAW_WAV, "rb") as wf:
    sr = wf.getframerate()
    raw_data = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0

def save_wav(samples, filepath):
    scaled = np.clip(samples * 32767.0, -32768.0, 32767.0).astype(np.int16)
    with wave.open(filepath, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(scaled.tobytes())

def extract_clip(t_start, t_end, fade_sec=0.015):
    i1 = int(t_start * sr)
    i2 = int(t_end * sr)
    chunk = raw_data[i1:i2].copy()
    fade_len = int(fade_sec * sr)
    if len(chunk) > 2 * fade_len:
        fade_in = np.linspace(0.0, 1.0, fade_len)
        fade_out = np.linspace(1.0, 0.0, fade_len)
        chunk[:fade_len] *= fade_in
        chunk[-fade_len:] *= fade_out
    return chunk

def stretch_clip(chunk, target_dur_sec, out_path):
    temp_in = f"{TEMP_DIR}/temp_clip.wav"
    save_wav(chunk, temp_in)
    cur_dur = len(chunk) / sr
    tempo = cur_dur / target_dur_sec
    
    if 0.5 <= tempo <= 2.0:
        filt = f"atempo={tempo:.4f}"
    elif tempo > 2.0:
        filt = f"atempo=2.0,atempo={tempo/2.0:.4f}"
    else:
        filt = f"atempo=0.5,atempo={tempo/0.5:.4f}"
        
    subprocess.run([
        "ffmpeg", "-y", "-i", temp_in,
        "-af", filt, out_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    with wave.open(out_path, "rb") as wf:
        n = wf.getnframes()
        return np.frombuffer(wf.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0

master_samples = int(TOTAL_VIDEO_DURATION * sr)
master_audio = np.zeros(master_samples, dtype=np.float32)

OFFSET = 2.00  # Shift all audio by exactly 2.0 seconds for thumbnail intro

def place_samples(samples, start_time_sec):
    actual_start = start_time_sec + OFFSET
    start_idx = int(actual_start * sr)
    end_idx = min(start_idx + len(samples), len(master_audio))
    actual_len = end_idx - start_idx
    master_audio[start_idx:end_idx] += samples[:actual_len]
    print(f"  Placed [{actual_start:6.2f}s - {actual_start + actual_len/sr:6.2f}s] (dur: {actual_len/sr:4.2f}s)")

print("\n--- Aligning Scenes 1 to 5 (with +2.0s intro offset) ---")
# Scene 1: Hook
s1_chunk = extract_clip(2.40, 25.85)
s1_sync = stretch_clip(s1_chunk, 22.0, f"{TEMP_DIR}/s1.wav")
place_samples(s1_sync, 0.80)

# Scene 2: Basic Idea & Columns
s2_chunk = extract_clip(27.35, 63.90)
s2_sync = stretch_clip(s2_chunk, 28.5, f"{TEMP_DIR}/s2.wav")
place_samples(s2_sync, 24.50)

# Scene 3: Linear Combinations & Grid
s3_chunk = extract_clip(65.45, 115.20)
s3_sync = stretch_clip(s3_chunk, 38.5, f"{TEMP_DIR}/s3.wav")
place_samples(s3_sync, 54.50)

# Scene 4: Transformation Gallery
s4_chunk = extract_clip(116.65, 182.55)
s4_sync = stretch_clip(s4_chunk, 63.5, f"{TEMP_DIR}/s4.wav")
place_samples(s4_sync, 94.50)

# Scene 5: Unit Square & Determinant
s5_chunk = extract_clip(184.40, 218.55)
s5_sync = stretch_clip(s5_chunk, 26.5, f"{TEMP_DIR}/s5.wav")
place_samples(s5_sync, 159.50)

print("\n--- Aligning Scene 6 (Linearity) ---")
p6a = extract_clip(220.55, 229.60)
p6a_sync = stretch_clip(p6a, 6.0, f"{TEMP_DIR}/p6a.wav")
place_samples(p6a_sync, 187.50)

p6b = extract_clip(230.10, 245.05)
p6b_sync = stretch_clip(p6b, 7.5, f"{TEMP_DIR}/p6b.wav")
place_samples(p6b_sync, 194.00)

p6c = extract_clip(245.95, 255.95)
p6c_sync = stretch_clip(p6c, 6.5, f"{TEMP_DIR}/p6c.wav")
place_samples(p6c_sync, 202.50)

p6d = extract_clip(256.55, 262.45)
p6d_sync = stretch_clip(p6d, 5.5, f"{TEMP_DIR}/p6d.wav")
place_samples(p6d_sync, 209.50)

print("\n--- Aligning Scene 7 (Build Matrix) ---")
p7a = extract_clip(264.75, 271.95)
p7a_sync = stretch_clip(p7a, 6.0, f"{TEMP_DIR}/p7a.wav")
place_samples(p7a_sync, 215.20)

p7b = extract_clip(272.55, 278.85)
p7b_sync = stretch_clip(p7b, 5.5, f"{TEMP_DIR}/p7b.wav")
place_samples(p7b_sync, 221.50)

p7c = extract_clip(279.30, 286.95)
p7c_sync = stretch_clip(p7c, 6.5, f"{TEMP_DIR}/p7c.wav")
place_samples(p7c_sync, 227.50)

p7d = extract_clip(287.20, 290.95)
p7d_sync = stretch_clip(p7d, 4.0, f"{TEMP_DIR}/p7d.wav")
place_samples(p7d_sync, 234.50)

p7e = extract_clip(291.70, 299.85)
p7e_sync = stretch_clip(p7e, 7.5, f"{TEMP_DIR}/p7e.wav")
place_samples(p7e_sync, 239.00)

print("\n--- Aligning Scene 8 (Summary & Ending) ---")
p8_takeaways = extract_clip(300.80, 324.35)
p8_t_sync = stretch_clip(p8_takeaways, 19.5, f"{TEMP_DIR}/p8_t.wav")
place_samples(p8_t_sync, 248.50)

p8_quote = extract_clip(327.10, 330.00)
p8_q_sync = stretch_clip(p8_quote, 4.5, f"{TEMP_DIR}/p8_q.wav")
place_samples(p8_q_sync, 269.00)

p8_outro = extract_clip(330.20, 334.80)
p8_o_sync = stretch_clip(p8_outro, 2.2, f"{TEMP_DIR}/p8_o.wav")
place_samples(p8_o_sync, 274.00)

MASTER_WAV = f"{TEMP_DIR}/master_unnorm.wav"
save_wav(master_audio, MASTER_WAV)

print("\nMastering audio with broadcast EBU R128 loudness normalization (-16 LUFS)...")
NORMALIZED_WAV = f"{TEMP_DIR}/master_mastered.wav"
subprocess.run([
    "ffmpeg", "-y", "-i", MASTER_WAV,
    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
    "-ar", "48000", NORMALIZED_WAV
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Muxing final video with audio and embedding thumbnail cover...")
OUTPUT_VIDEO = os.path.join(PROJECT_DIR, "final_video.mp4")

subprocess.run([
    "ffmpeg", "-y",
    "-i", VIDEO_WITH_THUMB,
    "-i", NORMALIZED_WAV,
    "-i", THUMBNAIL_JPG,
    "-map", "0:v:0",
    "-map", "1:a:0",
    "-map", "2:v:0",
    "-c:v:0", "copy",
    "-c:a", "aac", "-b:a", "192k",
    "-c:v:1", "copy",
    "-disposition:v:1", "attached_pic",
    OUTPUT_VIDEO
], check=True)

# Mirror to render_output/
RENDER_OUTPUT_FINAL = os.path.join(PROJECT_DIR, "render_output", "final_video.mp4")
subprocess.run(["cp", OUTPUT_VIDEO, RENDER_OUTPUT_FINAL], check=True)

print(f"\nSUCCESS: Final video ({TOTAL_VIDEO_DURATION:.2f}s) with 2-second thumbnail intro created!")
