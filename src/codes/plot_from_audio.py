from codes.audio_visualization import (
    load_sound_files,
    plot_waves,
    plot_specgram,
    plot_log_power_specgram
)
sound_file_paths = ["./data/drums.wav","./data/kp-intro.wav"]
sound_file_names = ["drums", "intro"]

print("raw-sound")
raw_sounds = load_sound_files(sound_file_paths)

print("specgram")
plot_specgram(sound_file_names,raw_sounds)
print("waves")
plot_waves(sound_file_names,raw_sounds)
print("log-power-spectrum")
plot_log_power_specgram(sound_file_names,raw_sounds)
