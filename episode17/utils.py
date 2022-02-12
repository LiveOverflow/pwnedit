from filelock import Timeout, FileLock

lock = FileLock("state.lock")

def get_state():
    with lock:
        with open('state', 'r') as f:
            state = f.read()
        return state

def set_state(state):
    with lock:
        with open('state', 'w') as f:
            state = f.write(state)


    
