# app/server.py

import asyncio
from app.config import TCP_HOST, TCP_PORT, MAX_CLIENTS, DEBUG
from app.agents.stock_agent import StockAgent

# Placeholder for StockAgent (we’ll implement next)
class StockAgent:
    async def process(self, message: str) -> str:
        # For now, just echo
        return f"Received: {message}"

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    print(f"[INFO] Client connected: {addr}")

    agent = StockAgent()
    writer.write("Welcome to MarketRadar-AI!\n".encode())
    await writer.drain()

    while True:
        try:
            data = await reader.readline()
            if not data:
                break
            message = data.decode().strip()
            if message.lower() in ["exit", "quit"]:
                writer.write("Goodbye!\n".encode())
                await writer.drain()
                break

            response = await agent.process(message)
            writer.write(f"{response}\n".encode())
            await writer.drain()
        except ConnectionResetError:
            print(f"[WARN] Client disconnected abruptly: {addr}")
            break

    writer.close()
    await writer.wait_closed()
    print(f"[INFO] Client disconnected: {addr}")

async def main():
    server = await asyncio.start_server(handle_client, TCP_HOST, TCP_PORT, limit=MAX_CLIENTS)
    addr = server.sockets[0].getsockname()
    print(f"[INFO] TCP Server running on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
