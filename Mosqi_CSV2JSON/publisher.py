import paho.mqtt.client as mqtt
import csv
import codecs
import json

_g_cst_ToMQTTTopicServerIP = "localhost"
_g_cst_ToMQTTTopicServerPort = 1883    ###port
_g_cst_MQTTTopicName = "test1"    ###TOPIC name

mqttc = mqtt.Client("python_pub")
mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)

fname = 'TEST.csv'     ###filename

###convert to json
with codecs.open(fname, "r", encoding='utf-8', errors='ignore') as csvf:
    for line in csv.DictReader(csvf):
        #print(json.dumps(line))
        mqttc.publish(_g_cst_MQTTTopicName, json.dumps(line))

#mqttc.publish(_g_cst_MQTTTopicName, ass)
