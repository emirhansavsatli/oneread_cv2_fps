import threading
from oneread import ONE


def main():
    cam1 = ONE("1", 2)
    cam2 = ONE("2", 3)
    cam3 = ONE("3", 30)

    thread = threading.Thread(target=cam1.CAPTURE)
    thread1 = threading.Thread(target=cam2.CAPTURE)
    thread2 = threading.Thread(target=cam3.CAPTURE)


    thread.start()
    thread1.start()
    thread2.start()

    thread.join()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()