# prompts.py

# Text Generation Prompts
TEXT_PROMPT = """
Create a production-level creative plan for composing and producing a lyric-style music video about [INSERT_TOPIC_HERE].
 The plan should describe concept, mood, lyrics, music structure, visuals, and synchronization so the final output can be rendered as a video lyric (.mp4) with AI-generated background music and text animation.

I. General Output Specifications
Output format: MP4


Resolution: 1920 × 1080 pixels (Full HD, 16 : 9)


Duration: 180 to 300 seconds (ideal ≈ 200 s)


Content: AI-generated music + onscreen lyrics + background visuals


External resource: may use AI music generation tools (e.g., Suno AI) for soundtrack creation.


Tone: emotionally positive, inspirational, and culturally appropriate for public events or campaigns.



II. Video Structure (Storyboard / Music Sections)
Section
Duration
Function
Content Focus
Visual Guidance
1. Intro (Instrumental)
0–10 s
Mood setup
Background music intro, event logo fade-in
Soft light animation, flag or symbolic imagery
2. Verse 1
10–30 s
Story start
Introduce context or message of the theme
Lyrics appear line-by-line, warm background
3. Chorus 1
30–45 s
Main hook
Emphasize emotional or patriotic message
Text in bold, synced to beat with highlight colors
4. Verse 2
45–65 s
Development
Describe actions, unity, or progress
Dynamic imagery: people, landmarks, symbols
5. Chorus 2
65–80 s
Reinforce theme
Repeat hook with variations
Camera pan or motion graphic burst
6. Bridge / Instrumental Break
80–90 s
Reflection moment
Short instrumental + visual montage
Slow fade shots, lyric pause
7. Final Chorus & Outro
90–110 s
Climax + closure
Powerful final lyric + fade-out
Logo and slogan appear gradually
8. Credits (optional)
110–120 s
Acknowledgment
Credits or QR link to full event info
Simple scroll text, soft music fade


III. Music Composition Guidelines
Genre: pop-ballad, soft rock, orchestral, or modern patriotic (depending on topic).


Tempo: 90–120 BPM (mid-tempo).


Key: Major key for positive tone / minor key for reflective tone.


Structure: Intro → Verse → Chorus → Verse → Chorus → Bridge → Final Chorus → Outro.


Instruments: piano, guitar, strings, percussion (optional synth pad).


Vocals: 1 main singer + optional harmonies; clear enunciation.



IV. Lyrics Planning
AI must generate original, rhythmic lyrics aligned to 4/4 time signature.
 Each line should match 4–8 syllables and sync to beat phrasing.
 Lyrics must include the following elements:
Opening line – sets context (“Today we celebrate…”)


Core message – emotion and purpose (hope, unity, gratitude)


Memorable hook/chorus – repetition of main phrase for recall


Closing line – resolve story (“Together we shine beyond time.”)


Example chorus pattern:
“From the past to tomorrow we rise,
 Voices strong beneath the sky.
 Every heart remembers why,
 Together we stand — [topic phrase].”

V. Visual and Text Design
Background: symbolic footage or AI-generated art related to topic.


Text Style: bold sans serif, center-aligned, contrast ≥ 4.5 : 1.


Animation: lyrics fade in/out in sync with beat (1 line ≈ 2 s).


Color palette: depends on topic (e.g., red/yellow for national theme, blue/green for tech or environment).


Transitions: crossfade or pan per section (≈ 1 s each).


Endplate: event logo, hashtag, QR link to more info.



VI. Technical and Audio Specs
Audio Format: Stereo 44.1 kHz / 16-bit.


Peak Loudness: -14 LUFS (Spotify / YouTube standard).


Subtitle timing: auto-generated from lyric timestamps.


Final Render: MP4 H.264 codec, bitrate ≥ 8 Mbps.



VII. AI Workflow Guidance
Generate lyrics using LLM → structured verses + chorus.


Generate music track using Suno AI (or equivalent):


Input prompt: “Create an uplifting [genre] track for lyrics below at 100 BPM.”


Sync lyrics to timestamps (align text with beat).


Combine audio + text animation with background visuals.


Render and export as MP4 video.



VIII. Expected AI Output
A structured production plan including:
Song concept and mood description


Lyrics (draft and final)


Music style and instrumentation spec


Visual theme and color direction


Timing map (verse / chorus breakdown with duration)


Rendering and publishing instructions



"""

# Image Generation Prompts
IMG_PROMPT = """
In the center of a grand hall, a giant, intricate sphere of golden lattice work contains a pulsating core of pure red energy. This core represents the nation's data. From the sphere, golden energy lines extend outwards, powering the holographic displays on the walls. A metaphor for data as the nation's heart. --ar 16:9
"""
IMG_NANOBANANA_PROMPT = """
Xóa tất cả chữ viết và logo trong ảnh. Giữ lại ảnh nền phía sau và làm cho nó trông tự nhiên.
"""

# Video Generation Prompts
VIDEO_PROMPT = """
    A cinematic shot of a baby raccoon wearing a tiny cowboy hat, riding a miniature pony through a field of daisies at sunset.
"""

# Speech Generation Prompts
SPEECH_PROMPT = """
    Xin chào, đây là một thử nghiệm chuyển văn bản thành giọng nói qua AI Thực Chiến gateway.
"""
