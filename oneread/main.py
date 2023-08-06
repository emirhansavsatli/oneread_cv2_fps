import threading
from oneread import ONE


def main():
    asd_instance = ONE("1", 2)
    asd_instance1 = ONE("2", 3)
    asd_instance2 = ONE("3", 30)

    thread = threading.Thread(target=asd_instance.CAPTURE)
    thread1 = threading.Thread(target=asd_instance1.CAPTURE)
    thread2 = threading.Thread(target=asd_instance2.CAPTURE)


    thread.start()
    thread1.start()
    thread2.start()

    thread.join()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()