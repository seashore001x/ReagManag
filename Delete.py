def delete():
    import shelve
    db = shelve.open('ReagentManagement-shelve')
    while True:
        key = input('\n Reagent delete? =>')
        if not key: break
        try:
            record = db[key]
            judgment = input('Delete %s? yes or no\n' % key)
            if judgment == 'yes':
                db.pop(key)
                print('%s has been successfully deleted' % key)
            elif judgment == 'no':
                print('Database remain unchanged!')
            else:
                break
        except:
            print('No such reagent "%s"!' % key)

