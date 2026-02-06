import argparse
import uvicorn

if __name__=='__main__':
    try:
        parser = argparse.ArgumentParser(description="web app")

        valid_true_args = ["T", 't', 'True', 'true']
        valid_false_args = ['F', 'f', 'False', 'false']

        parser.add_argument(
            '--host',
            type=str,
            help="Chose a valid host",
            default='localhost'
        )

        parser.add_argument(
            '--port',
            help="chose an available port",
            type=int,
            default=8000
        )

        parser.add_argument(
            "--reload",
            type=str,
            default="f"
        )

        parser.add_argument(
            "--workers",
            type=int,
            help="number of threads uvicorn can use"
        )


        args = parser.parse_args()

        host = args.host
        port = args.port
        reload = args.reload

        if reload in valid_true_args:
            reload = True

        elif reload in valid_false_args:
            reload = False

        else:
            reload = False



        """
            If you want to connect multiple devices
            Set host to 0.0.0.0
            set port to 8080
            Make sure you have port forwarding for 8080
            Have someone type your ip shown in network settings + : + port
            ie.: http://10.0.0.1:8080
            both devices must be on the same wifi
        """

        uvicorn.run(
            "App.Api.WebApp:app",
            host=host,
            port=port,
            reload=reload,
            workers=4,
            limit_concurrency=100,
            timeout_keep_alive=5
        )

    except Exception as e:
        print(e)
