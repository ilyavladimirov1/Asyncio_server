import asyncio

async def tcp_echo_client():
    """
    Асинхронная функция, которая подключается к TCP-серверу,
    отправляет сообщение и печатает ответ сервера.
    """
    reader, writer = await asyncio.open_connection('127.0.0.1', 9090)
    message = input("Введите сообщение: ")
    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(1000)
    print(f'Received: {data.decode()!r}')

    writer.close()

asyncio.run(tcp_echo_client())
