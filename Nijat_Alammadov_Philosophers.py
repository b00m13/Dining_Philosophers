import threading
import random
import time


# -----------------------------------------------------------------------------
class Philosopher(threading.Thread):
    running = True

    # ---------------------------------------------------------------------------
    def __init__(self, xname, chopStickLeft, chopStickRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.chopStickLeft = chopStickLeft
        self.chopStickRight = chopStickRight

    # ------------------------------------------------------------------------------
    def run(self):
        while self.running:
            time.sleep(random.uniform(3, 15))
            print('%s want to eat a meal.' % self.name)
            self.dine()

    # -----------------------------------------------------------------------------------
    def dine(self):
        chopStick1, chopStick2 = self.chopStickLeft, self.chopStickRight

        while self.running:
            chopStick1.acquire(True)
            locked = chopStick2.acquire(False)
            if locked: break
            chopStick1.release()
            print('%s exchange chopsticks' % self.name)
            chopStick1, chopStick2 = chopStick2, chopStick1
        else:
            return

        self.dining()
        chopStick2.release()
        chopStick1.release()

    # -------------------------------------------------------------------------------
    def dining(self):
        print('%s start to eat meal ' % self.name)
        time.sleep(random.uniform(1, 10))
        print('%s finishes eat meal && thinking.' % self.name)
    # ---------------------------------------------------------------------------------


def PhilosophersDiningTime():
    chopSticks = [threading.Lock() for n in range(7)]
    philosopherNames = ('Nietzsche', 'Averroes', 'Ambrose', 'Damascius', 'Galilei', 'Gorgias', 'Iamblichus')

    philosophers = [Philosopher(philosopherNames[i], chopSticks[i % 7], chopSticks[(i + 1) % 7]) \
                    for i in range(7)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False
    print("One round going to finish")


# ----------------------------------------------------------------------------------------------------------------------
PhilosophersDiningTime()
