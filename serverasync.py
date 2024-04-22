import asyncio

async def handle_echo(reader, writer):
    """
    Эта асинхронная функция обрабатывает входящие соединения.
    Она читает данные, полученные от клиента, и отправляет их обратно.
    """
    data = await reader.read(1000)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received {message!r} from {addr!r}")

    writer.write(data)
    await writer.drain()
    print(f"Sent {message!r} to {addr!r}")

    writer.close()


async def main():
    """
    Главная функция, создающая и запускающая сервер.
    """
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 9090)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
        
asyncio.run(main())
