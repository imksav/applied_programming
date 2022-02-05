class temperature_stat:
    def __init__(self, date, temperature_data):

        self.date = date

        self.temperature_data = temperature_data

    def check_status(self, temperature_data):

        if temperature_data > 85:

            return "Celcius very hot."

        elif temperature_data > 65:

            return "Celcius pleasant day."

        else:

            return "Celcius very cold."

    def display(self, day_status):

        print(f"--------Daily Temperature----------------")

        print(f"Temperature Day [{self.date}] = {self.temperature_data} {day_status} ")
        
if __name__ == "__main__":
     
    number_of_record = int(input("How many days to record ? "))

    record_list = []



    for i in range(1, number_of_record+1):

        temperature_data = input(f'Temperature Day{i}: ')

        record_list.append(temperature_stat(i, temperature_data))



    for obj in record_list:

        temperature_status = obj.temperature_data

        day_status = (obj.check_status(int(temperature_status)))

        day_number = obj.date

        obj.display(day_status)
