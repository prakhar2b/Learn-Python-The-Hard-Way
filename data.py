#!/usr/bin/python

import csv
b = open('data.csv', 'w')
a = csv.writer(b)
data = [['Device_ID', 'Eth_MAC_ID', 'WiFi_MAC_ID'],\
        ['293', '219', ''],\
        ['54', '13', ''],\
        ['76', '','54'],\
        ['765', '','14'],\
        ['734', '667',''],\
        ['836', '','554'],\
        ['3', '','464'],\
        ['986', '565',''],\
        ['45', '328',''],\
        ['433', '','94']]
a.writerows(data)
b.close()
