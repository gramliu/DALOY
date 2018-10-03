import serial
import time
from threading import Thread

class Reader:
    def __init__(self, debug=False):
        self.reader = serial.Serial("/dev/ttyUSB0", baudrate=9600)
        print("Initialized XBee Reader")
        self.debug = debug

    def run(self):
        while True:
            data = self.reader.readline().decode()
            try:
                val = [float(i) for i in data.split(",")]
            except ValueError:
                print("Non-numeric text detected! Text: ", data)
            if self.debug:
                print(val)
            else:
                import DaloyGround
                DaloyGround.instance.registerEntry(tuple(val))
            time.sleep(0.3)

    def start(self):
        thread = Thread(target=self.run)
        thread.start()

if __name__ == "__main__":
    reader = Reader(debug=True)
    reader.start()