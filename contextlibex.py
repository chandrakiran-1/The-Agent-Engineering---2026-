from contextlib import contextmanager
@contextmanager
def db():
    print("connected:")
    yield
    print("closed")
with db():
    print("working")