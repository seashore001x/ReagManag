print("Reagent Management System for Institute of Diary Science\tALPHA v0.1\n")
import Delete
import Query
import Upgrade
while True:
    quest = input("Query, upgrade or delete a reagent?\n\t1. Query\t2.Upgrade\t3.Delete\n")
    if not quest: break
    if quest == '1':
        Query.query()
    if quest == '2':
        Upgrade.upgrade()
    if quest == '3':
        Delete.delete()

