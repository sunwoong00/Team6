import pyaudio
import wave
import whisper

def record_audio(output_file: str, record_seconds: int = 5):
    format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024
    audio = pyaudio.PyAudio()

    # print(f"{record_seconds}초 동안 녹음이 시작됩니다. 말해주세요...")

    # 입력 장치 명시
    stream = audio.open(
        format=format,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=chunk,
        input_device_index=1  # 사용 가능한 입력 장치 ID로 수정
    )
    frames = []

    for _ in range(0, int(rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # print("녹음이 완료되었습니다.")
    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    # print(f"녹음된 파일이 '{output_file}'에 저장되었습니다.")


def speech_to_text(file_path: str) -> str:
    """
    주어진 음성 파일을 Whisper 모델로 텍스트로 변환합니다.
    
    :param file_path: 음성 파일 경로
    :return: 변환된 텍스트
    """
    model = whisper.load_model("tiny")
    # print("음성 파일을 텍스트로 변환 중입니다...")
    result = model.transcribe(file_path, language="ko")
    text = result["text"]
    # print("변환된 텍스트:", text)
    return text


def stt(file_path, output_file, record_seconds = 10):
    record_audio(output_file, record_seconds)
    text = speech_to_text(file_path)
    return text


# if __name__ == "__main__":
#     audio_file = "recorded_audio.wav"  # 저장할 오디오 파일 이름
#     record_audio(output_file=audio_file, record_seconds=5)  # 5초 녹음
#     text = speech_to_text(file_path=audio_file)  # 녹음된 파일을 텍스트로 변환
#     print(f"최종 변환 텍스트: {text}")
