import subprocess as sp, argparse
import asyncio

async def handle(reader, writer):
    while True:
        data = await reader.read(1024)
        process = sp.Popen([data], stdout=sp.PIPE, stderr=sp.PIPE, shell=True, universal_newlines=True)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            ans = "OK \n"+ stdout
        else:
            ans = "ERROR \n"+ stderr 
        print(ans)
        writer.write(ans.encode())
        await writer.drain()

async def main():
    parser = argparse.ArgumentParser(description="Servidor asincrónico")
    parser.add_argument('-ht', type=str, help="Ingresar host")
    parser.add_argument('-p', type=int, help="Ingresar puerto")
    args = parser.parse_args()
    server = await asyncio.start_server(handle, args.ht, args.p)
    print("Starting server...")
    await server.serve_forever()

asyncio.run(main())