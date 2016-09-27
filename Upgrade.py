def upgrade():
    import shelve
    from Reagent import Reagent
    fieldnames = ('name', 'brand', 'quantity', 'location', 'owner')
    db = shelve.open('ReagentManagement-shelve')

    while True:
        key = input('\nReagent upgrade? =>')
        if not key: break
        if key in db:
            record = db[key]
        else:
            record = Reagent(name='?', brand='?', quantity='?', location='?')
        for field in fieldnames:
            currval = getattr(record, field)
            newtext = input('\t[%s] = %s\n\t\tnew?=>' % (field, currval))
            if newtext:
                setattr(record, field, newtext)
        db[key] = record
    db.close()
