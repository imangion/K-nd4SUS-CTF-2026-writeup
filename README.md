# Signal Audit — Writeup

**Category:** rev  
**Challenge:** Signal Audit  
**Final flag:** `KSUS{s4n1ty_ch3ck_QSL_7373}`

> Note: the decoded bottom text is slightly distorted, so the `h` in `ch3ck` can look like `n` in some crops.

---

## Challenge description

We were given an audio file named `audit.wav` and the following prompt:

> Our monitoring station has been picking up a rhythmic transmission on the HF bands. The signal is old, but the signature is unmistakable to those who know how to listen. Be prepared to QSL, and 73 to the first to answer!

The important clues here were:

- **HF bands**
- **QSL**
- **73**

Those are all radio-related hints, so the first guess was that the file was not just ordinary audio, but some kind of **ham radio image transmission**.

---

## Step 1 — Inspect the audio

The first thing to do was generate a spectrogram from the WAV file.

```bash
python3 scripts/make_spectrogram.py assets/audit.wav assets/spectrogram_generated.png
```

That makes it easier to see whether the signal looks structured. The waveform clearly was not random noise or speech only; it had the repeating tone structure you would expect from an encoded transmission.

### Challenge screenshot

![challenge](https://github.com/imangion/K-nd4SUS-CTF-2026-writeup/blob/main/challenge.png)

### Spectrogram

![spectrogram](https://github.com/imangion/K-nd4SUS-CTF-2026-writeup/blob/main/spectrogram.png)

### Zoomed spectrogram

![spectrogram zoom](https://github.com/imangion/K-nd4SUS-CTF-2026-writeup/blob/main/spec_zoom.png)

At this point the radio clues strongly suggested **SSTV**.

---

## Step 2 — Identify SSTV / Robot mode

Once treated as SSTV, the signal decodes into an image. The recovered image contains visible radio-themed text, including:

- `CQ SSTV`
- `K!nd4SUS CTF 2026`

That confirms the intended path immediately.

The recovered frame looked like this:

![decoded image 1](https://github.com/imangion/K-nd4SUS-CTF-2026-writeup/blob/main/decoded_robot_guess1.png)

A second decode variant gave a very similar result:

![decoded image 2](https://github.com/imangion/K-nd4SUS-CTF-2026-writeup/blob/main/decoded_robot_guess2.png)

---

## Step 3 — Extract the flag from the bottom line

The flag is printed along the bottom of the decoded SSTV image. Because the line is small and noisy, it helps to crop and enhance it.

```bash
python3 scripts/crop_flag.py assets/decoded_robot_guess2.png assets/flag_crop_generated.png
python3 scripts/enhance_flag_text.py assets/flag_crop_generated.png assets/flag_text_zoom_generated.png
```

### Bottom crop

![flag crop](https://github.com/imangion/K-nd4SUS-CTF-2026-writeup/blob/main/flag_crop.png)

### Enhanced text zoom

![flag zoom](https://github.com/imangion/K-nd4SUS-CTF-2026-writeup/blob/main/flag_text_zoom.png)

The reconstructed text is:

```text
KSUS{s4n1ty_ch3ck_QSL_7373}
```

---

## Why this was the correct approach

This challenge was mainly about recognizing the clues rather than brute force.

- `HF bands` pointed to radio transmission.
- `QSL` and `73` are standard ham radio terms.
- The structured audio strongly suggested an image-bearing analog mode.
- Decoding as SSTV revealed the actual image and the flag.

---

## Files in this repo

- audit.wav — original challenge audio
- challenge.png — challenge screenshot
- spectrogram.png — spectrogram view of the WAV
- spec_zoom.png — zoomed spectrogram
- decoded_robot_guess1.png — decoded SSTV image
- decoded_robot_guess2.png — alternate decoded SSTV image
- flag_crop.png — bottom crop containing the flag
- flag_text_zoom.png — enhanced crop for easier reading
- make_spectrogram.py — builds a spectrogram from WAV input
- crop_flag.py — crops the bottom text from the decoded image
- enhance_flag_text.py — sharpens and enlarges the crop

---

## Reproduction notes

The actual SSTV decode step was done externally, and the repo keeps the resulting evidence images so the full solve path is documented. The included scripts cover the reproducible parts used in the writeup:

1. Analyze the audio with a spectrogram.
2. Decode the SSTV signal.
3. Crop and enhance the bottom text line.
4. Read the flag.

If you want a cleaner version later, this can be rewritten into a shorter CTF-style format or into a more formal GitHub writeup.
