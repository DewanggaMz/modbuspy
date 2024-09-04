import asyncio
from pymodbus.client import AsyncModbusSerialClient
from pymodbus.exceptions import ModbusException

slaves = [0, 1]


async def connection():
    client = AsyncModbusSerialClient(
        port="/dev/ttyS0",
        stopbits=1,
        bytesize=8,
        parity="N",
        baudrate=9600,
        timeout=1,
        reconnect_delay=2000,
        reconnect_delay_max=5000
    )
    while not await client.connect():
        print("Connection failed, retrying...")
        await asyncio.sleep(5)
        
    return client

async def read_holding_register(client, slave, address):
    try:
        result = await client.read_holding_registers(slave=slave, address=address)
        return result.registers
    except ModbusException as e:
        print(f"Modbus exception occurred: {e}")
    except Exception as e:
        print(f"Error reading from slave {slave}: {e}")
        return None

async def run():
        client = await connection()
        isConnected = client is not None
        
        print(f"status connection : {isConnected}")
        
        try:
            while isConnected:
                await asyncio.sleep(1)

                result1, result2 = await asyncio.gather(
                    read_holding_register(client, slave=1, address=1),
                    read_holding_register(client, slave=2, address=1)
                )

                print(f"hasil register slave 1: {result1}")
                print(f"hasil register slave 2: {result2}")
                
        except Exception as e:
            print(f"Error reading Modbus registers: {e}")


if __name__ == "__main__":
    print("Starting")
    asyncio.run(run())
