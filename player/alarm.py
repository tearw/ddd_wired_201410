import re

def alarm_adjust(alarms):
    relations = []
    f = open('alarm.txt')
    line = f.readline().strip('\n')
    while line:
        conditions,relation = line.split(':')
        if alarm_match(conditions, alarms):
            relations.append(relation)
            #alarms = replace_alarms(relation, alarms)
        line = f.readline().strip('\n')
    f.close()
    
    for relation in relations:
        alarms = replace_alarms(relation, alarms)
    
    return alarms
    
def replace_alarms(relation, alarms):
    alarms = ',' + alarms + ','
    name = relation.split('=')[0]
    relation_with_comma = ',' + relation + ','
    if re.search(',%s=\d,'%name, alarms):
        return re.sub(',%s=\d,'%name, relation_with_comma, alarms)[1:-1]
    else: return alarms[1:len(alarms)] + relation
    
def alarm_match(conditions, alarms):
    alarms = ',' + alarms + ','
    cons = conditions.split(',')
    for condition in cons:
        condition = ',' + condition + ','
        if -1 == alarms.find(condition):return False
    return True
    
if __name__ == '__main__':
    assert('loflom=0,ais=1,lck=0,tim=0,bbe=0,bdi=0,aais=1,abdi=1,arei=1' == alarm_adjust('loflom=0,ais=1,lck=0,tim=1,bbe=1,bdi=0'))
    assert('loflom=0,ais=1,lck=0,tim=0,bbe=0,bdi=0,aais=1,abdi=1' == alarm_adjust('loflom=0,ais=1,lck=0,tim=1,bbe=1,bdi=1'))
            
