from PySock import client

name = input('Choose your nickname: ')


def abc(data, con):
    print(f"Message from {data['sender_name']} : {data['data']}")
    con.SEND("test", input(' '))


c = client(client_name=name, debug=True)
c.CLIENT("192.168.100.23", 9669)
c.CREATE_CHANNEL("test")

count = 0
while True:
    c.LISTEN(channel="test", function=abc, args=(c,))

    if count == 0:
        c.SEND_TO_CLIENT(target_name="swat", data="Hello, what are you doing.")
        count += 1
