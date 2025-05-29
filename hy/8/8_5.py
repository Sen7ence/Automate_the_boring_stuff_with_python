# 生成随机的测验试卷文件
# 35份试卷，50个选择题，随机次序
import random

# 将测验数据保存在字典中
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 生成35份试卷
for quizNum in range(35):
    # 创建试卷和答案文件
    quizFile = open('capitalsquiz%s.txt' % (quizNum+1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum+1), 'w')

    # 写入试卷标题
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' %
                   (quizNum+1) + '\n\n')
    quizFile.write('\n\n')

    # 随机排列州名
    states = list(capitals.keys())  # 生成州名列表
    random.shuffle(states)  # 随机排列州名

    # 生成50道题目
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]  # 正确答案
        wrongAnswers = list(capitals.values())  # 错误答案列表
        # 从错误答案列表里删除正确答案correctAnswer
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)  # 随机抽取3个错误答案
        answerOptions = wrongAnswers+[correctAnswer]  # 将正确答案和错误答案组合在一起
        random.shuffle(answerOptions)  # 随机排列答案选项

        # 写入试卷题目
        quizFile.write('%s.What is the capital of %s?\n' %
                       (questionNum+1, states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' %
                           ('ABCD'[i], answerOptions[i]))  # 写入答案选项
        quizFile.write('\n')  # 换行

        # 写入答案
        answerKeyFile.write('%s. %s\n' % (
            questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))  # 写入答案选项

    quizFile.close()  # 关闭试卷文件
    answerKeyFile.close()  # 关闭答案文件
