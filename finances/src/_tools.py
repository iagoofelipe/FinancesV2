from queue import Queue

def queueWorker(q:Queue):
    while True:
        func, args, kwargs = q.get()
        signal_done = kwargs.pop('signal_done', None)
        signal_with_result = kwargs.pop('signal_with_result', False)
        r = func(*args, **kwargs)

        # emitindo sinal, quando finalizado
        if signal_done is not None:
            signal_done.emit(r) if signal_with_result else signal_done.emit()
        q.task_done()
