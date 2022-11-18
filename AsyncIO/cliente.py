import asyncio, argparse, subprocess

parser = argparse.ArgumentParser(description="Servidor asincrónico")
parser.add_argument('-ht', type=str, help="Ingresar host")
parser.add_argument('-p', type=int, help="Ingresar puerto")
args = parser.parse_args()

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(args.ht, args.p)
    while True:
        command = input("> ")
        salida = command
        command = command.encode()
        if salida[:4] == "exit" or len(salida) == 0:
            print("Saliendo...")
            writer.close()
            await writer.wait_closed()
            return
        writer.write(command)
        await writer.drain()
        recv = await reader.read(1024)
        print(recv.decode())
try:
    asyncio.run(tcp_echo_client())
except ConnectionResetError as e:
    print(e)
