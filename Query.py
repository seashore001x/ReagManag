def query():
    # interactive queries
    import shelve
    fieldnames = ('name', 'brand', 'quantity', 'location', 'owner')
    maxfield = max(len(f) for f in fieldnames)
    db = shelve.open('ReagentManagement-shelve')

    while True:
        key = input('\nReagent query? Type all for query all reagent=> ')  # key or empty line, exc at eof
        if not key: break
        if key == 'all':
            for i in db:
                print (db[i])
            continue
        try:
            record = db[key]  # fetch by key, show in console
        except:
            print('No such reagent "%s"!' % key)
        else:
            for field in fieldnames:
                print(field.ljust(maxfield), '=>', getattr(record, field))