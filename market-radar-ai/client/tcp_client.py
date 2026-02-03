# client/tcp_client.py

import asyncio

TCP_HOST = "127.0.0.1"
TCP_PORT = 9000

async def tcp_client():
    reader, writer = await asyncio.open_connection(TCP_HOST, TCP_PORT)
    print(await reader.readline())  # Welcome message

    while True:
        message = input("> ")
        if message.lower() in ["exit", "quit"]:
            writer.write(f"{message}\n".encode())
            await writer.drain()
            break

        writer.write(f"{message}\n".encode())
        await writer.drain()
        response = await reader.readline()
        print(response.decode().strip())

    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(tcp_client())
