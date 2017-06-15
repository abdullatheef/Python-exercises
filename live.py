def log_streamer(from_=0):
    mtime = os.path.getmtime(settings.LOG_FILE)
    with open('/var/log/stk.log') as f:
        start = -int(from_) or -1000
        filestart = True
        while filestart:
            try:
                f.seek(start, 2)
                filestart = False
                to_send = f.readlines()
                last = f.tell()
                yield "".join(["<p>%s</p>" %i.strip() for i in to_send])
            except IOError:
                start += 50
    while True:
        newmtime = os.path.getmtime('/var/log/stk.log')
        if newmtime == mtime:
            time.sleep(3)
        mtime = newmtime
        with open(settings.LOG_FILE) as f:
            f.seek(last)
            next_line = f.readlines()
            if next_line:
                yield "<p>#######################%s########################</p><p>%s</p>" %(
                    datetime.now().strftime('%Y-%m-%d %H:%M'),
                    "".join(["<p><pre>%s</pre></p>" %i.strip() for i in next_line]))
            last = f.tell()
@login_required
def live_debug_log(request):
    return StreamingHttpResponse(log_streamer(request.GET.get('from', 0)))

