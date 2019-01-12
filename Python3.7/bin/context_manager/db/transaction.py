import contextlib
from connection import Connection


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield tx
    except:
        tx.rollback()
        raise

    tx.commit()


if __name__ == "__main__":
    conn = Connection()
    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            raise ValueError()  # trigger error
            y = x + 2
            print('transaction 0 =', x, y)
    except ValueError:
        print('Oops! Transaction 0 failed.')

    print('\n')

    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            y = x + 2
            print('transaction 1=', x, y)
    except ValueError:
        assert False


