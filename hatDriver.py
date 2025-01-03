import tensorflow as tf

try:
    # 사용 가능한 물리적 장치 확인
    physical_devices = tf.config.experimental.list_physical_devices()
    print("TensorFlow에서 사용 가능한 물리적 장치:")
    for device in physical_devices:
        print(f"장치 이름: {device.name}, 장치 유형: {device.device_type}")

    # NPU 확인
    npu_devices = [device for device in physical_devices if "NPU" in device.device_type.upper() or "HAILO" in device.name.upper()]
    if npu_devices:
        print(f"NPU 또는 Hailo 장치가 감지되었습니다: {npu_devices}")
    else:
        print("NPU 또는 Hailo 장치가 감지되지 않았습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
