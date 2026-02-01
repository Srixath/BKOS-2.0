# firmware/imu/test_imu.py
import time
import board
import busio
from adafruit_bno08x import BNO08X

# -----------------------------
# I2C setup
# -----------------------------
i2c = busio.I2C(board.SCL, board.SDA)

# TCA9548A multiplexer address
TCA_ADDR = 0x70

def select_channel(channel):
    """
    Enable only one channel on the TCA9548A at a time.
    channel: 0-7
    """
    i2c.writeto(TCA_ADDR, bytes([1 << channel]))

# -----------------------------
# IMU channel assignments
# -----------------------------
# 0 = thigh, 1 = knee frame, 2 = shin
imu_channels = [0, 1, 2]

# Keep track of BNO objects so we don't reinitialize every loop
imus = [None, None, None]

# -----------------------------
# Main loop
# -----------------------------
try:
    while True:
        for ch in imu_channels:
            select_channel(ch)

            # Initialize IMU if not already
            if imus[ch] is None:
                imus[ch] = BNO08X(i2c)

            imu = imus[ch]

            # Read quaternion
            quat = imu.quaternion  # tuple: (w, x, y, z)
            print(f"IMU channel {ch}: quaternion = {quat}")

        print("-" * 40)
        time.sleep(0.2)  # 5 readings per second

except KeyboardInterrupt:
    print("Exiting IMU test.")
