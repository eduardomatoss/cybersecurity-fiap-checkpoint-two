import sounddevice as sound
from wavio import write


def record_audio(duration: int = 3, sample_rate: int = 44100) -> any:
    recording = sound.rec(
        int(duration * sample_rate), samplerate=sample_rate, channels=1
    )
    sound.wait()
    return recording


def save_record(file_path: str, record, sample_rate: int = 44100):
    write(file_path, record, sample_rate, sampwidth=4)
