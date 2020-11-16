from asyncmcrcon import MinecraftClient


class mcutil:
    ip: str
    port: int
    password: str

    def __init__(self, ip, port, password):
        self.ip = ip
        self.port = port
        self.password = password

    async def get_online_players(self):
        async with MinecraftClient(self.ip, self.port, self.password) as mc:
            output = await mc.send("list")
        output = output.split(" ")
        remove = []
        for item in output:
            try:
                item = int(item)
            except:
                remove.append(item)
        for item in remove:
            output.remove(item)
        return tuple(output)
