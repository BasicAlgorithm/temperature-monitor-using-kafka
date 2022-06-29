import json 
from kafka import KafkaConsumer
from os import system, name
from datetime import datetime

def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def symbol(current, previous):
    if (current >= previous):
        return "+++"
    else:
        return "---"

previous_t = 0

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest'
    )

    # infinite loop waiting for producer temperatures
    for message in consumer:
        data_rec = json.loads(message.value)
        current_t = data_rec["temperature"]
        dif = get_change(float(current_t), float(previous_t))
        up_down = symbol(float(current_t), float(previous_t))
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        clear()
        print("+------------------------------------+")
        print("|         Station Temperature        |")
        print("+-----------------------+------------+")
        print("| Actual temperature    |",current_t)
        print("+-----------------------+------------+")
        print("| Change of temperature |",round(dif,2),"% ",up_down)
        print("+-----------------------+------------+")
        print("|                 Time  |",current_time)
        print("+-----------------------+------------+")
        previous_t = current_t