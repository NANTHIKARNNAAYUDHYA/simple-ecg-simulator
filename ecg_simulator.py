import math
import time
import os

def simulate_ecg():
    print("กำลังเริ่มจำลองสัญญาณคลื่นไฟฟ้าหัวใจ (ECG Simulation)... กด Ctrl+C เพื่อหยุดนะคะ")
    time.sleep(1)
    
    # พารามิเตอร์จำลองคลื่น P-Q-R-S-T
    cycle_length = 40
    
    try:
        while True:
            for i in range(cycle_length):
                # ใช้ฟังก์ชันคณิตศาสตร์สร้างรูปร่างคลื่น ECG คร่าวๆ
                val = 0
                if 5 <= i <= 8:
                    val = math.sin((i - 5) / 3 * math.pi) * 2  # P wave
                elif 12 <= i <= 14:
                    val = -3 * (14 - i) / 2  # Q wave
                elif i == 15:
                    val = 15  # R peak (ยอดสูงสุด)
                elif i == 16:
                    val = -6  # S wave
                elif 20 <= i <= 26:
                    val = math.sin((i - 20) / 6 * math.pi) * 4  # T wave
                
                # แสดงผลเป็นกราฟเส้นตรงใน Terminal
                spaces = " " * int(max(0, val + 5))
                if val == 15:
                    print(spaces + "* R-Peak (Heartbeat!)")
                else:
                    print(spaces + "-")
                    
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nหยุดการทำงานเรียบร้อยค่ะ ขอให้สนุกกับการเขียนโค้ดนะคะ!")

if __name__ == "__main__":
    simulate_ecg()
