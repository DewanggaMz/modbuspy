import asyncio
from pymodbus.client import AsyncModbusSerialClient

slaves = [0, 1]


def read_slaves(client):
    pass


async def run():
    try:
        client = AsyncModbusSerialClient(
            method="rtu",
            port="/dev/ttyS0",
            stopbits=1,
            bytesize=8,
            parity="N",
            baudrate=9600,
            timeout=1
        )

        isConnected = await client.connect()
        print(f"status connection : {isConnected}")

        while isConnected:
            await asyncio.sleep(1)
            result = await client.read_holding_registers(slave=1, address=1)
            print(f"hasil register slave 1: {result}")

        client.close()
    except(Exception):
        print(F"Error connecting {Exception}")


if __name__ == "__main__":

    asyncio.run(run())

