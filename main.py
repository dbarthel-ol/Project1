# main code of application that reads sensor values and sends them over LoRaWAN
import RN2483
import sensors


if __name__ == '__main__':
    print("hello world")
    LoRa = RN2483.LoRa()
    print(LoRa.test)
    tempsensor = sensors.DS12B80()
    print(tempsensor.test2)

