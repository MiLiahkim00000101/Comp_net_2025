import os

# Another way (right way to write csv file) without any exceptions

file_out_raw = open("output/ping_log_with_empty_lines.csv", "w")

file_out_raw.write("Server_Name;Packet_loss;RTT\n")

command = r"ping -c 5 "

adresses = [r"youtube.com", r"google.com", r"universe.roboflow.com", r"github.com", r"yaandex.ru", r"www.multitran.com", r"vk.com", r"mail.google.com", r"colab.research.google.com", r"koronatech.ru"]

to_ping = list()

for adress in adresses:
    to_ping.append(command + adress)

for adress_to_ping in to_ping:
    output=os.popen(adress_to_ping)
    for line in output:
        words_of_line = line.split(" ")
        
        if (words_of_line[0] == "PING"):
            file_out_raw.write("\n")
            file_out_raw.write(words_of_line[1])
            file_out_raw.write(';')

        if (words_of_line[-1] == "loss\n"):
            file_out_raw.write(words_of_line[-3])
            file_out_raw.write(';')

        if (words_of_line[0] == "round-trip"):
            sep_using_slash = line.split("/")
            file_out_raw.write(sep_using_slash[-1])

file_out_raw.close()

file_out_raw_r = open("output/ping_log_with_empty_lines.csv", "r")
file_out_final = open("output/ping_log.csv", "w")

for line in file_out_raw_r:
    if (line.strip()):
        file_out_final.write(line)

file_out_final.close()
file_out_raw_r.close()
