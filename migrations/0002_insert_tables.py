from yoyo import step

steps = [
    step(""
         "INSERT INTO exam "
         "(exam_name,question_count,pass_percentage,created_on,""created_by,updated_on,updated_by) VALUES"
         "('Python basics',20,'70',now(),'shashi',now(),'shashi'),"
         "('Core Java',30,'70',now(),'shashi',now(),'shashi')"
         ),
    step(""
         "INSERT INTO technology (name,created_on,created_by,updated_on,updated_by) VALUES"
         "('AWs',now(),'shashi',now(),'shashi'),"
         "('Angular',now(),'shashi',now(),'shashi'),"
         "('React JS',now(),'shashi',now(),'shashi'),"
         "('Python',now(),'shashi',now(),'shashi'),"
         "('Java',now(),'shashi',now(),'shashi');"
         ),
    step("INSERT INTO questions "
         "(question_text,question_image,question_level,technology_id,created_on,created_by,updated_on,updated_by)"
         "VALUES"
         "('Which of the following is an invalid statement?','',2,1,now(),'shashi',now(),'shashi'),"
         "('Which of the following cannot be a variable?','',1,1,now(),'shashi','2020-12-10 10:53:57.295','shashi'),"
         "('Which is the correct operator for power(x^y)?','',3,1,now(),'shashi',now(),'shashi'),"
         "('Which one of these is floor division?','',1,1,now(),'shashi',now(),'shashi'),"
         "('Is Python case sensitive when dealing with identifiers?','',1,1,now(),'shashi',now(),'shashi'),"
         "('What is the maximum possible length of an identifier?','',1,1,now(),'shashi',now(),'shashi'),"
         "('Which of the following is invalid?','',2,1,now(),'shashi',now(),'shashi'),"
         "('Why are local variable names beginning with an underscore discouraged?','',"
         "3,1,now(),'shashi',now(),'shashi'),"
         "('All keywords in Python are in','',1,1,now(),'shashi',now(),'shashi'),"
         "('Which of the following is true for variable names in Python?','',2,1,now(),'shashi',now(),'shashi')"
         ),
     step(""
          "INSERT INTO options "
          "(option_text,correct_option,question_id,created_on,created_by,updated_on,updated_by) VALUES"
          "('abc = 1,000,000',0,1,now(),'shashi',now(),'shashi'),"
          "('a b c = 1000 2000 3000',1,1,now(),'shashi',now(),'shashi'),"
          "('a,b,c = 1000, 2000, 3000',0,1,now(),'shashi',now(),'shashi'),"
          "('a_b_c = 1,000,000',0,1,now(),'shashi',now(),'shashi'),"
          "('__init__',0,2,now(),'shashi',now(),'shashi'),"
          "('in',1,2,now(),'shashi',now(),'shashi'),"
          "('it',0,2,now(),'shashi',now(),'shashi'),"
          "('on',0,2,now(),'shashi',now(),'shashi'),"
          "('X^y',0,3,now(),'shashi',now(),'shashi'),"
          "('X**y',1,3,now(),'shashi',now(),'shashi'),"
          "('None of the mentioned',0,3,now(),'shashi',now(),'shashi'),"
          "('X^^y',0,3,now(),'shashi',now(),'shashi'),"
          "('/',0,4,now(),'shashi',now(),'shashi'),"
          "('//',1,4,now(),'shashi',now(),'shashi'),"
          "('%',0,4,now(),'shashi',now(),'shashi'),"
          "('None of the mentioned',0,4,'2020-12-10 11:01:37.996','shashi','2020-12-10 11:01:37.996','shashi'),"
          "('yes',1,5,'2020-12-10 11:03:25.581','shashi','2020-12-10 11:03:25.581','shashi'),"
          "('no',0,5,'2020-12-10 11:04:28.206','shashi','2020-12-10 11:04:28.206','shashi'),"
          "('machine dependent',0,5,'2020-12-10 11:04:41.833','shashi','2020-12-10 11:04:41.833','shashi'),"
          "('none of the mentioned',0,5,'2020-12-10 11:04:55.255','shashi','2020-12-10 11:04:55.255','shashi'),"
          "('31 characters',0,6,'2020-12-10 11:07:59.296','shashi','2020-12-10 11:07:59.296','shashi'),"
          "('63 characters',0,6,'2020-12-10 11:08:12.137','shashi','2020-12-10 11:08:12.137','shashi'),"
          "('79 characters',0,6,'2020-12-10 11:08:20.698','shashi','2020-12-10 11:08:20.698','shashi'),"
          "('none of the mentioned',1,6,'2020-12-10 11:09:12.310','shashi','2020-12-10 11:09:12.310','shashi'),"
          "('_a = 1',0,7,'2020-12-10 11:10:32.197','shashi','2020-12-10 11:10:32.197','shashi'),"
          "('__a = 1',0,7,'2020-12-10 11:10:43.101','shashi','2020-12-10 11:10:43.101','shashi'),"
          "('__str__ = 1',0,7,'2020-12-10 11:10:54.093','shashi','2020-12-10 11:10:54.093','shashi'),"
          "('none of the mentioned',1,7,'2020-12-10 11:11:19.337','shashi','2020-12-10 11:11:19.337','shashi'),"
          "('they are used to indicate a private variables of a class',1,8,now(),'shashi',now(),'shashi'),"
          "('they confuse the interpreter',0,8,'2020-12-10 11:13:39.630','shashi','2020-12-10 11:13:39.630','shashi'),"
          "('they are used to indicate global variables',0,8,now(),'shashi',now(),'shashi'),"
          "('they slow down execution',0,8,'2020-12-10 11:14:00.244','shashi','2020-12-10 11:14:00.244','shashi'),"
          "('lower case',0,9,'2020-12-10 11:15:53.382','shashi','2020-12-10 11:15:53.382','shashi'),"
          "('UPPER CASE',0,9,'2020-12-10 11:16:04.627','shashi','2020-12-10 11:16:04.627','shashi'),"
          "('Capitalized',0,9,'2020-12-10 11:16:14.026','shashi','2020-12-10 11:16:14.026','shashi'),"
          "('None of the mentioned',1,9,'2020-12-10 11:16:27.259','shashi','2020-12-10 11:16:27.259','shashi'),"
          "('unlimited length',1,10,'2020-12-10 11:17:12.506','shashi','2020-12-10 11:17:12.506','shashi'),"
          "('all private members must have leading and trailing underscores',0,10,now(),'shashi',now(),'shashi'),"
          "('underscore and ampersand are the only two special characters allowed',0,10,now(),'shashi',now(),'shashi'),"
          "('none of the mentioned',0,10,'2020-12-10 11:18:25.527','shashi','2020-12-10 11:18:25.527','shashi')"
     ),
     step(
          "INSERT INTO user_exam_report "
          "(user_id,exam_score,exam_status,exam_id,created_on,created_by,updated_on,updated_by) VALUES"
          "('1956',65,'Fail',1,'2020-12-14 06:34:12.559','shashi','2020-12-14 06:34:12.559','shashi'),"
          "('1956',85,'Pass',1,'2020-12-14 06:34:36.912','shashi','2020-12-14 06:34:36.912','shashi'),"
          "('1934',75,'Pass',2,'2020-12-14 06:34:56.284','shashi','2020-12-14 06:34:56.284','shashi')"
     ),
     step(
          '''INSERT INTO user_exam (submission,meta_data,exam_report_id,created_on,created_by,updated_on,updated_by) VALUES('[
	{"sno":1,
    "question": "Which of the following is an invalid statement?",
    "question_image": "",
    "option_1": "abc = 1,000,000",
    "option_2": "a b c = 1000 2000 3000",
    "option_3": "a,b,c = 1000, 2000, 3000",
    "option_4": "a_b_c = 1,000,000",
    "correct_answer": "a b c = 1000 2000 3000",
    "user_answer": "a,b,c = 1000, 2000, 3000"
	},{
	"sno":2,
	"question": "Which of the following cannot be a variable?",
    "question_image": "",
    "option_1": "__init__",
    "option_2": "in",
    "option_3": "it",
    "option_4": "on",
    "correct_answer": "in",
    "user_answer": "in"
	},
	{
	"sno":3,
    "question": "Which is the correct operator for power(x^y)?",
    "question_image": "",
    "option_1": "X^y",
    "option_2": "X**y",
    "option_3": "None of the mentioned",
    "option_4": "X^^y",
    "correct_answer": "X**y",
    "user_answer": "X^^y"
	}
	]
	','[{
    "ip_address": "168.212. 226.234",
    "session_token": "Frsdfe23",
    "browser": "Google Chrome"
  }]',1,'2020-12-14 13:10:32.319','shashi','2020-12-14 13:10:32.319','shashi') '''
     )
]
