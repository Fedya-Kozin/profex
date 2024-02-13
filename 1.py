import csv
with open('students.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f,delimiter=',')
    count_class={}
    sum_class={}
    for human in reader:
        if 'Хадаров Владимир' in human['Name']:
            print(f'Ты получил: {human["score"]}, за - {human["titleProject_id"]}')
        count_class[human['classs']]=count_class.get(human['classs'],0)+1
        sum_class[human['classs']]=sum_class.get(human['classs'],0)+ (int(human['score']) if human['score'] != 'None' else 0)
with open('students_new.scv','w',encoding='utf-8',newline='') as file:
    f=open('students.csv','r',encoding='utf-8')
    reader = csv.DictReader(f, delimiter=',')
    w=csv.writer(file)
    w.writerow(['id','Name','titleProject_id','classs','score'])
    for line in reader:
        if line['score'] == 'None':
            line['score'] = round(sum_class[line['classs']] / count_class[line['classs']], 3)
        w.writerow([line['id'], line['Name'], line['titleProject_id'], line['classs'], line['score']])