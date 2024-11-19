from queue import Queue

def queueWorker(q:Queue):
    while True:
        item = q.get()
        func = item['func']
        args = item.get('args', tuple())
        kwargs = item.get('kwargs', {})
        signal_done = item.get('signal_done', None)
        signal_with_result = item.get('signal_with_result', False)

        r = func(*args, **kwargs)

        # emitindo sinal, quando finalizado
        if signal_done is not None:
            signal_done.emit(r) if signal_with_result else signal_done.emit()
        q.task_done()
