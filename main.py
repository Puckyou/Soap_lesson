import osa

#Task 1
import re
URL = "http://www.webservicex.net/ConvertTemperature.asmx?WSDL"

client = osa.client.Client(URL)

temp_list = []
with open("temps.txt", "r") as f:
    data = f.readlines()
    for line in data:
        num = re.sub("\D","", line)
        response = client.service.ConvertTemp(Temperature=int(num),
                                                  FromUnit="degreeFahrenheit",
                                                  ToUnit="degreeCelsius")
        temp_list.append(response)
        a = sum(temp_list)/len(temp_list)
print(round(a, 1))


#Task 2

URL1 = "http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL"

client1 = osa.client.Client(URL1)

with open("currencies.txt", "r") as f1:
    data1 = f1.readlines()
    for line in data1:
        split_data = line.split(" ")
        response1 = client1.service.ConvertToNum(fromCurrency=split_data[2].strip(),
                                                 toCurrency="RUB",
                                                amount=int(split_data[1]),
                                                 rounding=True)
        print("{0} {1} RUR\n".format(split_data[0], round(response1)))

#Task 3

URL2 = "http://www.webservicex.net/length.asmx?WSDL"

client2 = osa.client.Client(URL2)

distance = 0
with open("travel.txt", "r") as f2:
    data2 = f2.readlines()
    for line in data2:
        num = re.sub("\D", "", line)
        response2 = client2.service.ChangeLengthUnit(LengthValue=num,
                                                 fromLengthUnit="Miles",
                                                 toLengthUnit="Kilometers")
        distance += response2
print(round(distance, 2))