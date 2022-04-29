from kivymd.app import MDApp

class KaTrainApp(MDApp):
    def __init__(self):
        super().__init__()


def run_app():
    app = KaTrainApp()
    app.run()

if __name__ == "__main__":
    run_app()

